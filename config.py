## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgCKvodu-gwwjmf95L-cjdNw3hLO9CHwKIbt-2U8GWUcCQ1ej4InbsgzsdQlQDIZy2pOIidkAYjMBjj2gmnGCbmDRNBrQAv5vobVtUIHVRfjdEMSNO-Yl9pcfdHJbGe4slix6yxSWX7BoyKOGTp3Fjzyrkd2BmQVFLCsQFU4dmfy_5QpL1W1LvyTetknVwBfljcYeZ_MmBanI1Ci3AIsSr-kP3B-7_m3XQVi0JnPiWGNTp71bHrJrnWCJvv15tyUUW0x4qFnIC-QIyPWKIr-NeHyYrcDxnsOBlNoURjPufBsGxe0dYugmHqd1VSbR1sfWOG6V7XsphPu99akJhFkkY_6AAAAAUBCpW4A")
BOT_TOKEN = getenv("BOT_TOKEN", "5357061878:AAExakkRjzYUvpoDjucX4AD2D71bwzC0yjM")
BOT_NAME = getenv("BOT_NAME", "𝑩𝑶𝑻 𝑴𝑼𝒁𝑰𝑪 𝑨𝑩𝑫𝑶 ‌ਊ")
API_ID = int(getenv("API_ID", "15713957"))
API_HASH = getenv("API_HASH", "0dfbddc3353bb68fc559545d21b9d83b")
OWNER_NAME = getenv("OWNER_NAME", "abdo")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Xx_ABDO2_Xx")
ALIVE_NAME = getenv("ALIVE_NAME", "abdo")
BOT_USERNAME = getenv("BOT_USERNAME", "musicb21_bot")
OWNER_ID = getenv("OWNER_ID", "1155106507")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Xx_abdo_muzic_xX")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "C_O_C_Q")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Xx_A_BDO_Xx")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1155106507").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
