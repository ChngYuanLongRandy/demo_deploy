from src.preprocessing.datamanager import load_from_database, preprocess_data, return_min_max_boxplot, bound_outliers, preprocess_input
from src.config.config import SAMPLE_DATA_PATH, ORI_NUM_FEATURES, TOTAL_FEATURES, CAT_FEATURES, TOTAL_NUM_FEATURES
import pandas as pd
import numpy as np
import pytest



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
def test_preprocess_data():
    """
    test if the processed data has the correct cols, data types, shape and unique values
    :return:
    """

    sample_data = pd.read_csv(SAMPLE_DATA_PATH)
    processed_sample_data = preprocess_data(sample_data)

    # Check columns
    assert ('ID' not in processed_sample_data.columns.to_list())
    assert ('Favourite Color' not in processed_sample_data.columns.to_list())

    # check unique values
    assert (len(processed_sample_data['Smoke'].value_counts())==2)
    assert (len(processed_sample_data['Survive'].value_counts())==2)
    assert (len(processed_sample_data['Ejection Fraction'].value_counts())==2)

    pass


