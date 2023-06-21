#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "16246834"
API_HASH = "29b3ffa9245c07f05375b92f38e8f13d"
BOT_TOKEN = "5716827359:AAE3NJPyZkXHATL8m3AmLVxFy0-NNhKOOog"
SESSION = "1AZWarzMBu0xf10AC1OqoqMFUU7IPmJ0cn-QVY3q0_vSybh5eOE4D2xP5SJMphleqWndRafbyuspSw1FWy57NpD1gdNlpyVheasBR-e-WtaBYGutWF496gmG2nj1kmeYjsWGY7qmvvXQfLiOgyc-A7UsvU_t3DlgKhzoIDNePpNKtDhrv8ctCMDbvYUj94YFCZ8_dQypteEj1fi3U7c1LGbT-yHlhngca0CiR2_wdJejAgsQ1V9cLi_fFLiFtkH3loOrqLrjgT-5jbMVtJemr_6cuhQZZEjXF1CepE9L-xuXrrKVpx0EVI_LEHsa9pNgP3N2jRueUDJ5madmE4D5kZexUIX5hl68="
FORCESUB = "executivebanget"
AUTH = 1715348447

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
