from aiogram import Bot, Dispatcher
from aiogram.types import URLInputFile
from typing import List
import discord
from commands import add_discord_id, start, admin, button_callbacks
from ...config import TELEGRAM_TOKEN, CONTENT_TYPES
from ...database.db import DB

bot = Bot(TELEGRAM_TOKEN)
dp = Dispatcher(bot)
db = DB()

async def forward_message(msg: discord.Message):
    chat_id = db.find_user(discord_id=msg.author.id)
    await bot.send_message(chat_id, msg.content)
    if msg.attachments:
        await send_files(chat_id, msg.attachments)

async def send_files(chat_id, attachments: List[discord.Attachment]):
    result = []
    for attachment in attachments:
        Type = CONTENT_TYPES[attachment.content_type.split("/")[0]]
        result.append(Type(media=URLInputFile(attachment.url)))
    await bot.send_media_group(chat_id, result)

dp.include_routers(
    add_discord_id.add_discord,
    start.start,
    admin.admin,
    button_callbacks.callbacks
    )