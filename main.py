from dotenv import load_dotenv
from libs.utils.helpers import get_active_pair
from bot.telegram_bot import AlertBot
from libs.core.binance_connector import BinanceWS
from libs.engine.signal_generator import SignalEngine

def main():
    load_dotenv()
    pair = get_active_pair()
    bot = AlertBot()
    engine = SignalEngine(bot_callback=bot.send)
    stream = BinanceWS(pair=pair, callback=engine.analyze)
    stream.start()

if __name__ == "__main__":
    main()
