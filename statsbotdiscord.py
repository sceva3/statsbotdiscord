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

# implementare il numero di ore 



# class Utente():
#     def __init__(self, ore_trascorse, join_t,exit_t ) ->None:
#       self.ore_trascorse = ore_trascorse
#       self.join_t = join_t
#       self.exit_t = exit_t
#     def calcola_ore(self, join_t, exit_t):
#         self.join_t = join_t
#         self.exit_t = exit_t
#         print(join_t,exit_t)

# user_time = Utente(ore_trascorse=None, join_t=None, exit_t=None)

user_times = {}

@bot.listen()
async def listener(event: hikari.events.voice_events.VoiceStateUpdateEvent) -> None:
    
    
    user_id = event.state.user_id
    now = datetime.datetime.now().replace(microsecond=0)

    
    if event.old_state is None:  # L'utente è entrato in un canale
        join_time = now
        user_times[user_id] = {"join_time": join_time, "exit_time": None}
        print(f"Utente {user_id} è entrato alle {join_time}.")

    elif event.state.channel_id is None:  # L'utente è uscito dal canale
        if user_id in user_times and user_times[user_id]["join_time"] is not None:
            exit_time = now
            join_time = user_times[user_id]["join_time"]
            time_spent = exit_time - join_time

            user_times[user_id]["exit_time"] = exit_time
            print(f"Utente {user_id} è uscito alle {exit_time}. Tempo trascorso: {time_spent}.")

 

# come passso un valore dentro una funzione fuori?
# se creo una classe tempo di utente con come attributi id_utente, ore_trascorse. e importando quella classe e ist

bot.run()
