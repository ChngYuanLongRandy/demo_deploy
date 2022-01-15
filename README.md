# Contents
1. [Name of Candidate](#name-of-candidate)
2. [Overview of folder structure](#overview-of-folder-structure)
3. [Running instructions](#running-instructions)
4. [Description of logical steps/ flow of pipeline](#description-of-logical-steps-flow-of-pipeline)
5. [Overview of Key findings in EDA and Pipeline, Feature Engineering Choices](#overview-of-key-findings-in-eda-and-pipeline-feature-engineering-choices)
6. [Model choices](#model-choices)
7. [Evaluation choices](#evaluation-choices)
8. [Other Considerations](#other-considerations)

------------------------------
## Name of Candidate
------------------------------
[Back to content page](#contents)

Hi! My name is :

>Chng Yuan Long, Randy

Email:

>chngyuanlong@gmail.com

------------------------------
## Overview of folder structure
------------------------------

[Back to content page](#contents)

### Folder structure:
```
AIAP
│  README.md
│  requirements.txt    
│  test-requirements.txt
|  run.sh
|  Dockerfile
|  eda.ipynb
|  tox.ini
|  
└──data
|  survive.db
|
└──src
   |  main.py
   |  file012.txt
   │
   └──config
   |     config.py
   |   
   └──preprocessing
   |     datamanager.py
   |
   └──tests
   |     test_bound_outliers.py
   |     test_load_from_database.py
   |     test_pipeline.py
   |     test_predict.py
   |     test_preprocess_data.py
   |     test_preprocess_input.py
   |
   └──model
         pipeline.pkl
         pipeline.py
         predict.py
         train_pipeline.py
```
### File Summary:
Format: File (folder)
- Usage

main.py (src)
- runs application

Config.py (src/config)
- Tweak variables in config/config files
   - File paths
   - model specific objects (CV, test ratio, random seed, params for cross validation)
   - Column names

Datamanager.py (src/Preprocessing)
- loads pipeline, data
- preprocesses input from application, data from database after reading

python files (src/tests)
- tests functions in the respective python files

Train-Pipeline.py (src/model)
- trains and scores the pipeline with the data in data folder
- outputs pipeline.pkl and a log on training outcome in the same folder

Pipeline.py (src/model)
- contains pipeline to transform data

predict.py (src/model)
- predicts inputs using pipeline trained on data in data folder

------------------------------
## Running instructions
------------------------------

[Back to content page](#contents)

You can run the application straight with either the bash script or from docker.
Optionally, you may run tests or train the pipeline on data in the data folder or run lint tools on the code.
A trained pipeline named pipeline.pkl should already be included in the src/model folder.

Default values are present on the application itself so that you can click on predict button at the end. If prediction is 0, message 'Please see a doctor!' will appear. Otherwise it will appear as 'Please keep up the healthy habits'.

The instructions below assumes a Windows OS

### Running Main Application
1. Bash Script: 

Run bash script (run.sh) by double clicking it. Streamlit application should appear in your browser. 

2. Docker:

Please pull image by running command in terminal with docker running

   >docker pull hashketh/aiap

Once retrieved, please run command 

   >docker run hashketh/aiap

The streamlit should be available in your browser via 

   >localhost:8501

### Running optional tests

------------------------------
## Description of logical steps flow of pipeline
------------------------------

[Back to content page](#contents)

I imagine the user would like to test the application first. After that they might want to train the model on the data.

They may do both using the package tox to test the application.

After that they can run the application. The application will then start by 

Train -> Ingest Data -> Preprocessing -> 


------------------------------
## Overview of Key findings in EDA and Pipeline Feature Engineering Choices
------------------------------

[Back to content page](#contents)

The dataset contains a moderate amount of features with 150K observations. Numerical features are typically tail heavy with some features require cleaning or imputing. Likewise the categorical features require some cleaning as well. Most numerical features do no correlate with the target and with each other. 

As I think that domain knowledge is useful in feature engineering and I do not have any medical knowledge, I tried to use polynomial transformation to see if any interactions between the numerical features will yield any strong correlation with the target however that is not the case. The only feature introduced is BMI and that appeared to be rather correlated to the target which is why it was kept.

The pipeline included median imputation of possible null values , bounding outliers within the distribution and the usual scaling or numerical features and one-hot encoding of categorical features. 

------------------------------
## Model choices
------------------------------

[Back to content page](#contents)

I used the following models
- Logistic Regression (LOGREG)
- Support Vector Machines (SVM)
- K-Nearest Neighbours (KNN)
- Random Forest (RF)
- Light Gradient Boosting Machine (LGBM)

The models used to train were chosen based on how complex the models are, whether they are ensemble models or not and where it is instance or model based. I originally intended to compare the models on the validation data and then choose 1 to perform hyperparamter tunning to achieve better results. However the models happen to give me good results that I dont need to tune hyperparameters.

Another selection criterion is also whether if there is any indication of overfitting on the data. Based on the training and test cross validation scores provided, I can see if a model is prone to overfit or not. If there is overfitting I can regularise the model or choose a less complex model. If there is underfitting I will choose a more complex model

LOGREG is the simplest of them all being a linear model. A simple model has its usefulness however it is unable to fit well onto the data using the default values.

SVM 

KNN is an instance based model that does not have any algorithim but predicts based on distance of the training data to the new instances for predictions.

RF is an ensemble model of decision trees which is prone to overfitting. Typically I will fit using default and then prune (regularise) the tree later.

LGBM is an ensemble model that improves on every iteration by adjusting to the residual error of the previous iteration. My understanding is that the LGBM is a variant of XGBoost that is faster. XGBoost is itself a more regularised variant of Gradient Boosting machine.   

I intitally chose to use LGBM as it provided the highest score on all metrics with accuracy taking precedence. It is also the fastest to train. However when I was building the application I have some issues running the LGBM model so I used random forest instead as it is the runner up with the same scoring on all metrics just a tad bit slower when training.

------------------------------
## Evaluation choices
------------------------------

[Back to content page](#contents)

As this is a classification problem, scores like recall, precision, accuracy, F1 score and the ROC AUC score are relevant.

The problem is about predicting the surival of a patient suffering from heart artery disease and I think between choosing a low false negative rate or a low false positive rate, a low false negative rate will take priority since the outcome of a false positive (predicted death when it is survive) is less disastrous than a false negative (predicted survive when it is death). The model should have high recall

------------------------------
## Other Considerations
------------------------------

[Back to content page](#contents)

This deployment is built with ease of use and maintenance in mind. 

A couple of design choices are made to this end:
Tox allows me to run a couple of virtual environments and commands in a easy manner. With Tox, I can use pytest, run lint packages on the code and train the model on the training data.

Pytest allows me and any other users to ensure that the code is working properly. I have written pre-train and post-train test cases so that I can cover both the data and the functions in the model and the behavior of the model.

Lint tools like black, isort and flake8 formats and flags out inconsistencies with the code in accordance with PEP8.

The model is also containerised in docker so we can avoid the "it only runs on my machine problem". This is done in the event that the bash script fails to run the application for some reason.

