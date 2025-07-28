#(©)CodeXBotz
#By @Codeflix_Bots



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8353723670:AAG8zb5jbnKxhgdRqN4SFhNbOD27gHtC-RY")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "27693415"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8dc020d35ff99813b494f20955d8c724")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002558615397"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "27693415"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://jaheco5847:gqomHHqygEBUxbVk@cluster0.9iy9hhx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster01")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1002699079269"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "0"))
FORCESUB_CHANNEL3 = int(os.environ.get("FORCESUB_CHANNEL3", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#token varibles
# my shortner https://dashboard.shareus.io/signup/lifetime/U9AZbV

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "yummyurl.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "f4e1787c1041fd077f95c6a721901f51dfebf0f6")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 1500)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://t.me/bolomotu/1314")

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b><blockquote>◈ Adult : <a href=https://t.me/motumovies>Join Now</a>\n◈ Movies : <a href=https://t.me/motulinks>Join Now</a>\n◈ Mainn Channel : <a href=https://t.me/motumoviess>Join Now</a>\n</a>\n◈ How to Download: <a href=https://t.me/bolomotu/1314>Watch Now</a>\n</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/vipmotus>Vip Motu</a></blockquote></b>")
try:
    ADMINS=[27693415]
    for x in (os.environ.get("ADMINS", "27693415").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐒𝐨𝐫𝐫𝐲 {first} 𝐘𝐨𝐮 𝐧𝐞𝐞𝐝 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐢𝐧 𝐦𝐲 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞 \n\n 𝐊𝐢𝐧𝐝𝐥𝐲 𝐏𝐥𝐞𝐚𝐬𝐞 𝐣𝐨𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>» ʙʏ @MOTUMOVIESS</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!\n\n» ᴍʏ ᴏᴡɴᴇʀ : @wrrohit02"

ADMINS.append(OWNER_ID)
ADMINS.append(27693415)

LOG_FILE_NAME = "codeflixbots.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)




