import os
from telegram import Bot
from telegram.ext import Application, CommandHandler
from bot.commands.switch_pair import set_pair
from bot.commands.report import report_accuracy
from bot.commands.emergency import emergency_stop

class AlertBot:
    def __init__(self):
        self.token = os.getenv("TG_BOT_TOKEN")
        self.chat_id = os.getenv("TG_CHAT_ID")
        self.bot = Bot(self.token)

        # Async bot handler
        self.app = Application.builder().token(self.token).build()
        self.app.add_handler(CommandHandler("set_pair", set_pair))
        self.app.add_handler(CommandHandler("report_accuracy", report_accuracy))
        self.app.add_handler(CommandHandler("emergency_stop", emergency_stop))
        self.app.run_polling(allowed_updates=[])
        
    def send(self, message):
        try:
            self.bot.send_message(chat_id=self.chat_id, text=message)
        except Exception as e:
            print(f"[Telegram Error] {e}")
