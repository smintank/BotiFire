import asyncio
import logging
import os
from aiogram import Bot, Dispatcher

from handlers import user_handlers, other_handlers

logging.basicConfig(level=logging.INFO)


async def main():
    logging.info('Starting bot')

    bot: Bot = Bot(token=os.getenv("TG_API"), parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error('Bot stopped')
