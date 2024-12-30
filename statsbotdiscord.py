import hikari
import os
from dotenv import load_dotenv
import hikari.events.voice_events
import hikari.guilds
import datetime
from pymongo import MongoClient

# non ci serve più il dizionario

#user_times = {}
# carichiamo il .env file e otteniamo il token
load_dotenv()

token = os.getenv('TOKEN')

#URI DI mongodb

MONGO_URI = os.getenv('MONGO_URI')

# configurazione di mongodb creazione oggetto cliente
client = MongoClient(MONGO_URI)

# acesso al database e collezione
db = client["voice_bot_db"]
collection = db["user_times"] 



# abilitato l'intento guild in particola il cambio di stato vocale

bot = hikari.GatewayBot(token,intents=hikari.Intents.GUILD_VOICE_STATES | hikari.Intents.MESSAGE_CONTENT )

# implementare il numero di ore 



@bot.listen()
async def listener(event: hikari.events.voice_events.VoiceStateUpdateEvent) -> None:
    
    
    user_id = event.state.user_id
    now = datetime.datetime.now().replace(microsecond=0)

    
    if event.old_state is None:  # L'utente è entrato in un canale
        join_time = now
        # user_times[user_id] = {"join_time": join_time, "exit_time": None}
        collection.update_one(
            {"user_id" : user_id},
            {"$set": {"join_time": join_time, "exit_time" : None}},
            upsert=True
            
        )
        print(f"Utente {user_id} è entrato alle {join_time}.")
        
        

    elif event.state.channel_id is None:  # L'utente è uscito dal canale
        user_data = collection.find_one({"user_id": user_id})
        if user_data and "join_time" in user_data:
            exit_time = now
            join_time = user_data["join_time"]
            
            time_spent = exit_time - join_time
            collection.update_one(
                {"user_id": user_id},
                {"$set": {"exit_time": exit_time, "time_spent": str(time_spent)}}
            )            
             
            print(f"Utente {user_id} è uscito alle {exit_time}. Tempo trascorso: {time_spent}.")


# come passso un valore dentro una funzione fuori?
# se creo una classe tempo di utente con come attributi id_utente, ore_trascorse. e importando quella classe e ist

bot.run()
