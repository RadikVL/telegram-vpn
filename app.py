import os
import asyncio
import logging
from aiogram import Bot, Dispatcher

from main.handlers.user_handlers import router
from dotenv import load_dotenv

load_dotenv('gitignoref/.env') # add folder 'gitignoref' with file .env. Put in it 'TOKEN=your_token'
TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main() -> None: # entry point
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except Exception as _ex:
        print(_ex)
