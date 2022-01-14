from src.config.config import PIPELINE_PATH
from src.preprocessing import datamanager


def make_prediction_inputs(input_data:list) -> int:
    survive_pipeline = datamanager.load_pipeline(PIPELINE_PATH)
    processed_input = datamanager.preprocess_input(input_data)
    prediction = survive_pipeline.predict(processed_input)
    return prediction