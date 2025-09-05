import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Bot Configuration
API_ID = os.environ.get("API_ID", "21157244")
API_HASH = os.environ.get("API_HASH", "6c1eee32be959812f0598919209a2105")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
CHANNEL_ID = os.environ.get("CHANNEL_ID", "-1002887045646")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002887045646"))

# MongoDB Configuration
DATABASE_URL = os.environ.get("DATABASE_URL", "Mongo -- mongodb+srv://takkishor9784:gG73juoh44MnvJEZ@cluster0.q8hxdk2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "takkishor9784")
COLLECTION_NAME = os.environ.get("COLLECTION_NAME", "tests")
ADMIN_ID = os.environ.get("ADMIN_ID", "1783306092")

# Flask Configuration
FLASK_URLS = [
    os.environ.get("PRIMARY_URL", "http://localhost:5000"),
    os.environ.get("SECONDARY_URL", ""),  # Secondary URL from env
    os.environ.get("BACKUP_URL", "")  # Backup URL from env
]

# Remove empty URLs
FLASK_URLS = [url for url in FLASK_URLS if url]

# Feature Flags
USE_FLASK_APP = os.environ.get("USE_FLASK_APP", "True").lower() == "true"
FORCE_DIRECT_SEND = os.environ.get("FORCE_DIRECT_SEND", "False").lower() == "true"

# Messages 
WELCOME_MSG = """
𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 Ganesh 𝐓𝐞𝐬𝐭 𝐒𝐞𝐫𝐢𝐞𝐬 𝐁𝐨𝐭! 🎯

ɪ ᴄᴀɴ ᴇxᴛʀᴀᴄᴛ ᴛᴇꜱᴛ ꜱᴇʀɪᴇꜱ ꜰʀᴏᴍ ᴀɴʏ ᴀᴘᴘx ᴀᴘᴘʟɪᴄᴀᴛɪᴏɴ.
ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴍᴇ ᴛʜᴇ ᴀᴘᴘ ɴᴀᴍᴇ ᴏʀ ᴡᴇʙꜱɪᴛᴇ ᴜʀʟ!

𝙃𝙤𝙬 𝙩𝙤 𝙪𝙨𝙚:
1. ꜱᴇɴᴅ ᴀᴘᴘ ɴᴀᴍᴇ (ᴇ.ɢ. "parmaracademy")
2. ᴏʀ ꜱᴇɴᴅ ᴡᴇʙꜱɪᴛᴇ ᴜʀʟ / ᴀᴘɪ ᴜʀʟ
3. ꜱᴇʟᴇᴄᴛ ᴛᴇꜱᴛ ꜱᴇʀɪᴇꜱ
4. ɢᴇᴛ ʏᴏᴜʀ ᴛᴇꜱᴛ!
"""

FORCE_SUB_MSG = """
⚠️ 𝐏𝐥𝐞𝐚𝐬𝐞 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥

ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴛʜᴇ ʙᴏᴛ.
ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ᴊᴏɪɴ!

𝘼𝙛𝙩𝙚𝙧 𝙟𝙤𝙞𝙣𝙞𝙣𝙜, 𝙘𝙡𝙞𝙘𝙠 '𝙍𝙚𝙛𝙧𝙚𝙨𝙝' 𝙗𝙪𝙩𝙩𝙤𝙣.

""" 

