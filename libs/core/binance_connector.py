from binance import ThreadedWebsocketManager
import os

class BinanceWS:
    def __init__(self, pair, callback):
        self.pair = pair.lower()
        self.callback = callback
        self.bsm = ThreadedWebsocketManager(
            api_key=os.getenv("BINANCE_API_KEY"),
            api_secret=os.getenv("BINANCE_SECRET")
        )

    def start(self):
        self.bsm.start()
        self.bsm.start_kline_socket(callback=self.on_kline, symbol=self.pair, interval="1m")

    def on_kline(self, msg):
        if msg["e"] == "kline":
            self.callback(msg["k"])
