# Don't Remove Credit Tg - @herokutech
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@herokutech
# Ask Doubt on telegram @OwnerRocky

from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "19609344"))
    API_HASH = environ.get("API_HASH", "31dfde0883ca3a155b5cfa880646d98f")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "vjbot") 
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://ankitraj3554:nL7rmRGVKKB5U6Bd@cluster0.fepjc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "vj-forward-bot")
    BOT_OWNER = int(environ.get("BOT_OWNER", "5568102372"))

# # Don't Remove Credit Tg - @herokutech
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@herokutech
# Ask Doubt on telegram @OwnerRocky

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []

# Don't Remove Credit Tg - @herokutech
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@herokutech
# Ask Doubt on telegram @OwnerRocky
