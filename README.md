# statsbotdiscord
# Bot per il Monitoraggio della Community con Dashboard

## Descrizione del Progetto

### Definizione
Questo progetto mira a fornire un bot per server Discord che consente ai gestori di community di monitorare e analizzare le metriche principali relative ai membri e alle attività del server.

### Problema che Risolve
Permette ai gestori di tenere traccia delle metriche più rilevanti, come la presenza, le interazioni e le attività degli utenti, fornendo statistiche dettagliate per una gestione più efficace della community.

## Funzionalità

### Metriche
- **Presenza**: Numero di ore medie che un membro passa nel server e nei vari canali (distribuzione delle presenze tramite grafici).
- **Interazioni**:
  - Numero di messaggi inviati da un membro nei diversi canali (distribuzione).
  - Attività prevalente di ciascun membro.
  - Condivisioni effettuate.
- **Eventi**:
  - Numero di eventi a cui partecipa un membro.
- **Ruoli**:
  - Statistiche sui ruoli più scelti nel server.
- **Membri**:
  - Numero totale di membri.
  - Percentuale di membri online rispetto al totale.
  - Statistiche su utenti bannati, kickati e in timeout con motivazioni.

## Interfaccia Utente
Gli utenti interagiranno con il bot tramite comandi su Discord.

## Dati Necessari
- **Numero di ore medie**:
  - Formula: `Totale di tempo trascorso dai membri / Numero totale di membri`.
- **Messaggi**:
  - Definizione: Stringa con almeno 5 caratteri, contenente una parola valida in italiano, priva di simboli o numeri.
  - Formula: `Somma dei messaggi inviati per ogni canale del server`.
- **Attività prevalente**:
  - Determinata dall'attività più frequente.
- **Statistiche dei ruoli**:
  - Somma delle reazioni relative ai ruoli.
- **Membri**:
  - Numero totale: Somma dei membri con il ruolo "membro".
  - Percentuale online: `Numero di membri online / Numero totale di membri * 100`.
- **Utenti bannati, kickati e in timeout**:
  - Somma dei rispettivi valori.

## Esempio di Funzionamento
Esempio di comando:
```
/hours
```
Risultato: Il bot restituisce il numero di ore medie trascorse dai membri nel server.

## Use Case
Un gestore vuole sapere quante ore medie i membri trascorrono nel server o quale attività viene svolta maggiormente da un determinato utente. Utilizza i comandi dedicati per ottenere questi dati in tempo reale.

## Comandi del Software

### Presenza
- `/hours [nome_utente] [id_channel] [avg] [-s]`
  - `nome_utente`: Tag utente.
  - `id_channel`: Canale di riferimento.
  - `avg`: Ore medie di presenza nel canale.
  - `-s`: Statistiche per tutti i membri del server o un canale specifico.

### Messaggi
- `/msg [nome_utente] [id_channel] [-s]`
  - `nome_utente`: Tag utente.
  - `id_channel`: Canale di riferimento.
  - `-s`: Numero totale di messaggi nel server o in un canale specifico.

### Attività
- `/act [nome_utente] [-s]`
  - `nome_utente`: Tag utente.
  - `-s`: Statistiche sull'attività prevalente di un utente o del server.

### Giochi
- `/games [nome_utente] [id_channel] [-s]`
  - `nome_utente`: Tag utente.
  - `id_channel`: Canale di riferimento.
  - `-s`: Gioco più svolto da un utente o nel server.

### Eventi
- `/events [nome_utente] [-s]`
  - `nome_utente`: Tag utente.
  - `-s`: Numero totale di eventi a cui hanno partecipato i membri del server.

### Ruoli
- `/rsts [-s]`
  - `-s`: Restituisce i ruoli più scelti nel server.

### Membri
- `/mbs [on] [off] [s]`
  - Restituisce il numero totale di membri e la percentuale di membri online/offline.

### Utenti Bannati, Kickati e in Timeout
- `/usr [bn] [kk] [to] [s]`
  - Restituisce statistiche sugli utenti bannati, kickati e in timeout.

## Compito del Progetto
Scrivere un programma in Python che:
1. Legge i dati da un file generato dal comando `git log`.
2. Analizza e fa il parsing del contenuto.
3. Restituisce le modifiche effettuate per ogni push del progetto.

### Requisiti
- Utilizzo di Python senza strumenti di intelligenza artificiale.
- Lettura e parsing del file `git log` per estrarre i dati rilevanti.

