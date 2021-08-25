from aiogram import types
from main import dp


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply('Hi, I`m manager bot\n')
