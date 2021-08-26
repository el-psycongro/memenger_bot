from aiogram.types import BotCommand
from common import bot


async def set_commands():
    commands = [
        BotCommand(command='/start', description='Start bot'),
        BotCommand(command='/memenger', description='Start AI manager'),
    ]

    await bot.set_my_commands(commands=commands)
