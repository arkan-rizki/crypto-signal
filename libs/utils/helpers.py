import os

def get_active_pair():
    return os.getenv("ACTIVE_PAIR", "BTCUSDT")

def safe_float(val, fallback=0.0):
    try:
        return float(val)
    except:
        return fallback
