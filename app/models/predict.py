import pandas as pd
import joblib

model = joblib.load('artifacts/xgboost_model.pkl')
encoders = joblib.load('artifacts/label_encoders.pkl')


def predict_price(data):

    df = pd.DataFrame([data])

    # Encode categorical columns
    categorical_cols = ['category', 'season']

    for col in categorical_cols:

        encoder = encoders[col]

        # Handle unseen labels
        if df[col][0] not in encoder.classes_:
            df[col] = encoder.transform([encoder.classes_[0]])
        else:
            df[col] = encoder.transform(df[col])

    # -----------------------------
    # Feature Engineering
    # -----------------------------

    # Simulated rolling features
    df['rolling_demand_5'] = df['demand']

    df['rolling_sales_5'] = (
        df['demand'] * df['base_price']
    )

    df['inventory_demand_ratio'] = (
        df['inventory'] / (df['demand'] + 1)
    )

    df['competitor_gap'] = (
        df['base_price'] - df['competitor_price']
    )

    # Match training feature order
    feature_order = [
        'product_id',
        'category',
        'demand',
        'inventory',
        'competitor_price',
        'season',
        'base_price',
        'rolling_demand_5',
        'rolling_sales_5',
        'inventory_demand_ratio',
        'competitor_gap'
    ]

    df = df[feature_order]

    prediction = model.predict(df)[0]

    return round(float(prediction), 2)