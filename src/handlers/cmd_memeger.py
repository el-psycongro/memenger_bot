from aiogram import types
from common import dp
from models.models import User, Chat
from sqlalchemy.orm import Session
from schedulers.scheduler import scheduler
from schedulers.workers import memenger_send
from datetime import datetime
import pytz

kiev_tz = pytz.timezone('Europe/Kiev')


@dp.message_handler(commands=['memenger'])
async def cmd_memenger(message: types.Message):
    time_now = datetime.now(tz=kiev_tz)
    hour, minute = time_now.hour, time_now.minute

    args = message.get_args()
    if args:
        time = args.split(':')
        if len(time) == 2:
            hour, minute = time
        elif len(time) == 1:
            hour = time[0]

    scheduler.add_job(func=memenger_send, trigger='cron', args=[str(message.chat.id)], hour=hour, minute=minute)
