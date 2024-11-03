from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

class Config(object):
    # required config variables
    API_HASH = getenv("38d104adbd94c66a349714abd7977d80", None)                # get from my.telegram.org
    API_ID = int(getenv("29727048", 0))                  # get from my.telegram.org
    BOT_TOKEN = getenv("7605039383:AAE1mgOumbsRbJo6OYP2GUxTOCmZS68-qYs", None)              # get from @BotFather
    DATABASE_URL = getenv("mongodb+srv://ms7371091:ms7371091@cluster0.vwfw6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)        # from https://cloud.mongodb.com/
    HELLBOT_SESSION = getenv("BQHFmUgAwzDySLMT945VnCI5m4fJ5DB2-sAkRvg29RnLJNlEdTFbIEMj-ESSCHLRhhFxdPyxrjg2InxIWALUvKm290fPmSQ9Z2T73QxgLcoa_2BQy1mgzkX5kSPNNFtg5ybRFXC5Ya07TXSGYRqlhFzPL_hzZ3WSh44RO7iM-6ZoXoO5XXQz2ngUjAl0ipt64ywZDHOUQI3kR7Frk2lAfk-KAMLJS9ggog4efXDyIRvOHe_0ImDmWWKPTE_4RQOl3736lQRzG0aiv4bIPuF3a8Vi0xeqN8oIMBFJQfzbevVvmqmgNuRyXKO1QK3aKnF_NXGtyYjupXqHKX9L0TrFIC-AW3repgAAAAGd2xVtAA", None)  # enter your session string here
    LOGGER_ID = int(getenv("-1002467044807", 0))            # make a channel and get its ID
    OWNER_ID = getenv("6943348077", "")                  # enter your id here

    # optional config variables
    BLACK_IMG = getenv("BLACK_IMG", "https://telegra.ph/file/2c546060b20dfd7c1ff2d.jpg")        # black image for progress
    BOT_NAME = getenv("BOT_NAME", "\x40\x4d\x75\x73\x69\x63\x5f\x48\x65\x6c\x6c\x42\x6f\x74")   # dont put fancy texts here.
    BOT_PIC = getenv("BOT_PIC", "https://te.legra.ph/file/5d5642103804ae180e40b.jpg")           # put direct link to image here
    LEADERBOARD_TIME = getenv("LEADERBOARD_TIME", "3:00")   # time in 24hr format for leaderboard broadcast
    LYRICS_API = getenv("LYRICS_API", None)             # from https://docs.genius.com/
    MAX_FAVORITES = int(getenv("MAX_FAVORITES", 30))    # max number of favorite tracks
    PLAY_LIMIT = int(getenv("PLAY_LIMIT", 0))           # time in minutes. 0 for no limit
    PRIVATE_MODE = getenv("PRIVATE_MODE", "off")        # "on" or "off" to enable/disable private mode
    SONG_LIMIT = int(getenv("SONG_LIMIT", 0))           # time in minutes. 0 for no limit
    TELEGRAM_IMG = getenv("TELEGRAM_IMG", None)         # put direct link to image here
    TG_AUDIO_SIZE_LIMIT = int(getenv("TG_AUDIO_SIZE_LIMIT", 104857600))     # size in bytes. 0 for no limit
    TG_VIDEO_SIZE_LIMIT = int(getenv("TG_VIDEO_SIZE_LIMIT", 1073741824))    # size in bytes. 0 for no limit
    TZ = getenv("TZ", "Asia/Kolkata")   # https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

    # do not edit these variables
    BANNED_USERS = filters.user()
    CACHE = {}
    CACHE_DIR = "./cache/"
    DELETE_DICT = {}
    DWL_DIR = "./downloads/"
    GOD_USERS = filters.user()
    PLAYER_CACHE = {}
    QUEUE_CACHE =  {}
    SONG_CACHE = {}
    SUDO_USERS = filters.user()


# get all config variables in a list
all_vars = [i for i in Config.__dict__.keys() if not i.startswith("__")]
