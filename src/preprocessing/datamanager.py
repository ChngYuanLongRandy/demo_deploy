import joblib
import pandas as pd
import sqlite3 as sq3
import numpy as np
from src.config.config import TOTAL_FEATURES

def preprocess_input(inputs: list) -> pd.DataFrame:
    inputs = np.array(inputs).reshape(1,-1)
    rename_cols = {k: v for k, v in zip(range(len(TOTAL_FEATURES)), TOTAL_FEATURES)}
    df = pd.DataFrame(inputs).rename(columns=rename_cols)
    return df


def preprocess_data(df) -> pd.DataFrame:
    df.drop(columns=['ID', 'Favorite color'], inplace = True)
    df.Survive = df.Survive.str.replace('No', '0')
    df.Survive = df.Survive.str.replace('Yes', '1')
    df.Survive = df.Survive.astype('int')
    df.Smoke = df.Smoke.replace('NO', 'No')
    df.Smoke = df.Smoke.replace('YES', 'Yes')
    df.Age = np.where(df.Age < 0, -df.Age, df.Age)
    df['Ejection Fraction'] = df['Ejection Fraction'].replace('L', 'Low').replace('N', 'Normal')
    df['Ejection Fraction'] = df['Ejection Fraction'].replace('High', 'Normal').replace('Normal', 'Normal-High')
    df['BMI'] = (df.Weight / df.Height / df.Height) * 10000

    return df


def load_from_database(db_path, custom_query=None) -> pd.DataFrame:
    con = sq3.Connection(db_path)
    if custom_query is not None:
        try:
            df: pd.DataFrame = pd.read_sql(custom_query, con)
        except:
            pass # TODO
    else:
        query = '''SELECT * FROM SURVIVE'''
        df: pd.DataFrame = pd.read_sql(query, con)

    df_processed = preprocess_data(df)
    return df_processed




def load_pipeline(pipe_path) ->'pipeline':
    pipe = joblib.load(filename=pipe_path)
    return pipe