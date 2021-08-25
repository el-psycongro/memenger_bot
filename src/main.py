import asyncio
import logging
from common import bot, dp, engine
from models.models import Base
from services.sheduler import scheduler


async def main():
    logging.basicConfig(level=logging.INFO)
    import handlers

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    scheduler.start()

    try:
        await dp.start_polling()
    finally:
        scheduler.shutdown()
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped!")
