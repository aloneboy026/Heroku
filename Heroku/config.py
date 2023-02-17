from os import getenv
from dotenv import load_dotenv

load_dotenv()

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "5791761493:AAGNMROvljLGlsZ2u-YSHlovelLYCu_j1HA")
BOT_NAME = getenv("BOT_NAME", "ᴍɪꜱꜱ ✘ ᴀɴɢᴇʟ")
BOT_USERNAME = getenv("BOT_USERNAME", "love_angelbot")
ASSID = int(getenv("ASSID", "6225126821"))
ASSNAME = getenv("ASSNAME", "miss angel")
ASSUSERNAME = getenv("ASSUSERNAME", "gethu_mass")
BOT_ID = int(getenv("BOT_ID", "5791761493"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Kittuthemeoe:kiranraj@cluster0.mv6oj.mongodb.net/?retryWrites=true&w=majority")
API_ID = int(getenv("API_ID", "10284859"))
API_HASH = getenv("API_HASH", "b0ad58eb8b845ba0003e0d9ce5fc2196")
OWNER_ID = int(getenv("OWNER_ID", "5613528193"))
UPDATE = getenv("UPDATE", "mondo_lover")
SUPPORT = getenv("SUPPORT", "team_comrade")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "9999"))
CMD_MUSIC = list(getenv("CMD_MUSIC", "/ !").split())
BG_IMG = getenv("BG_IMG", "https://telegra.ph/file/53112d2692ac8d0b499c0.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5613528193").split()))
START_PIC = getenv("START_PIC", "https://telegra.ph/file/8af51bc635611f4a009c5.jpg")
OWNER_USERNAME = getenv("OWNER_USERNAME", "t.me//matna_setha")
IMG_1 = "https://telegra.ph/file/202c8e5a57f1f8597fe2a.jpg"
