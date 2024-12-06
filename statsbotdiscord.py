import hikari
import os
from dotenv import load_dotenv
import hikari.events.voice_events

# apro il json

# carichiamo il .env file e otteniamo il token
load_dotenv()

token = os.getenv('TOKEN')

# abilitato l'intento guild in particola il cambio di stato vocale

bot = hikari.GatewayBot(token,intents=hikari.Intents.GUILD_VOICE_STATES | hikari.Intents.MESSAGE_CONTENT )

'''
@bot.listen()
async def ping(event: hikari.events.voice_events) -> None:

bot.run()
'''