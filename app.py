import streamlit as st
import time

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_titleCreeremo una lista di vini dove ogni vino ha dei "tag" (etichette) che corrispondono alle risposte.

### 3. Codice Prototipo (Il Sommelier Digitale)

Copia questo codice="WineArt Selector", page_icon="🍷", layout="centered")

# --- STILE CSS (Elegante e scuro come una cantina) ---
st.markdown("""
    <style>
    .main { background- in un nuovo file (o sovrascrivi `app.py`) per vedere come funziona la logica:

```python
import streamlit as st
import time

# --- CONFIGURAZIONE ---
st.set_page_configcolor: #1a1a1a; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color:(page_title="Il Tuo Sommelier", page_icon="🍷")

# CSS per rendere la carta vini elegante #800020; color: white; border: none; }
    .wine-card { background-color: #262626; padding: 20px; border-radius: 15px (stile WineArt)
st.markdown("""
    <style>
    .wine-card {
        border: 1px solid #ddd;
        padding: 20px;
        border-radius: 10px;
        background-color: #fdfdfd;
        border-left: 5; border: 1px solid #4d0013; margin-top: 20px; }
    .price-tag { font-size: 24px; color: #ffcc00;px solid #800020; /* Color Borgogna */
        margin-bottom: 20px font-weight: bold; }
    .stSelectbox label { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# --- DATABASE VINI (Esempio di ;
    }
    .wine-price {
        color: #800020;
6 vini) ---
# Puoi aggiungere tutti quelli che vuoi seguendo questo schema
vini = [
    {
        "nome": "Amarone della Valpolicella",
        "tipo": "Rosso",
        "cor        font-size: 24px;
        font-weight: bold;
    }
    .stButton>button { border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- DATABASE VINI (Esempio con 10 vini) ---
# In un'app reale ne aggiungeremo molti di più
vini = [
    {
        "nome": "Franciacorta Brut DOCG",
        "cantina": "Bellavista",
        "tipo": "Bollicine",
po": "Strutturato",
        "abbinamento": "Carne",
        "mood": "Regalo importante / Serata Speciale",
        "prezzo": "55.00€",
        "descr": "Note di amarena, cioccolato e spezie. Un gigante della tradizione italiana.",
        "        "abbinamento": "Aperitivo",
        "occasione": "Brindisi tra amici",
        "prezzo": "45€",
        "descrizione": "Perlage fine e persistente. Note di croperche": "Perché la sua struttura regge piatti complessi e scalda il cuore."
    },
    {
        "nome": "Franciacorta Brut DOCG",
        "tipo": "Bollicinesta di pane e agrumi.",
        "corpo": "Leggero/Elegante"
    },
    {
        "nome": "Amarone della Valpolicella",
        "cantina": "",
        "corpo": "Elegante",
        "abbinamento": "Aperitivo",
        "mood": "Serata romantica",
        "prezzo": "38.00€",
        Bertani",
        "tipo": "Rosso",
        "abbinamento": "Carne Rossa",
        ""descr": "Perlage finissimo, note di crosta di pane e agrumi.",
        "peroccasione": "Occasione Speciale",
        "prezzo": "85€",
        "descrizione": "Grande struttura, note di prugna, marasca e spezie dolci.",
        "corpo":che": "Le bollicine sono l'inizio perfetto per ogni storia d'amore."
    },
    {
        "nome": "Vermentino di Gallura",
        "tipo": "Bianco",
        "corpo": "Fresco",
        "abbinamento": "Pesce",
        "mood": "Cena con amici",
        "prezzo": "22.00€",
        "descr": "Sapido, "Molto Strutturato"
    },
    {
        "nome": "Vermentino di Gallura",
        "cantina": "Sella & Mosca",
        "tipo": "Bianco",
        "abbinamento": "Pesce",
        "occasione": "Serata tra amici",
        " minerale, con richiami di macchia mediterranea.",
        "perche": "È il compagno idealeprezzo": "28€",
        "descrizione": "Fresco, sapido con sentori di macchia mediterranea.",
        "corpo": "Fresco/Minerale"
    }
]

# --- INTER per risate e piatti di mare freschi."
    },
    {
        "nome": "Gewürztraminer",
        "tipo": "Bianco",
        "corpo": "Aromatico",
        "abFACCIA ---
st.title("🍷 Il Tuo Sommelier Digitale")
st.write("Rispondi a 3 domande e troverò la bottiglia ideale dalla nostra carta.")

st.divider()

# DOMbinamento": "Pesce",
        "mood": "Serata romantica",
        "prezzo": "28.00€",
        "descr": "Esplosione di litchi, rosa canina e speANDA 1
cibo = st.selectbox("Cosa mangerai?", ["Scegli...", "Aperitivozie dolci.",
        "perche": "Il suo profumo incanterebbe chiunque."
    },
    {
        "nome": "Brunello di Montalcino",
        "tipo": "Rosso",
", "Pesce", "Carne Rossa", "Pizza/Pasta"])

# DOMANDA 2
serata = st.        "corpo": "Eterno",
        "abbinamento": "Carne",
        "selectbox("Che tipo di serata è?", ["Scegli...", "Brindisi tra amici", "Cena romantica",mood": "Regalo importante",
        "prezzo": "75.00€",
        "descr": " "Occasione Speciale"])

# FILTRO LOGICO
if cibo != "Scegli..." and serataEleganza pura, tabacco, cuoio e frutti neri.",
        "perche": "Se vuoi fare != "Scegli...":
    st.write("---")
    with st.spinner("Consultando la cant colpo, il Brunello è una garanzia assoluta."
    },
    {
        "nome": "Mina..."):
        time.sleep(1)
    
    # Cerchiamo i vini che corrispondono (oscato d'Asti",
        "tipo": "Dolce",
        "corpo": "Leggero",Logica di filtro)
    risultati = [v for v in vini if v["abbinamento"] ==
        "abbinamento": "Dessert",
        "mood": "Cena con amici",
         cibo or v["occasione"] == serata]
    
    if risultati:
        st.subheader(f"Ho"prezzo": "18.00€",
        "descr": "Dolce ma fresco, con arom trovato {len(risultati)} proposte per te:")
        
        for vino in risultati:
            sti di pesca e salvia.",
        "perche": "Per chiudere in dolcezza senza appesantire.".markdown(f"""
                <div class="wine-card">
                    <small>{vino['tipo']}
    }
]

# --- INTERFACCIA ---
st.title("🍷 WineArt Selector")
st - {vino['cantina']}</small>
                    <h3>{vino['nome']}</h3>
                    <p><i>{vino['descrizione']}</i></p>
                    <p><b>Corpo:</b> {vino['cor.subheader("Trova la bottiglia perfetta per il tuo momento")
st.divider()

# STEP 1: Cosapo']}</p>
                    <div class="wine-price">{vino['prezzo']}</div>
                </div>
             mangi?
cibo = st.selectbox("Cosa c'è nel piatto?", ["Scegli...",""", unsafe_allow_html=True)
            if st.button(f"Scegli {vino['nome'] "Aperitivo", "Pesce", "Carne", "Dessert"])

# STEP 2: Il Mood
mood = st.selectbox("Che atmosfera cerchi?", ["Scegli...", "Cena con amici", "Serata}", key=vino['nome']):
                st.success(f"Ottima scelta! Il cameriere arriver romantica", "Regalo importante / Serata Speciale"])

st.write("")
if st.button("TROVA ILà subito con il tuo {vino['nome']}.")
    else:
        st.warning("Nessun vino corris VINO IDEALE 🍇"):
    if cibo == "Scegli..." or mood == "Scegli...":ponde esattamente, ma ecco un jolly che sta bene su tutto!")
        # Qui potresti mettere un vino "standard
        st.warning("Per favore, seleziona sia il cibo che il mood!")
    else:
        "
