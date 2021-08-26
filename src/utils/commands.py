from aiogram.types import BotCommand
from aiogram.types.bot_command_scope import BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats
from common import bot


async def set_commands():
    commands = [
        BotCommand(command='/start', description='Start bot'),
        BotCommand(command='/memenger', description='Start AI manager'),
    ]

    await bot.set_my_commands(commands=commands, scope=BotCommandScopeAllPrivateChats())
