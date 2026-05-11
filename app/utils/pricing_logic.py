def apply_business_rules(predicted_price, inventory, demand, competitor_price):

    if inventory < 50:
        predicted_price *= 1.10

    if demand > 300:
        predicted_price *= 1.15

    blended_price = (0.7 * predicted_price) + (0.3 * competitor_price)

    return round(blended_price, 2)