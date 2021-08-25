from aiogram import Bot, Dispatcher
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from config import API_TOKEN, POSTGRES_URL

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

engine = create_async_engine(POSTGRES_URL, future=True)
Session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
