def generate_risk(close_price):
    close = float(close_price)
    return {
        "entry": close,
        "tp1": close + 50,
        "tp2": close + 100,
        "tp3": close + 150,
        "sl": close - 75
    }
