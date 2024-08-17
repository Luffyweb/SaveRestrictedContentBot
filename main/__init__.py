#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 29452145
API_HASH = 5a2784e571fe5043852d32396a34a13b
BOT_TOKEN = 6340500779:AAGJcz-AorhwZnDKGZI84ehcoiM1LI0LxSE
SESSION = BQHBZ3EAKuTw7gsiKOjyd7m5B_9ZCnwDbCgFfrkemGudO43TMbo5PYNpMlTRuJ9js_CV5LuXgZvhrqLkrvqjGro9yKG2dwUtcRXxjsyXhvYpH0KNWqKMoCTRVoaqxac8eq9kZJrMxkwEabkCPcWPi-qVtp52V9hBul8D8SV1Zgj0rHTYoJFh_ZQAXbYvWaYmSWYe8IX4oafWP2WwK-MThTbioDyThRsQysVj2nSSFKTMaVyv2IihKm1XGtSu27hcxVE8EHbqxGGUatPDLaTq4CV9ydf68cnWFXOiFPH7BfThZxjfJJyEu2rpsCThaG16VqeVIjvufanXGbaHBUldW4g99WJhbgAAAAGGD3onAA
FORCESUB = Luffywebbd
AUTH = 6544128551

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

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
