from logging import Handler, LogRecord
from os import getenv

from telebot import TeleBot
from telebot.util import antiflood

bot = TeleBot(getenv('TELEGRAM_TOKEN', ''))
ERROR_CHAT_ID = getenv('ERROR_CHAT_ID', '')
MAX_MESSAGE_LENGTH = 4096


class TelegramHandler(Handler):
    def __init__(self) -> None:
        super().__init__()
        self.bot = bot
        self.chat_id = ERROR_CHAT_ID
        self.MAX_MESSAGE_LENGTH = MAX_MESSAGE_LENGTH

    def emit(self, record: LogRecord) -> None:
        log_entry = self.format(record)
        for i in range(0, len(log_entry), self.MAX_MESSAGE_LENGTH):
            antiflood(
                self.bot.send_message,
                self.chat_id,
                log_entry[i : i + self.MAX_MESSAGE_LENGTH],
            )
