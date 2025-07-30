from libs.engine.pattern_detector import detect_pattern
from libs.engine.confluence_builder import build_confluence
from libs.engine.risk_manager import generate_risk
from libs.core.market_regime import detect_regime
from libs.core.onchain import get_funding_rate
from libs.utils.helpers import safe_float

class SignalEngine:
    def __init__(self, bot_callback):
        self.bot_callback = bot_callback

    def analyze(self, kline):
        if not kline["x"]:
            return

        close = safe_float(kline["c"])
        volume = safe_float(kline["v"])
        pattern, pattern_score = detect_pattern(kline)
        regime = detect_regime()
        funding = get_funding_rate()

        volume_score = 90 if volume > 100 else 50
        confidence = build_confluence(volume_score, pattern_score, regime)
        risk = generate_risk(close)

        signal = (
            f"📊 Pair: {kline['s']}\n"
            f"📈 Market: {regime}\n"
            f"⚠️ Kondisi: {pattern}\n\n"
            f"🎯 Signal: BUY\n"
            f"Confidence: {confidence:.1f}%\n"
            f"Entry: {risk['entry']}\n"
            f"TP1: {risk['tp1']} | TP2: {risk['tp2']} | TP3: {risk['tp3']}\n"
            f"SL: {risk['sl']}\n"
            f"Funding: {funding}"
        )

        if confidence >= 80:
            self.bot_callback(signal)
