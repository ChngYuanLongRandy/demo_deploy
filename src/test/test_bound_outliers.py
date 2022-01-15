from src.preprocessing.datamanager import load_from_database, preprocess_data, return_min_max_boxplot, bound_outliers, preprocess_input
from src.config.config import SAMPLE_DATA_PATH, ORI_NUM_FEATURES, TOTAL_FEATURES, CAT_FEATURES, TOTAL_NUM_FEATURES
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

def test_bound_outliers():
    """
    test if the outliers have been cap to the min or max
    :return: None
    """
    arbitary_value = 1
    for col in ORI_NUM_FEATURES:
        ori_min = processed_sample_data[col].min()
        ori_max = processed_sample_data[col].max()

        bound_outliers(processed_sample_data, col)

        current_min = processed_sample_data[col].min()
        current_max = processed_sample_data[col].max()

        assert (ori_min-arbitary_value <= current_min)
        assert (ori_max+arbitary_value >= current_max)
