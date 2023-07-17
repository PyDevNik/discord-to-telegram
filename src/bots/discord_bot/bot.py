import discord
from discord.ext.commands import Bot, when_mentioned
from ...database.db import DB
from ..telegram_bot.bot import forward_message

bot = Bot(
        command_prefix=when_mentioned, 
        intents=discord.Intents.all(),
        help_command=None
        )

db = DB()

@bot.event
async def on_message(msg):
    if not msg.author.bot:
        await forward_message(msg)