import os
from pathlib import Path

# main folders
CONFIG_PATH = os.path.dirname(__file__) #aiap/src/config
SRC_ROOT = Path(CONFIG_PATH).parent #aiap/src
ROOT = Path(SRC_ROOT).parent #aiap

DATA_PATH = os.path.join(ROOT,'data') #aiap/data
MODEL_PATH = os.path.join(SRC_ROOT,'model') #aiap/src/model
PREPROCESSING_PATH = os.path.join(SRC_ROOT,'preprocessing') #aiap/src/preprocessing

# Objects
DATABASE_PATH = os.path.join(DATA_PATH,'survive.db') # aiap/data/survive.db
PIPELINE_NAME = 'pipeline.pkl'
PIPELINE_PATH = os.path.join(MODEL_PATH,PIPELINE_NAME) #aiap/src/model/pipeline.pkl

# model specific objects
RANDOM_SEED = 42
CV = 5
TEST_RATIO = 0.2
PARAMS= {} #insert params configuration here

# data base specific objects
TARGET = ['Survive']
CAT_FEATURES = ['Gender','Smoke','Diabetes','Ejection Fraction']
ORI_NUM_FEATURES = ['Sodium', 'Creatinine', 'Pletelets', 'Creatinine phosphokinase','Blood Pressure', 'Hemoglobin', 'Height' , 'Weight']
TOTAL_NUM_FEATURES = ['Age','Sodium','Creatinine','Pletelets','Creatinine phosphokinase','Blood Pressure','Hemoglobin','Height','Weight','BMI']

TOTAL_FEATURES = ['Gender','Smoke','Diabetes','Age','Ejection Fraction','Sodium','Creatinine','Pletelets','Creatinine phosphokinase','Blood Pressure','Hemoglobin','Height','Weight','BMI']
TOTAL_FEATURES_W_TARGET = TOTAL_FEATURES + TARGET

# streamlit-specific objects
