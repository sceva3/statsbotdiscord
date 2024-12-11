import hikari
import os
from dotenv import load_dotenv
import hikari.events.voice_events
import hikari.guilds
import datetime
# apro il json

# carichiamo il .env file e otteniamo il token
load_dotenv()

token = os.getenv('TOKEN')

# abilitato l'intento guild in particola il cambio di stato vocale

bot = hikari.GatewayBot(token,intents=hikari.Intents.GUILD_VOICE_STATES | hikari.Intents.MESSAGE_CONTENT )

@bot.listen()
async def listener(event: hikari.events.voice_events.VoiceStateUpdateEvent) -> None:
    
#  if event.old_state == None:
#    print(now.time())


bot.run()
