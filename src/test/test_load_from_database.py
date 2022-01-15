from src.preprocessing.datamanager import load_from_database, preprocess_data, return_min_max_boxplot, bound_outliers, preprocess_input
from src.config.config import SAMPLE_DATA_PATH, ORI_NUM_FEATURES, TOTAL_FEATURES, CAT_FEATURES, TOTAL_NUM_FEATURES, DATABASE_PATH, TOTAL_FEATURES_W_TARGET, ORI_FEATURES
import pandas as pd
import numpy as np
import pytest

sample_data = pd.read_csv(SAMPLE_DATA_PATH)
processed_sample_data = preprocess_data(sample_data)

sample_input =[
  "Male",
  "Yes",
  "Normal",
  21,
  "Low",
  120,
  0.2,
  266000,
  100,
  105,
  16.3,
  185,
  80,
  23.374726077428782
]

def test_load_from_database():
    """
    checks if the columns retrieved are all present
    :return:
    """

    sample_database = load_from_database(DATABASE_PATH)

    assert (sample_database.columns.to_list() ==  TOTAL_FEATURES_W_TARGET)