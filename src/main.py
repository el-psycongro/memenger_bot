import asyncio
import logging
from common import dp, engine
from models.base import Base


async def main():
    logging.basicConfig(level=logging.INFO)
    import handlers

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()


if __name__ == '__main__':
    asyncio.run(main())


