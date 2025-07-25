import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from handlers import register_handlers
from secret_info import TOKEN

API_TOKEN = TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

register_handlers(dp)


async def on_startup(dp):
    logging.info("Бот запущен")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
