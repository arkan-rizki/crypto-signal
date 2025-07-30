def detect_pattern(candle):
    o = float(candle["o"])
    c = float(candle["c"])
    h = float(candle["h"])
    l = float(candle["l"])

    if c > o and (c - o) > (h - l) * 0.5:
        return "Bullish Engulfing", 85
    elif o > c and (o - c) > (h - l) * 0.5:
        return "Bearish Engulfing", 85
    return "No Clear Pattern", 40
