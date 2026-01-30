import streamlit as st
import time
import random

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="WineArt Selector", page_icon="🍷", layout="centered")

# --- STILE CSS (Elegante stile WineArt) ---
st.markdown("""
    <style>
    .main { background-color: #f9f9f9; }
    .wine-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        border-left: 8px solid #800020;
        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
        margin-bottom: 25px;
    }
    .wine-price {
        color: #800020;
        font-size: 26px;
        font-weight: bold;
    }
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        height: 3.5em;
        background-color: #800020;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATABASE VINI (Esempio di 10 vini) ---
vini = [
    {
        "nome": "Amarone della Valpolicella",
        "cantina": "Bertani",
        "tipo": "Rosso",
        "corpo": "Molto Strutturato",
        "abbinamento": "Carne",
        "mood": "Regalo importante / Serata Speciale",
        "prezzo": "85.00€",
        "descr": "Note di amarena, cioccolato e spezie. Un gigante della tradizione.",
        "perche": "Perché la sua potenza regge i sapori forti e rende la serata indimenticabile."
    },
    {
        "nome": "Franciacorta Brut DOCG",
        "cantina": "Bellavista",
        "tipo": "Bollicine",
        "corpo": "Elegante e Fine",
        "abbinamento": "Aperitivo",
        "mood": "Serata romantica",
        "prezzo": "45.00€",
        "descr": "Perlage finissimo, note di crosta di pane e agrumi freschi.",
        "perche": "Le bollicine sono l'inizio perfetto per ogni grande storia."
    },
    {
        "nome": "Vermentino di Gallura",
        "cantina": "Sella & Mosca",
        "tipo": "Bianco",
        "corpo": "Fresco e Sapido",
        "abbinamento": "Pesce",
        "mood": "Cena con amici",
        "prezzo": "28.00€",
        "descr": "Profuma di macchia mediterranea e salsedine.",
        "perche": "È il compagno ideale per risate e piatti di mare freschi."
    },
    {
        "nome": "Gewürztraminer",
        "cantina": "Tramin",
        "tipo": "Bianco",
        "corpo": "Aromatico",
        "abbinamento": "Pesce",
        "mood": "Serata romantica",
        "prezzo": "32.00€",
        "descr": "Esplosione di litchi, rosa canina e spezie dolci.",
        "perche": "Il suo profumo intenso crea un'atmosfera magica e avvolgente."
    },
    {
        "nome": "Brunello di Montalcino",
        "cantina": "Biondi Santi",
        "tipo": "Rosso",
        "corpo": "Eterno ed Elegante",
        "abbinamento": "Carne",
        "mood": "Regalo importante / Serata Speciale",
        "prezzo": "95.00€",
        "descr": "Eleganza pura, tabacco, cuoio e frutti neri di bosco.",
        "perche": "Se vuoi fare un colpo da maestro, il Brunello è la tua risposta."
    },
    {
        "nome": "Moscato d'Asti DOCG",
        "cantina": "Vietti",
        "tipo": "Dolce",
        "corpo": "Leggero e Brioso",
        "abbinamento": "Dessert",
        "mood": "Cena con amici",
        "prezzo": "18.00€",
        "descr": "Dolcezza bilanciata da una freschezza incredibile, note di pesca.",
        "perche": "Per chiudere in dolcezza e leggerezza tra mille chiacchiere."
    }
]

# --- INTERFACCIA ---
st.title("🍷 WineArt Selector")
st.subheader("Trova la bottiglia ideale per il tuo momento")
st.write("---")

# STEP 1: Cosa mangi?
cibo = st.selectbox("Cosa c'è nel piatto?", ["Seleziona...", "Aperitivo", "Pesce", "Carne", "Dessert"])

# STEP 2: Il Mood
mood = st.selectbox("Che atmosfera cerchi?", ["Seleziona...", "Cena con amici", "Serata romantica", "Regalo importante / Serata Speciale"])

st.write("")

if st.button("TROVA IL VINO IDEALE 🍇"):
    if cibo == "Seleziona..." or mood == "Seleziona...":
        st.warning("Per favore, seleziona sia il cibo che il mood per aiutarmi a scegliere!")
    else:
        with st.spinner("Il sommelier sta scendendo in cantina..."):
            time.sleep(1.5)
            
        # Logica di filtro: cerchiamo i vini che corrispondono a entrambi
        scelte = [v for v in vini if v["abbinamento"] == cibo and v["mood"] == mood]
        
        # Se non c'è un match perfetto, cerchiamo solo per cibo
        if not scelte:
            scelte = [v for v in vini if v["abbinamento"] == cibo]
            
        if scelte:
            st.success(f"Ho trovato {len(scelte)} proposta/e perfetta/e per te:")
            for vino in scelte:
                st.markdown(f"""
                <div class="wine-card">
                    <small style="color: grey; text-transform: uppercase;">{vino['tipo']} • {vino['corpo']}</small>
                    <h1 style="color: #800020; margin-top: 5px;">{vino['nome']}</h1>
                    <p style="font-size: 18px; color: #333;"><b>Cantina:</b> {vino['cantina']}</p>
                    <p style="font-size: 16px;"><i>"{vino['descr']}"</i></p>
                    <div style="background-color: #f1f1f1; padding: 10px; border-radius: 5px; margin-top: 10px;">
                        <b>L'ESPERTO DICE:</b> {vino['perche']}
                    </div>
                    <div class="wine-price" style="margin-top: 15px;">{vino['prezzo']}</div>
                </div>
                """, unsafe_allow_html=True)
                st.write("")
        else:
            st.error("Purtroppo non ho un vino che corrisponde esattamente. Ma chiamami, in cantina ho sempre qualche tesoro nascosto!")

# CONTATTI FINALI
st.write("---")
st.caption("WineArt Selector - Tecnologia applicata al gusto.")
