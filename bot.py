import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

storage: MemoryStorage = MemoryStorage()

from handlers import command_handlers, other_handlers, fms_menu


logging.basicConfig(level=logging.INFO)


async def main():
    logging.info('Starting bot')

    bot: Bot = Bot(token=os.getenv("TG_API"), parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=storage)

    dp.include_router(command_handlers.router)
    dp.include_router(fms_menu.router)
    dp.include_router(other_handlers.router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error('Bot stopped')
