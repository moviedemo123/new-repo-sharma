import re, sys, logging
from os import environ

logging.basicConfig(level=logging.ERROR)

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Auto_Filters_Bot')
API_ID = environ.get('API_ID', '')
if len(API_ID) == 0:
    logging.error('API_ID is missing, exiting now')
    exit()
else:
    API_ID = int(API_ID)
API_HASH = environ.get('API_HASH', '')
if len(API_HASH) == 0:
    logging.error('API_HASH is missing, exiting now')
    exit()
BOT_TOKEN = environ.get('BOT_TOKEN', '')
if len(BOT_TOKEN) == 0:
    logging.error('BOT_TOKEN is missing, exiting now')
    exit()
PORT = int(environ.get('PORT', '8080'))

# Bot pics and stickers
STICKERS = (environ.get('STICKERS', 'CAACAgIAAxkBAAEGm9hjhf69CtQmXoeQ2HidYCGBFeZ4gAACxgEAAhZCawpKI9T0ydt5RysE CAACAgIAAxkBAAEGm9pjhf7I9jCDh3PpkocMNFcPJfisvwAC0wADVp29CvUyj5fVEvk9KwQ CAACAgIAAxkBAAEGm9xjhf7SH4Yc8EP5yI4e8BTH968ClwACGAADDbbSGX671giQDJU8KwQ')).split()
PICS = (environ.get('PICS', 'https://telegra.ph/file/58fef5cb458d5b29b0186.jpg https://telegra.ph/file/f0aa4f433132769f8970c.jpg https://telegra.ph/file/f515fbc2084592eca60a5.jpg https://telegra.ph/file/20dbdcffaa89bd3d09a74.jpg https://telegra.ph/file/6045ba953af4def846238.jpg')).split()

# Bot Admins
ADMINS = environ.get('ADMINS', '')
if len(ADMINS) == 0:
    logging.error('ADMINS is missing, exiting now')
    exit()
else:
    ADMINS = [int(admins) if id_pattern.search(admins) else admins for admins in ADMINS.split()]

# Channels
INDEX_CHANNELS = [int(index_channels) if id_pattern.search(index_channels) else index_channels for index_channels in environ.get('INDEX_CHANNELS', '').split()]
AUTH_CHANNEL = [int(auth_channels) if id_pattern.search(auth_channels) else auth_channels for auth_channels in environ.get('AUTH_CHANNEL', '').split()]
LOG_CHANNEL = environ.get('LOG_CHANNEL', '')
if len(LOG_CHANNEL) == 0:
    logging.error('LOG_CHANNEL is missing, exiting now')
    exit()
else:
    LOG_CHANNEL = int(LOG_CHANNEL)

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "")
if len(DATABASE_URL) == 0:
    logging.error('DATABASE_URL is missing, exiting now')
    exit()
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/SL_Bots_Support')
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/SL_Bots_Updates')

# Bot settings
AUTO_FILTER = is_enabled((environ.get('AUTO_FILTER', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SPELL_CHECK = is_enabled(environ.get("SPELL_CHECK", "True"), True)
SHORTLINK = is_enabled((environ.get('SHORTLINK', "True")), True)
DELETE_TIME = int(environ.get('DELETE_TIME', 3600))
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "False")), False)
WELCOME = is_enabled((environ.get('WELCOME', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
LINK_MODE = is_enabled(environ.get("LINK_MODE", "True"), True)
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))

# Other
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "✅ I Found: <code>{query}</code>\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating} / 10</a>\n☀️ Languages: {languages}\n📀 RunTime: {runtime} Minutes\n\n🗣 Requested by: {message.from_user.mention}\n©️ Powered by: <b>{message.chat.title}</b>")
FILE_CAPTION = environ.get("FILE_CAPTION", "<i>{file_name}</i>\n\nᴘʟᴇᴀsᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ᴄʟᴏsᴇ ʙᴜᴛᴛᴏɴ ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ sᴇᴇɴ ᴛʜᴇ ᴍᴏᴠɪᴇ")
SHORTLINK_URL = environ.get("SHORTLINK_URL", "mdiskshortner.link")
SHORTLINK_API = environ.get("SHORTLINK_API", "36f1ae74ba1aa01e5bd73bdd0bc22aa915443501")
WELCOME_TEXT = environ.get("WELCOME_TEXT", "Hello {mention}, Welcome to {title} group!")
TUTORIAL = environ.get("TUTORIAL", "https://t.me/SL_Bots_Updates")

# stream features vars
"""Deploy this repo: https://github.com/adarsh-goel/filestreambot"""
BIN_CHANNEL = environ.get("BIN_CHANNEL", "")
if len(BIN_CHANNEL) == 0:
    logging.error('BIN_CHANNEL is missing, exiting now')
    exit()
else:
    BIN_CHANNEL = int(BIN_CHANNEL)
URL = environ.get("URL", "")
if len(URL) == 0:
    logging.error('URL is missing, exiting now')
    exit()
else:
    if URL.startswith(('https://', 'http://')):
        if not URL.endswith("/"):
            URL += '/'
    else:
        logging.error('URL is not valid, exiting now')
        exit()
