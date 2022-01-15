from src.config.config import PIPELINE_PATH
from src.preprocessing import datamanager


def make_prediction_inputs(input_data:list, proba = False) -> int:
    survive_pipeline = datamanager.load_pipeline(PIPELINE_PATH)
    processed_input = datamanager.preprocess_input(input_data)
    if proba:
        prediction_proba = survive_pipeline.predict_proba(processed_input)
        return prediction_proba
    else:
        prediction = survive_pipeline.predict(processed_input)
        return prediction