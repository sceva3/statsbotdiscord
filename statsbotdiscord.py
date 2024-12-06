import hikari
import os
from dotenv import load_dotenv

# apro il json

# carichiamo il .env file e otteniamo il token
load_dotenv()

token = os.getenv('TOKEN')

bot = hikari.GatewayBot(token,intents=hikari.Intents.ALL_UNPRIVILEGED | hikari.Intents.MESSAGE_CONTENT )
# funzione di ascolto del bot con esecuzione della risposta al comando ping

