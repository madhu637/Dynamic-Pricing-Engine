import pandas as pd


def create_sliding_window_features(df):

    df['rolling_demand_5'] = (
        df['demand']
        .rolling(window=5, min_periods=1)
        .mean()
    )

    df['rolling_sales_5'] = (
        df['sales']
        .rolling(window=5, min_periods=1)
        .mean()
    )

    return df