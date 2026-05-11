import time
from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel

from app.models.predict import predict_price

app = FastAPI(
    title="Dynamic Pricing Engine API",
    description="AI-powered pricing optimization using XGBoost",
    version="1.0.0"
)


class ProductInput(BaseModel):

    product_id: int

    category: Literal[
        "Electronics",
        "Fashion",
        "Books",
        "Grocery",
        "Home",
        "Sports"
    ]

    demand: int

    inventory: int

    competitor_price: float

    season: Literal[
        "Summer",
        "Winter",
        "All",
        "Festival"
    ]

    base_price: float


@app.get("/")
def root():

    return {
        "message": "Dynamic Pricing API Running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post("/predict-price")
def predict(product: ProductInput):

    start_time = time.time()

    result = predict_price(product.dict())

    latency = round(
        (time.time() - start_time) * 1000,
        2
    )

    return {
        "recommended_price": result,
        "latency_ms": latency
    }