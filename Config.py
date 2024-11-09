import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "24665539"))
    API_HASH = os.environ.get("API_HASH", "e73183cee6cbcfcdea8901f7680ff0f9")
    BOT_TOKEN = os.environ.get("8015587250:AAHp99ktS-ubfTACFvdfbUcLaj3llKWTN5w", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "@B_W_EE")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
