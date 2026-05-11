import pandas as pd
import joblib

from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

from app.utils.feature_engineering import preprocess_data
from app.utils.demand_window import create_sliding_window_features


def train():

    df = pd.read_csv('app/data/ecommerce_pricing.csv')

    df = create_sliding_window_features(df)

    df, encoders = preprocess_data(df)

    X = df.drop(columns=['sales'])
    y = df['sales']

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = XGBRegressor(
        n_estimators=500,
        learning_rate=0.03,
        max_depth=8,
        subsample=0.9,
        colsample_bytree=0.9,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)

    print(f'MAE: {mae}')

    joblib.dump(model, 'app/models/pricing_model.pkl')
    joblib.dump(encoders, 'app/models/encoders.pkl')


if __name__ == '__main__':
    train()