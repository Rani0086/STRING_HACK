# TEAM PURVI ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "27079591"
    API_HASH = "c81ae4c3dc026ea4bf49842a8ce4a5f9"
    #TOKEN = "7837097346:AAGmI0BfMnHjd9FzdZo6ovVTxjF4QnrQhTM"
    TOKEN = os.environ.get("TOKEN", None)
    MONGO_URL = "mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority"
    START_PIC = "https://envs.sh/jbP.png"
    SUDOERS = filters.user(["7526369190"])
