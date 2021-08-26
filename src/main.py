import logging


async def main():
    # Configure logging
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('apsscheduler').setLevel(logging.INFO)

    # Database create tables
    from common import engine
    from models.models import Base
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Apscheduler
    from schedulers.scheduler import scheduler
    scheduler.start()

    # Start bot
    import handlers
    from common import dp, bot
    from utils.commands import set_commands
    from schedulers.workers import memenger_send

    try:
        #scheduler.add_job(func=memenger_send, trigger='interval', args=[str(1342614252)], minutes=1)
        await set_commands()
        await dp.start_polling()
    finally:
        scheduler.shutdown()
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    import asyncio
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped!")
