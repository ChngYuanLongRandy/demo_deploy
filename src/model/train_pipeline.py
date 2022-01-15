import joblib
from sklearn.model_selection import GridSearchCV, train_test_split
from src.config.config import DATABASE_PATH, TOTAL_FEATURES, TARGET, TEST_RATIO, RANDOM_SEED, CV, PARAMS, \
    MODEL_PATH, PIPELINE_PATH, ROOT, SRC_ROOT, MODEL_NAME
from src.model.pipeline import survive_pipe_rfc
from src.preprocessing import datamanager
from sklearn.model_selection import cross_validate
from sklearn.metrics import classification_report, roc_auc_score
from src.config.config import CV
from time import time


def run_trainpipeline(gridsearch=False):
    df = datamanager.load_from_database(DATABASE_PATH)

    print(df.head())
    print(df.iloc[0])
    print(df[TOTAL_FEATURES])
    print(df[TARGET])
    print(df.isna().sum())

    X_train, X_test, y_train, y_test = train_test_split(
        df[TOTAL_FEATURES],
        df[TARGET],
        test_size=TEST_RATIO,
        random_state=RANDOM_SEED,
    )

    if gridsearch:
        print('Gridsearch = True')
        try:
            model = GridSearchCV(
                survive_pipe_rfc,
                PARAMS,
                cv=CV
            )
            score_pipeline(model, X_train, y_train, X_test, y_test)
            joblib.dump(model, PIPELINE_PATH)
        except Exception:
            raise Exception('Unable to proceed, please check Parameters')

        joblib.dump(model, PIPELINE_PATH)
    else:
        print('Gridsearch = False')
        survive_pipe_rfc.fit(X_train, y_train)
        score_pipeline(survive_pipe_rfc, X_train, y_train, X_test, y_test)
        joblib.dump(survive_pipe_rfc, PIPELINE_PATH)


def score_pipeline(model,X_train, y_train, X_test, y_test):
    now = time()
    y_pred = model.predict(X_test)

    model_cv_score = cross_validate(model, X_train, y_train,
                                    cv=CV,
                                    n_jobs=-1,
                                    return_train_score=True,
                                    scoring='accuracy')
    then = time()
    diff = then - now
    output_logfile(model,model_cv_score, y_test, y_pred, diff)


def output_logfile(model, model_cv_score,y_test, y_pred, diff):
    with open('log_file.txt', 'w') as log_file:
        log_file.write('Log file for model results\n')
        log_file.write('Model is ' + MODEL_NAME+ '\n')
        log_file.write(f'Classifcation report :\n{classification_report(y_test, y_pred)}'+ '\n')
        log_file.write(f'Average CV train acc score : \n {model_cv_score["train_score"].mean()} '+ '\n')
        log_file.write(f'Average CV test acc score : \n {model_cv_score["test_score"].mean()} '+ '\n')
        log_file.write(f'ROC AUC score :\n {roc_auc_score(y_test, y_pred)}'+ '\n')
        log_file.write(f'Seconds taken to run results is {diff}')



if __name__ == "__main__":
    run_trainpipeline()
