from aiogram.types import InputMediaPhoto, InputMediaVideo, InputMediaAudio, InputMediaAnimation, InputMediaDocument

# Bots
DISCORD_TOKEN = ""
TELEGRAM_TOKEN = ""

# Database
DATABASE_URL = ""
DATABASE_NAME = ""

# Collections
USERS = "USERS"
CODES = "CODES"

# Helpers
CONTENT_TYPES = {
    'image': InputMediaPhoto,
    'video': InputMediaVideo,
    'audio': InputMediaAudio,
    'animation': InputMediaAnimation,
    'document': InputMediaDocument
}


# Admin
ADMINS = []