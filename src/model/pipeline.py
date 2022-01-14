import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.config.config import TOTAL_NUM_FEATURES, CAT_FEATURES, RANDOM_SEED

num_pipe = Pipeline([
    ('num_impute_median', SimpleImputer(strategy= 'median')),
    ('ss',StandardScaler())
])

cat_pipe = Pipeline([
    ('ohe',OneHotEncoder(drop='first'))
])

transform_pipe = ColumnTransformer([
    ('num_transform', num_pipe,TOTAL_NUM_FEATURES),
    ('cat_transform',cat_pipe,CAT_FEATURES)
])

survive_pipe_rfc = Pipeline([
    ('transform',transform_pipe),
    ('rfc',RandomForestClassifier(random_state=RANDOM_SEED))
])