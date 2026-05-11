import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title('AI Dynamic Pricing Engine')

product_id = st.number_input(
    'Product ID',
    value=101
)

category = st.selectbox(
    'Category',
    [
        'Electronics',
        'Fashion',
        'Books',
        'Grocery',
        'Home',
        'Sports'
    ]
)

demand = st.slider(
    'Demand',
    1,
    1000,
    300
)

inventory = st.slider(
    'Inventory',
    1,
    1000,
    100
)

competitor_price = st.number_input(
    'Competitor Price',
    value=100.0
)

season = st.selectbox(
    'Season',
    [
        'Summer',
        'Winter',
        'All',
        'Festival'
    ]
)

base_price = st.number_input(
    'Base Price',
    value=80.0
)

chart_df = pd.DataFrame({
    'Metric': ['Demand', 'Inventory'],
    'Value': [demand, inventory]
})

fig = px.bar(
    chart_df,
    x='Metric',
    y='Value',
    title='Demand vs Inventory'
)

st.plotly_chart(fig)

if st.button('Generate Price'):

    payload = {
        'product_id': product_id,
        'category': category,
        'demand': demand,
        'inventory': inventory,
        'competitor_price': competitor_price,
        'season': season,
        'base_price': base_price
    }

    try:

        response = requests.post(
            'http://localhost:8000/predict-price',
            json=payload
        )

        st.write("Status Code:", response.status_code)

        st.write("Raw Response:", response.text)

        result = response.json()

        st.success(
            f"Recommended Price: ₹{result['recommended_price']}"
        )

        st.write(
            f"Latency: {result['latency_ms']} ms"
        )

    except Exception as e:

        st.error(f"Error: {e}")
    