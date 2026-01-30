import streamlit as st
import time
import random

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="WineArt Selector", page_icon="🍷", layout="centered")

# --- 2. STILE CSS ---
st.markdown("""
    <style>
    .main { background-color: #f4f4f4; }
    .wine-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        border-left: 10px solid #800020;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
        margin-bottom: 25px;
    }
    .wine-price { color: #800020; font-size: 26px; font-weight: bold; margin-top: 10px; }
    .stButton>button { width: 100%; border-radius: 25px; height: 3.5em; background-color: #800020; color: white; font-weight: bold; border: none; }
    /* Stile per il link della scheda */
    .stLinkButton>a { width: 100% !important; border-radius: 20px !important; text-align: center !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DATABASE VINI (Con link alla carta) ---
vini = [
    # BOLLICINE
    {
        "nome": "Champagne Vintage 2013", "cantina": "Dom Pérignon", "tipo": "Bollicine",
        "corpo": "Robusto", "stile": "Minerale", "abbinamento": "Pesce", "mood": "Occasione Speciale",
        "prezzo": "280.00€", "descr": "Un'icona di equilibrio e complessità.",
        "perche": "Il massimo prestigio per celebrare un accordo storico.",
        "link": "https://www.cartavinidigitale.it/menu-digitale-wineart/" # Sostituisci con link specifico
    },
    {
        "nome": "Franciacorta Cuveé Prestige", "cantina": "Ca' del Bosco", "tipo": "Bollicine",
        "corpo": "Leggero", "stile": "Secco", "abbinamento": "Aperitivo", "mood": "Incontro di lavoro",
        "prezzo": "45.00€", "descr": "Equilibrato, fresco e piacevolmente acido.",
        "perche": "Elegante e professionale, ideale per un aperitivo di business.",
        "link": "https://www.cartavinidigitale.it/menu-digitale-wineart/"
    },
    # BIANCHI
    {
        "nome": "Greco di Tufo Giallo d'Arles", "cantina": "Quintodecimo", "tipo": "Bianco",
        "corpo": "Di Medio Corpo", "stile": "Minerale", "abbinamento": "Pesce", "mood": "Incontro di lavoro",
        "prezzo": "55.00€", "descr": "Giallo oro, sentori di albicocca e note minerali.",
        "perche": "Un bianco autorevole che dimostra competenza e buon gusto.",
        "link": "https://www.cartavinidigitale.it/menu-digitale-wineart/"
    },
    {
        "nome": "Pinot Grigio", "cantina": "Jermann", "tipo": "Bianco",
        "corpo": "Leggero", "stile": "Secco", "abbinamento": "Pesce", "mood": "Incontro di lavoro",
        "prezzo": "35.00€", "descr": "Intenso, persistente, con un corpo eccezionale.",
        "perche": "Un classico intramontabile per un business lunch di alto livello.",
        "link": "https://www.cartavinidigitale.it/menu-digitale-wineart/"
    },
    # ROSSI
    {
        "nome": "Sassicaia 2020", "cantina": "Tenuta San Guido", "tipo": "Rosso",
        "corpo": "Robusto", "stile": "Secco", "abbinamento": "Carne", "mood": "Occasione Speciale",
        "prezzo": "350.00€", "descr": "Maestoso, note di piccoli frutti rossi.",
        "perche": "Quando il tavolo delle trattative richiede il peso massimo dell'enologia.",
        "link": "https://www.cartavinidigitale.it/menu-digitale-wineart/"
    },
    {
        "nome": "Brunello di Montalcino", "cantina": "Casanova di Neri", "tipo": "Rosso",
        "corpo": "Di Medio Corpo", "stile": "Secco", "abbinamento": "Carne", "mood": "Incontro di lavoro",
        "prezzo": "70.00€", "descr": "Grande bevibilità, ciliegia e sottobosco.",
        "perche": "Un rosso di classe che accompagna la conversazione senza sovrastarla.",
        "link": "www.cartavinidigitale.it/menu-digitale-wineart/#1745654818035-20641e56-b023"
    }
]

# --- 4. INTERFACCIA ---
st.title("🍷 WineArt Selector")

# Tasto per tornare alla carta principale
st.link_button("⬅️ TORNA ALLA CARTA VINI", "https://www.cartavinidigitale.it/menu-digitale-wineart/")

st.write("")
st.subheader("Il consulente digitale per la tua scelta in cantina")
st.divider()

col1, col2 = st.columns(2)
with col1:
    cibo = st.selectbox("1. Cosa c'è nel piatto?", ["Scegli...", "Aperitivo", "Pesce", "Carne"])
    corpo = st.selectbox("3. Struttura del vino?", ["Scegli...", "Leggero", "Di Medio Corpo", "Robusto"])

with col2:
    mood = st.selectbox("2. Che atmosfera cerchi?", ["Scegli...", "Cena con amici", "Incontro di lavoro", "Occasione Speciale"])
    stile = st.selectbox("4. Carattere preferito?", ["Scegli...", "Secco", "Fruttato", "Aromatico", "Minerale"])

st.write("")

# --- 5. LOGICA ---
if st.button("INTERROGA IL SOMMELIER 🍇"):
    if cibo == "Scegli..." or mood == "Scegli...":
        st.warning("Seleziona almeno Cibo e Atmosfera!")
    else:
        with st.spinner("Sto selezionando le etichette migliori..."):
            time.sleep(1)
        
        match = [v for v in vini if v["abbinamento"] == cibo and v["mood"] == mood]
        
        if not match:
            match = [v for v in vini if v["abbinamento"] == cibo]

        if match:
            st.success(f"Ecco le proposte ideali per il tuo {mood}:")
            for vino in match:
                # Scheda del vino
                st.markdown(f"""
                <div class="wine-card">
                    <small style="color: #888;">{vino['tipo']} • {vino['corpo']} • {vino['stile']}</small>
                    <h1 style="color: #800020; margin: 5px 0;">{vino['nome']}</h1>
                    <p style="margin: 0; font-weight: bold;">{vino['cantina']}</p>
                    <p style="margin-top: 10px; font-style: italic;">"{vino['descr']}"</p>
                    <div style="background-color: #f9f0f2; padding: 12px; border-radius: 8px; border-left: 4px solid #800020; margin-top: 15px;">
                        <b>PERCHÈ SCEGLIERLO:</b> {vino['perche']}
                    </div>
                    <div class="wine-price">{vino['prezzo']}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # TASTO LINK SCHEDA VINO (Sotto la card)
                st.link_button(f"📄 VEDI SCHEDA COMPLETA DI {vino['nome'].upper()}", vino['link'])
                st.write("")
        else:
            st.error("Nessun vino trovato. Contatta il nostro sommelier!")

st.divider()
st.caption("WineArt Selector - Gestiamo il Caos della scelta.")
