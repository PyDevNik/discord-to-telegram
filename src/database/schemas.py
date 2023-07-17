from pydantic import BaseModel
from typing import List
from aiogram.types.user import User as TgUser
from discord import TextChannel as DsChannel
from aiogram.types.chat import Chat as TgChannel

class User(BaseModel):
    tg_user: TgUser
    discord_channels: List[DsChannel]
    telegram_channels: List[TgChannel]
    ref_code: str = ""

class Code(BaseModel):
    user_id: int
    code: str
    invites: int