import joblib
from sklearn.model_selection import GridSearchCV, train_test_split
from src.config.config import DATABASE_PATH, TOTAL_FEATURES, TARGET, TEST_RATIO, RANDOM_SEED, CV, PARAMS, \
    MODEL_PATH, PIPELINE_PATH, ROOT, SRC_ROOT
from src.model.pipeline import survive_pipe_rfc
from src.preprocessing import datamanager


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
        except:
            pass  # TODO

        joblib.dump(model, PIPELINE_PATH)
    else:
        print('Gridsearch = False')
        survive_pipe_rfc.fit(X_train, y_train)

    joblib.dump(survive_pipe_rfc, PIPELINE_PATH)


if __name__ == "__main__":
    run_trainpipeline()
