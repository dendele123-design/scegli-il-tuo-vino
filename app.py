import streamlit as st
import time
import random

# =================================================================
# 1. CONFIGURAZIONE E GRAFICA (Il "Look" dell'app)
# =================================================================
st.set_page_config(page_title="WineArt Selector", page_icon="🍷", layout="centered")

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
    .wine-title { color: #800020; font-size: 30px; font-weight: bold; margin-bottom: 0px; }
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
# 2. LINK ALLE CATEGORIE (Le tue ancore di WordPress)
# =================================================================
LINK_BASE = "https://www.cartavinidigitale.it/menu-digitale-wineart/"
LINK_BOLLICINE = f"{LINK_BASE}#1740398853462-a2bc72ab-7b7d"
LINK_CHAMPAGNE = f"{LINK_BASE}#1745914895725-84011f71-5d21"
LINK_BIANCHI = f"{LINK_BASE}#1745853678461-fb96405a-dddb"
LINK_ROSE = f"{LINK_BASE}#1740390912898-ab964a88-abf3"
LINK_ROSSI = f"{LINK_BASE}#1745654818035-20641e56-b023"
LINK_ESTERI = f"{LINK_BASE}#1745917570747-12734a65-c3ee"

# =================================================================
# 3. DATABASE VINI (Esempio con i campi della scheda tecnica)
# =================================================================
vini = [
    {
        "nome": "Petite Arvine", "produttore": "Les Cretes", "regione": "Valle d'Aosta",
        "prezzo": "36€", "uve": "Petite Arvine 100%", 
        "olfatto": "Note di frutta esotica, agrumi e fiori bianchi.",
        "gusto": "Sapido, fresco e minerale.",
        "immagine": "https://www.cartavinidigitale.it/wp-content/uploads/2026/01/Les_cretes_fumin_superstart.jpg",
        "tipo": "Vini Bianchi", "corpo": "Leggero", "stile": "Minerale", 
        "abbinamento": "Pesce", "mood": "Incontro di lavoro", "link": LINK_BIANCHI
    },
    {
        "nome": "Sassicaia 2020", "produttore": "Tenuta San Guido", "regione": "Toscana",
        "prezzo": "350€", "uve": "Cabernet Sauvignon, Cabernet Franc", 
        "olfatto": "Piccoli frutti rossi, erbe aromatiche e note tostate.",
        "gusto": "Maestoso, con tannini setosi e infinita persistenza.",
        "immagine": "https://www.tenutasanguido.com/images/bottiglia_sassicaia.png", # Link esempio
        "tipo": "Vini Rossi", "corpo": "Robusto", "stile": "Secco", 
        "abbinamento": "Carne", "mood": "Occasione Speciale", "link": LINK_ROSSI
    },
    {
        "nome": "Franciacorta Cuveé Prestige", "produttore": "Ca' del Bosco", "regione": "Lombardia",
        "prezzo": "45€", "uve": "Chardonnay, Pinot Nero, Pinot Bianco", 
        "olfatto": "Note di agrumi, crosta di pane e frutta bianca.",
        "gusto": "Equilibrato, fresco e piacevolmente acido.",
        "immagine": "https://www.cadelbosco.com/wp-content/uploads/2021/03/cuvee-prestige.png", # Link esempio
        "tipo": "Bollicine", "corpo": "Leggero", "stile": "Secco", 
        "abbinamento": "Aperitivo", "mood": "Incontro di lavoro", "link": LINK_BOLLICINE
    }
    # AGGIUNGI QUI GLI ALTRI VINI SEGUENDO QUESTO SCHEMA...
]

# =================================================================
# 4. INTERFACCIA (Menu e Pulsanti)
# =================================================================
st.title("🍷 WineArt Selector")
# Tasto in alto per tornare al sito
st.link_button("📖 CARTA VINI COMPLETA", LINK_BASE)
st.write("")

# Le 4 caselle di scelta
col1, col2 = st.columns(2)
with col1:
    cibo = st.selectbox("1. Cosa mangi?", ["Scegli...", "Aperitivo", "Pesce", "Carne", "Dessert"])
    corpo = st.selectbox("3. Struttura?", ["Scegli...", "Leggero", "Di Medio Corpo", "Robusto"])
with col2:
    mood = st.selectbox("2. Atmosfera?", ["Scegli...", "Cena con amici", "Incontro di lavoro", "Occasione Speciale"])
    stile = st.selectbox("4. Carattere?", ["Scegli...", "Secco", "Fruttato", "Aromatico", "Minerale"])

st.write("")

# =================================================================
# 5. LOGICA DI RICERCA (Il "Cervello")
# =================================================================
if st.button("🔎 TROVA IL VINO IDEALE", type="primary"):
    if cibo == "Scegli..." or mood == "Scegli...":
        st.warning("Per favore, seleziona almeno Cibo e Atmosfera!")
    else:
        with st.spinner("Il sommelier sta consultando la cantina..."):
            time.sleep(1)
        
        # Filtro base (Cibo + Mood)
        match = [v for v in vini if v["abbinamento"] == cibo and v["mood"] == mood]
        
        # Se non c'è match, usiamo solo il cibo
        if not match: match = [v for v in vini if v["abbinamento"] == cibo]
        
        # Filtro opzionale per Corpo e Stile
        if match:
            match_finale = match.copy()
            if corpo != "Scegli...":
                match_finale = [v for v in match_finale if v["corpo"] == corpo]
            if stile != "Scegli...":
                match_finale = [v for v in match_finale if v["stile"] == stile]
            
            # Se il filtro troppo stretto dà zero, torniamo al match precedente
            risultati = match_finale if match_finale else match

            st.success(f"Ho trovato {len(risultati)} proposta/e per te:")
            for vino in risultati:
                # LA SCHEDA GRAFICA (Come lo screenshot)
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
                # TASTO DINAMICO CATEGORIA
                st.link_button(f"🔎 VEDI TUTTI I {vino['tipo'].upper()}", vino['link'])
                st.write("")
        else:
            st.error("Nessun vino trovato. Prova a cambiare i filtri!")

# =================================================================
# 6. PULSANTIERA CATEGORIE (Tasti rapidi in basso)
# =================================================================
st.divider()
st.subheader("📂 Esplora le categorie:")
c1, c2, c3 = st.columns(3)
with c1: st.link_button("🥂 BOLLICINE", LINK_BOLLICINE)
with c2: st.link_button("✨ CHAMPAGNE", LINK_CHAMPAGNE)
with c3: st.link_button("🍸 BIANCHI", LINK_BIANCHI)

c4, c5, c6 = st.columns(3)
with c4: st.link_button("🌸 ROSÈ", LINK_ROSE)
with c5: st.link_button("🍷 ROSSI", LINK_ROSSI)
with c6: st.link_button("🌍 ESTERI", LINK_ESTERI)

st.caption("WineArt Selector - Tecnologia applicata al gusto.")
