from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

print("Starting Cloud Upload Bot!")
bot = Client(
    "clouduploadbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="damanik"),
)

bot.run()
