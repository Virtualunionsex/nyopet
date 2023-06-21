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
SESSION = "AQAueOqsHHAEjSzuEg1g-DRFxsy441-lBw-9VUAOqF_BJ9TJzQXi38TmS35rRwRojXI8EsG0eAujf_-6rrVT1Na2qVcN93iulGpoJtyWO_CKWyUvsYDaC7v41Z4PYqZSnyhS3Hsd7R0CRhLtya1IwtEP4NZHKAp2zJebIYuV3foyn72liUr3tphhTfWA2HeQ2P29SwqKYphd8qB-nBujxuZUMEj7p6j-Lsm_ckLjvRCCcpdXy15ReqkmuYDSLGQO6nx2DaT4oWPB_ayrnZBESnjtn3J4tWEOt-I02SbWoNEZKvyVuLBpv3drB24RmQs_3JKIDPcgQkdXsgFFW11bvu8VZj4j3wA"
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
