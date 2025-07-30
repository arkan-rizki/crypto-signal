def build_confluence(volume_score, pattern_score, regime):
    base = (volume_score + pattern_score) / 2
    if regime == "Trending":
        base += 10
    return min(base, 100)
