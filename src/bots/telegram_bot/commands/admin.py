from ..messages import ADMIN_PANEL
from ..keyboards.admin import admin_keyboard
from ....config import ADMINS
from aiogram import Router
from ...telegram_bot.bot import bot
from .forms import EditDB
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from ....database.db import DB
import pandas as pd

admin = Router()
db = DB()

@admin.message(Command(commands=["admin"]))
async def admin_comand(msg: Message):
    if msg.from_user.id in ADMINS:
        await msg.answer(ADMIN_PANEL, reply_keyboard=admin_keyboard)

@admin.message(EditDB.file)
async def edit_db(msg: Message, state: FSMContext):
    await state.clear()
    if msg.document.file_name.startswith("collection_"):
        await bot.download(msg.document.file_id)
        index = msg.document.file_name.split("_")[1]
        if index == 1: db.update_users(pd.read_excel(msg.document.file_name).to_dict(orient="records"))
        elif index == 2: db.update_codes(pd.read_excel(msg.document.file_name).to_dict(orient="records"))
        await msg.answer("Готово!")