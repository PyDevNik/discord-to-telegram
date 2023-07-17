from ..messages import START_MESSAGE
from ....database.db import DB
from ..keyboards.start import start_keyboard
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

start = Router()
db = DB()

@start.message(Command(commands=["start"]))
async def start_command(msg: Message):
    code = msg.text.split(" ")[1]
    code = db.find_code(user_id=msg.from_user.id)
    if code:
        code.invites += 1
        await msg.answer(START_MESSAGE, reply_keyboard=start_keyboard)
        db.update_code(code)
