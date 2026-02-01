import streamlit as st
import time
import random

# =================================================================
# 1. CONFIGURAZIONE E STILE (App Wine Selector 1.0)
# =================================================================
st.set_page_config(page_title="Wine Selector 1.0", page_icon="🍷", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #fdfaf5; }
    .wine-card {
        text-align: center;
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin-bottom: 30px;
    }
    .wine-title { color: #800020; font-size: 30px; font-weight: bold; margin-bottom: 5px; }
    .wine-producer { font-size: 18px; font-weight: bold; color: #333; margin-bottom: 0px; }
    .wine-region { color: #800020; font-weight: bold; font-size: 16px; margin-bottom: 5px; }
    .wine-price { font-size: 22px; color: #444; margin-bottom: 20px; font-weight: bold; }
    .tech-info { text-align: left; display: inline-block; max-width: 450px; font-size: 15px; color: #444; }
    .check { color: #800020; margin-right: 8px; font-weight: bold; }
    .stButton>button { width: 100%; border-radius: 25px; background-color: #800020; color: white; font-weight: bold; }
    .stLinkButton>a { width: 100% !important; border-radius: 20px !important; text-align: center !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

# =================================================================
# 2. ANCORE CATEGORIE CARTA VINI
# =================================================================
LINK_BASE = "https://www.cartavinidigitale.it/menu-digitale-wineart/"
LINK_BOLLICINE = f"{LINK_BASE}#1740398853462-a2bc72ab-7b7d"
LINK_CHAMPAGNE = f"{LINK_BASE}#1745914895725-84011f71-5d21"
LINK_BIANCHI = f"{LINK_BASE}#1745853678461-fb96405a-dddb"
LINK_ROSE = f"{LINK_BASE}#1740390912898-ab964a88-abf3"
LINK_ROSSI = f"{LINK_BASE}#1745654818035-20641e56-b023"
LINK_ESTERI = f"{LINK_BASE}#1745917570747-12734a65-c3ee"

# =================================================================
# 3. DATABASE VINI (Modello Scheda Tecnica)
# =================================================================
vini = [
    {
        "nome": "Petite Arvine", "produttore": "Les Cretes", "regione": "Valle d'Aosta",
        "prezzo": "36€", "uve": "Petite Arvine 100%", 
        "olfatto": "Note di frutta esotica, agrumi e fiori bianchi.",
        "gusto": "Sapido, fresco e minerale.",
        "immagine": "https://www.lescretes.it/wp-content/uploads/2021/04/Petite-Arvine-Les-Cretes.png",
        "tipo": "Vini Bianchi", "corpo": "Leggero", 
        "abbinamento": "Pesce", "mood": "Incontro di lavoro", "link": LINK_BIANCHI
    },
    {
        "nome": "Brunello di Montalcino", "produttore": "Casanova di Neri", "regione": "Toscana",
        "prezzo": "70€", "uve": "Sangiovese 100%", 
        "olfatto": "Sentori di ciliegia matura, sottobosco e cuoio.",
        "gusto": "Elegante, tannini setosi e grande persistenza.",
        "immagine": "https://www.casanovadineri.it/uploads/bottiglie/brunello-di-montalcino-docg.png",
        "tipo": "Vini Rossi", "corpo": "Di Medio Corpo", 
        "abbinamento": "Carne", "mood": "Incontro di lavoro", "link": LINK_ROSSI
    },
    {
        "nome": "Sassicaia 2020", "produttore": "Tenuta San Guido", "regione": "Toscana",
        "prezzo": "350€", "uve": "Cabernet Sauvignon, Cabernet Franc", 
        "olfatto": "Piccoli frutti rossi, erbe aromatiche e note tostate.",
        "gusto": "Maestoso, con tannini setosi e infinita persistenza.",
        "immagine": "https://www.tenutasanguido.com/images/bottiglia_sassicaia.png",
        "tipo": "Vini Rossi", "corpo": "Robusto", 
        "abbinamento": "Carne", "mood": "Occasione Speciale", "link": LINK_ROSSI
    }
    # Aggiungi qui gli altri 15 vini seguendo questo schema...
]

# =================================================================
# 4. INTERFACCIA (App Wine Selector 1.0)
# =================================================================
st.title("🍷 Wine Selector 1.0")
st.link_button("📖 CARTA VINI COMPLETA", LINK_BASE)
st.write("")

# Menu di scelta semplificato a 3 caselle
col1, col2, col3 = st.columns(3)
with col1:
    cibo = st.selectbox("1. Cosa mangi?", ["Scegli...", "Aperitivo", "Pesce", "Carne", "Dessert"])
with col2:
    mood = st.selectbox("2. Atmosfera?", ["Scegli...", "Cena con amici", "Incontro di lavoro", "Occasione Speciale"])
with col3:
    corpo = st.selectbox("3. Struttura?", ["Scegli...", "Leggero", "Di Medio Corpo", "Robusto"])

st.write("")

# =================================================================
# 5. LOGICA DI RICERCA
# =================================================================
if st.button("🔎 TROVA IL VINO IDEALE", type="primary"):
    if cibo == "Scegli..." or mood == "Scegli...":
        st.warning("Per favore, seleziona almeno Cibo e Atmosfera!")
    else:
        with st.spinner("Il sommelier sta cercando in cantina..."):
            time.sleep(1)
        
        # Filtro base
        match = [v for v in vini if v["abbinamento"] == cibo and v["mood"] == mood]
        
        # Raffinamento opzionale per Struttura
        if match and corpo != "Scegli...":
            match_struttura = [v for v in match if v["corpo"] == corpo]
            if match_struttura:
                match = match_struttura

        if match:
            st.success(f"Ho trovato {len(match)} proposta/e per te:")
            for vino in match:
                st.markdown(f"""
                <div class="wine-card">
                    <img src="{vino['immagine']}" width="150">
                    <div class="wine-title">{vino['nome']}</div>
                    <div class="wine-producer">{vino['produttore']}</div>
                    <div class="wine-region">{vino['regione']}</div>
                    <div class="wine-price">{vino['prezzo']}</div>
                    <div class="tech-info">
                        <p><span class="check">✔</span> <b>Uve:</b> {vino['uve']}</p>
                        <p><span class="check">✔</span> <b>Olfatto:</b> {vino['olfatto']}</p>
                        <p><span class="check">✔</span> <b>Gusto:</b> {vino['gusto']}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.link_button(f"🔎 VEDI TUTTI I {vino['tipo'].upper()}", vino['link'])
                st.write("")
        else:
            st.error("Nessun vino trovato. Prova a cambiare i parametri!")

# =================================================================
# 6. PULSANTIERA CATEGORIE
# =================================================================
st.divider()
st.subheader("📂 Esplora le sezioni:")
c1, c2, c3 = st.columns(3)
with c1: st.link_button("🥂 BOLLICINE", LINK_BOLLICINE)
with c2: st.link_button("✨ CHAMPAGNE", LINK_CHAMPAGNE)
with c3: st.link_button("🍸 BIANCHI", LINK_BIANCHI)

c4, c5, c6 = st.columns(3)
with c4: st.link_button("🌸 ROSÈ", LINK_ROSE)
with c5: st.link_button("🍷 ROSSI", LINK_ROSSI)
with c6: st.link_button("🌍 ESTERI", LINK_ESTERI)

st.caption("App Wine Selector 1.0 • Sviluppato con tecnologia Streamlit")
