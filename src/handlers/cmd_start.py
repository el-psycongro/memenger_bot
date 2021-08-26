from aiogram import types
from common import dp
from models.models import User, Chat
from sqlalchemy.orm import Session


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    s_maker = message.bot.get('sessionmaker')
    async with s_maker() as session:
        session: Session

        await session.merge(Chat(
            chat_id=message.chat.id,
            type=message.chat.type,
            title=message.chat.title,
        ))

        await session.merge(User(
            user_id=message.from_user.id,
            is_bot=message.from_user.is_bot,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            username=message.from_user.username,
            language_code=message.from_user.language_code,
            chat_id=message.chat.id
        ))
        await session.commit()

    await message.reply('Hi, I`m manager bot\n')
