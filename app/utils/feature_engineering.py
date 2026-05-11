import pandas as pd
from sklearn.preprocessing import LabelEncoder


def preprocess_data(df):

    df['inventory_demand_ratio'] = (
        df['inventory'] / (df['demand'] + 1)
    )

    df['competitor_gap'] = (
        df['base_price'] - df['competitor_price']
    )

    categorical_cols = ['category', 'season']

    encoders = {}

    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le

    return df, encoders