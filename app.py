import streamlit as st
import time
import random

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="WineArt Selector", page_icon="🍷", layout="centered")

# --- 2. STILE CSS (Personalizzato per i colori dei vini) ---
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
    
    /* Stile per i bottoni categoria */
    .stLinkButton>a { width: 100% !important; border-radius: 10px !important; text-align: center !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DATABASE VINI (Con link alle sezioni specifiche) ---
# Link alle ancore (ID) che hai impostato su WordPress
LINK_BASE = "https://www.cartavinidigitale.it/menu-digitale-wineart/"
LINK_BOLLICINE = f"{LINK_BASE}#1745654818035-20641e56-b021" # Esempio ID
LINK_BIANCHI = f"{LINK_BASE}#1745654818035-20641e56-b022"   # Esempio ID
LINK_ROSSI = f"{LINK_BASE}#1745654818035-20641e56-b023"     # Quello che abbiamo testato

vini = [
    {
        "nome": "Franciacorta Cuveé Prestige", "cantina": "Ca' del Bosco", "tipo": "Bollicine",
        "corpo": "Leggero", "stile": "Secco", "abbinamento": "Aperitivo", "mood": "Incontro di lavoro",
        "prezzo": "45.00€", "descr": "Equilibrato, fresco e piacevolmente acido.",
        "perche": "Elegante e professionale, ideale per un aperitivo di business.",
        "link": LINK_BOLLICINE
    },
    {
        "nome": "Greco di Tufo Giallo d'Arles", "cantina": "Quintodecimo", "tipo": "Bianco",
        "corpo": "Di Medio Corpo", "stile": "Minerale", "abbinamento": "Pesce", "mood": "Incontro di lavoro",
        "prezzo": "55.00€", "descr": "Giallo oro, sentori di albicocca e note minerali.",
        "perche": "Un bianco autorevole che dimostra competenza e buon gusto.",
        "link": LINK_BIANCHI
    },
    {
        "nome": "Brunello di Montalcino", "cantina": "Casanova di Neri", "tipo": "Rosso",
        "corpo": "Di Medio Corpo", "stile": "Secco", "abbinamento": "Carne", "mood": "Incontro di lavoro",
        "prezzo": "70.00€", "descr": "Grande bevibilità, ciliegia e sottobosco.",
        "perche": "L'eleganza del Sangiovese in purezza per una cena di classe.",
        "link": LINK_ROSSI
    }
]

# --- 4. INTERFACCIA ---
st.title("🍷 WineArt Selector")
st.subheader("Trova il vino perfetto per il tuo momento")
st.divider()

col1, col2 = st.columns(2)
with col1:
    cibo = st.selectbox("1. Cosa mangi?", ["Scegli...", "Aperitivo", "Pesce", "Carne"])
    corpo = st.selectbox("3. Struttura del vino?", ["Scegli...", "Leggero", "Di Medio Corpo", "Robusto"])
with col2:
    mood = st.selectbox("2. Che atmosfera cerchi?", ["Scegli...", "Cena con amici", "Incontro di lavoro", "Occasione Speciale"])
    stile = st.selectbox("4. Carattere preferito?", ["Scegli...", "Secco", "Fruttato", "Aromatico", "Minerale"])

st.write("")

# --- 5. LOGICA DI RICERCA ---
if st.button("🔍 TROVA IL VINO IDEALE", type="primary"):
    with st.spinner("Consultando la cantina..."):
        time.sleep(0.8)
    
    match = [v for v in vini if v["abbinamento"] == cibo and v["mood"] == mood]
    if not match:
        match = [v for v in vini if v["abbinamento"] == cibo]

    if match:
        st.success(f"Ecco il mio consiglio per te:")
        for vino in match:
            st.markdown(f"""
            <div class="wine-card">
                <small>{vino['tipo']} • {vino['corpo']}</small>
                <h1 style="color: #800020; margin: 5px 0;">{vino['nome']}</h1>
                <p><b>{vino['cantina']}</b></p>
                <p><i>"{vino['descr']}"</i></p>
                <div style="background-color: #f9f0f2; padding: 12px; border-radius: 8px; border-left: 4px solid #800020; margin-top: 15px;">
                    <b>IL SOMMELIER:</b> {vino['perche']}
                </div>
                <div class="wine-price">{vino['prezzo']}</div>
            </div>
            """, unsafe_allow_html=True)
            st.link_button(f"📄 VEDI SCHEDA COMPLETA", vino['link'])
    else:
        st.error("Nessun vino trovato per questa combinazione.")

# --- 6. LA NUOVA PULSANTIERA DI NAVIGAZIONE ---
st.write("")
st.write("")
st.divider()
st.subheader("📂 Oppure esplora le nostre categorie:")

# Creiamo una griglia di bottoni
c1, c2, c3 = st.columns(3)

with c1:
    st.link_button("🥂 LE BOLLICINE", LINK_BOLLICINE)
with c2:
    st.link_button("🍸 I BIANCHI", LINK_BIANCHI)
with c3:
    st.link_button("🍷 I ROSSI", LINK_ROSSI)

st.write("")
st.link_button("📖 APRI LA CARTA VINI COMPLETA (Dall'inizio)", LINK_BASE)

st.divider()
st.caption("WineArt Selector - Scegli l'eccellenza.")
