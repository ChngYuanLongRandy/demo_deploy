from src.model.pipeline import num_pipe, cat_pipe, transform_pipe, survive_pipe_rfc
import pandas as pd
import numpy as np
from src.config.config import SAMPLE_DATA_PATH, TOTAL_NUM_FEATURES, CAT_FEATURES, RANDOM_SEED
from src.preprocessing.datamanager import preprocess_data


def test_pipeline():
    """
    test no Na values from pipeline output
    :return: None
    """
    sample_data = pd.read_csv(SAMPLE_DATA_PATH)
    processed_sample_data = preprocess_data(sample_data)

    transformed_processed_sample_data = transform_pipe.fit_transform(processed_sample_data)

    assert(np.all(pd.DataFrame(transformed_processed_sample_data).isna()).sum() == 0)
