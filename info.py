from os import environ

API_ID = environ.get("API_ID", "12380656")
API_HASH = environ.get("API_HASH", "d927c13beaaf5110f25c505b7c071273")
BOT_TOKEN = environ.get("BOT_TOKEN", "7328112987:AAE-m8fhi09-5GtdiSI0Lii8Qvpkg7Snnfs")
BOT_NAME = environ.get("BOT_NAME", "AV_GPT_BOT")
ADMIN = int(environ.get("ADMIN", "5977931010"))
CHAT_GROUP = int(environ.get("CHAT_GROUP", "-1002028053413"))
ADMIN_NAME = environ.get("ADMIN_NAME", "BOT_OWNER26")
LOG_CHANNEL = environ.get("LOG_CHANNEL", "-1002110971750")
MONGO_URL = environ.get("MONGO_URL", "mongodb+srv://aman991932:aman@cluster0.qp6vfyg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
AUTH_CHANNEL = int(
    environ.get("AUTH_CHANNEL", "-1002012150170")
)  # add your channel id for force subscribe
FSUB = environ.get("FSUB", True)
STICKERS_IDS = (
    "CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME"
).split()
COOL_TIMER = 20  # keep this atleast 20
ONLY_SCAN_IN_GRP = environ.get(
    "ONLY_SCAN_IN_GRP", True
)  # If IMG_SCAN_IN_GRP is set to True, image scanning is restricted to your support group only. If it's False, the image scanning feature can be used anywhere.
REACTIONS = ["❤️‍🔥", "⚡", "🔥"]
