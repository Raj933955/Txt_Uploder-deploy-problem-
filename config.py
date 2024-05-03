import os

API_ID = API_ID = 27952989

API_HASH = os.environ.get("API_HASH", "74f04808a359e9a516e955ec243613ca")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6821976502:AAEleXStH1ehZN0qnZJY3qafo57jAq4fg0U")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 585731991))

LOG = -1002047255106

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "585731991").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


