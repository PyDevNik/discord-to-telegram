from .telegram_bot.bot import dp
from .discord_bot.bot import bot
from ..config import DISCORD_TOKEN
from threading import Thread

telegram = Thread(target=dp.run_polling)
discord = Thread(target=bot.run, args=(DISCORD_TOKEN,))

telegram.start()
discord.start()