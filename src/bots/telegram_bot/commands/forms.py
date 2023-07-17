from aiogram.fsm.state import State, StatesGroup

class AddDiscordID(StatesGroup):
    discord_id = State()
    telegram_id = State()

class EditDB(StatesGroup):
    file = State()