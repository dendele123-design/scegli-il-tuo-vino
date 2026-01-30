import streamlit as st
import time
import random

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="WineArt Selector", page_icon="🍷", layout="centered")

# --- 2. STILE CSS (WineArt Identity) ---
st.markdown("""
    <style>
    .main { background-color: #f4f4f4; }
    .wine-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        border-left: 10px solid #800020;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
    .wine-price { color: #800020; font-size: 26px; font-weight: bold; margin-top: 10px; }
    .stButton>button { width: 100%; border-radius: 25px; height: 3.5em; background-color: #800020; color: white; font-weight: bold; border: none; }
    .stLinkButton>a { width: 100% !important; border-radius: 20px !important; text-align: center !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DATABASE VINI (3 per Categoria con Link dedicati) ---
LINK_BASE = "https://www.cartavinidigitale.it/menu-digitale-wineart/"

vini = [
    # --- BOLLICINE ---
    {"nome": "Franciacorta Cuveé Prestige", "cantina": "Ca' del Bosco", "tipo": "Bollicine", "corpo": "Leggero", "stile": "Secco", "abbinamento": "Aperitivo", "mood": "Incontro di lavoro", "prezzo": "45€", "descr": "Equilibrato e fresco.", "cat_link": f"{LINK_BASE}#1740398853462-a2bc72ab-7b7d"},
    {"nome": "Franciacorta Alma Brut", "cantina": "Bellavista", "tipo": "Bollicine", "corpo": "Leggero", "stile": "Secco", "abbinamento": "Aperitivo", "mood": "Cena con amici", "prezzo": "42€", "descr": "Note di frutti bianchi e fiori.", "cat_link": f"{LINK_BASE}#1740398853462-a2bc72ab-7b7d"},
    {"nome": "Trento DOC Brut", "cantina": "Ferrari", "tipo": "Bollicine", "corpo": "Leggero", "stile": "Minerale", "abbinamento": "Aperitivo", "mood": "Incontro di lavoro", "prezzo": "30€", "descr": "Grande eleganza e freschezza.", "cat_link": f"{LINK_BASE}#1740398853462-a2bc72ab-7b7d"},

    # --- CHAMPAGNE ---
    {"nome": "Vintage 2013", "cantina": "Dom Pérignon", "tipo": "Champagne", "corpo": "Robusto", "stile": "Minerale", "abbinamento": "Pesce", "mood": "Occasione Speciale", "prezzo": "280€", "descr": "Iconico e complesso.", "cat_link": f"{LINK_BASE}#1745914895725-84011f71-5d21"},
    {"nome": "Grande Cuvée", "cantina": "Krug", "tipo": "Champagne", "corpo": "Robusto", "stile": "Aromatico", "abbinamento": "Pesce", "mood": "Occasione Speciale", "prezzo": "320€", "descr": "Il Re degli Champagne.", "cat_link": f"{LINK_BASE}#1745914895725-84011f71-5d21"},
    {"nome": "Brut Imperial", "cantina": "Moët & Chandon", "tipo": "Champagne", "corpo": "Di Medio Corpo", "stile": "Fruttato", "abbinamento": "Pesce", "mood": "Incontro di lavoro", "prezzo": "65€", "descr": "Fresco e ammiccante.", "cat_link": f"{LINK_BASE}#1745914895725-84011f71-5d21"},

    # --- BIANCHI ---
    {"nome": "Greco di Tufo Giallo d'Arles", "cantina": "Quintodecimo", "tipo": "Vini Bianchi", "corpo": "Di Medio Corpo", "stile": "Minerale", "abbinamento": "Pesce", "mood": "Incontro di lavoro", "prezzo": "55€", "descr": "Potente e sapido.", "cat_link": f"{LINK_BASE}#1745853678461-fb96405a-dddb"},
    {"nome": "Pinot Grigio", "cantina": "Jermann", "tipo": "Vini Bianchi", "corpo": "Leggero", "stile": "Secco", "abbinamento": "Pesce", "mood": "Cena con amici", "prezzo": "35€", "descr": "Un classico d'autore.", "cat_link": f"{LINK_BASE}#1745853678461-fb96405a-dddb"},
    {"nome": "Chardonnay Lowengang", "cantina": "Alois Lageder", "tipo": "Vini Bianchi", "corpo": "Robusto", "stile": "Secco", "abbinamento": "Pesce", "mood": "Occasione Speciale", "prezzo": "75€", "descr": "Vellutato e persistente.", "cat_link": f"{LINK_BASE}#1745853678461-fb96405a-dddb"},

    # --- ROSÈ ---
    {"nome": "Rosa del Golfo", "cantina": "Rosa del Golfo", "tipo": "Vini Rosè", "corpo": "Leggero", "stile": "Fruttato", "abbinamento": "Aperitivo", "mood": "Cena con amici", "prezzo": "22€", "descr": "Tipico salentino, fragrante.", "cat_link": f"{LINK_BASE}#1740390912898-ab964a88-abf3"},
    {"nome": "Calafuria", "cantina": "Tormaresca", "tipo": "Vini Rosè", "corpo": "Leggero", "stile": "Fruttato", "abbinamento": "Pesce", "mood": "Cena con amici", "prezzo": "25€", "descr": "Note di petali di rosa e pompelmo.", "cat_link": f"{LINK_BASE}#1740390912898-ab964a88-abf3"},
    {"nome": "Whispering Angel", "cantina": "Chateau d'Esclans", "tipo": "Vini Rosè", "corpo": "Di Medio Corpo", "stile": "Minerale", "abbinamento": "Aperitivo", "mood": "Occasione Speciale", "prezzo": "40€", "descr": "Il Rosé più glamour del mondo.", "cat_link": f"{LINK_BASE}#1740390912898-ab964a88-abf3"},

    # --- ROSSI ---
    {"nome": "Sassicaia 2020", "cantina": "Tenuta San Guido", "tipo": "Vini Rossi", "corpo": "Robusto", "stile": "Secco", "abbinamento": "Carne", "mood": "Occasione Speciale", "prezzo": "350€", "descr": "Aristocratico e profondo.", "cat_link": f"{LINK_BASE}#1745654818035-20641e56-b023"},
    {"nome": "Brunello di Montalcino", "cantina": "Casanova di Neri", "tipo": "Vini Rossi", "corpo": "Di Medio Corpo", "stile": "Secco", "abbinamento": "Carne", "mood": "Incontro di lavoro", "prezzo": "70€", "descr": "Elegante Sangiovese.", "cat_link": f"{LINK_BASE}#1745654818035-20641e56-b023"},
    {"nome": "Tignanello", "cantina": "Antinori", "tipo": "Vini Rossi", "corpo": "Robusto", "stile": "Fruttato", "abbinamento": "Carne", "mood": "Occasione Speciale", "prezzo": "160€", "descr": "Il Supertuscan per eccellenza.", "cat_link": f"{LINK_BASE}#1745654818035-20641e56-b023"},

    # --- ESTERI ---
    {"nome": "Malbec Argentino", "cantina": "Catena Zapata", "tipo": "Vini Esteri", "corpo": "Robusto", "stile": "Fruttato", "abbinamento": "Carne", "mood": "Incontro di lavoro", "prezzo": "110€", "descr": "Potente e vellutato.", "cat_link": f"{LINK_BASE}#1745917570747-12734a65-c3ee"},
    {"nome": "Pinot Noir Gevrey-Chambertin", "cantina": "Louis Jadot", "tipo": "Vini Esteri", "corpo": "Di Medio Corpo", "stile": "Aromatico", "abbinamento": "Carne", "mood": "Occasione Speciale", "prezzo": "95€", "descr": "La classe della Borgogna.", "cat_link": f"{LINK_BASE}#1745917570747-12734a65-c3ee"},
    {"nome": "Riesling Trocken", "cantina": "Dr. Loosen", "tipo": "Vini Esteri", "corpo": "Leggero", "stile": "Minerale", "abbinamento": "Pesce", "mood": "Cena con amici", "prezzo": "30€", "descr": "Acidità citrina e mineralità.", "cat_link": f"{LINK_BASE}#1745917570747-12734a65-c3ee"},
]

# --- 4. INTERFACCIA ---
st.title("🍷 WineArt Selector")
st.link_button("📖 CARTA VINI COMPLETA", LINK_BASE)
st.write("")

col1, col2 = st.columns(2)
with col1:
    cibo = st.selectbox("1. Cosa mangi?", ["Scegli...", "Aperitivo", "Pesce", "Carne"])
    corpo = st.selectbox("3. Struttura?", ["Scegli...", "Leggero", "Di Medio Corpo", "Robusto"])
with col2:
    mood = st.selectbox("2. Atmosfera?", ["Scegli...", "Cena con amici", "Incontro di lavoro", "Occasione Speciale"])
    stile = st.selectbox("4. Carattere?", ["Scegli...", "Secco", "Fruttato", "Aromatico", "Minerale"])

if st.button("🔎 TROVA IL VINO IDEALE", type="primary"):
    if cibo == "Scegli..." or mood == "Scegli...":
        st.warning("Seleziona almeno Cibo e Atmosfera!")
    else:
        with st.spinner("Sto consultando la cantina..."):
            time.sleep(1)
        
        # Logica di Filtro
        match = [v for v in vini if v["abbinamento"] == cibo and v["mood"] == mood]
        if not match: match = [v for v in vini if v["abbinamento"] == cibo]

        if match:
            for vino in match:
                st.markdown(f"""
                <div class="wine-card">
                    <small>{vino['tipo']} • {vino['corpo']} • {vino['stile']}</small>
                    <h1 style="color: #800020; margin: 5px 0;">{vino['nome']}</h1>
                    <p><b>{vino['cantina']}</b></p>
                    <p><i>"{vino['descr']}"</i></p>
                    <div class="wine-price">{vino['prezzo']}</div>
                </div>
                """, unsafe_allow_html=True)
                # TASTO DINAMICO PER CATEGORIA
                st.link_button(f"🔎 VEDI TUTTI I {vino['tipo'].upper()}", vino['cat_link'])
                st.write("")
        else:
            st.error("Nessun vino trovato. Contatta il sommelier!")

st.divider()
st.caption("WineArt Selector - Gestiamo il Caos della scelta.")
