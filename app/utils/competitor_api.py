import requests
import random


def get_competitor_price(product_name):

    # Replace with real API in production
    simulated_price = round(random.uniform(50, 1000), 2)

    return {
        'product': product_name,
        'competitor_price': simulated_price
    }