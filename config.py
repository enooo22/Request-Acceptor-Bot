from os import environ

API_ID = int(environ.get("API_ID", "25959542"))
API_HASH = environ.get("API_HASH", "814b705305b7ecaa628468c011ea16d1")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002569909548"))
ADMINS = int(environ.get("ADMINS", "8134543713"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://lavanya143111443:wJ4EhAF0jCUOm35Z@cluster0.llqwyeo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
