# =================================================================
# 1. IMPORTAZIONE STRUMENTI (Le librerie che servono al programma)
# =================================================================
import streamlit as st  # Serve per creare il sito web
import time             # Serve per creare l'effetto "caricamento"

# =================================================================
# 2. CONFIGURAZIONE DELLA PAGINA (Titolo del tab e Icona)
# =================================================================
st.set_page_config(page_title="WineArt Selector", page_icon="🍷", layout="centered")

# =================================================================
# 3. DESIGN E GRAFICA (Qui decidiamo i colori e le ombre)
# =================================================================
st.markdown("""
    <style>
    /* Sfondo generale del sito */
    .main { background-color: #fdfaf5; } 
    
    /* Stile del bottone principale */
    .stButton>button { width: 100%; border-radius: 25px; background-color: #800020; color: white; font-weight: bold; }
    
    /* La "Cornice" del vino (Wine Card) */
    .wine-card {
        text-align: center;
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08); /* Ombra leggera */
        margin-bottom: 30px;
    }
    
    /* Colore e dimensione dei testi nella scheda */
    .wine-title { color: #800020; font-size: 32px; font-weight: bold; }
    .wine-producer { font-size: 20px; font-weight: bold; color: #333; }
    .wine-region { color: #800020; font-weight: bold; font-size: 18px; }
    .wine-price { font-size: 24px; color: #444; margin-bottom: 20px; }
    
    /* Allineamento delle info tecniche (Uve, Olfatto, Gusto) */
    .tech-info {
        text-align: left;
        display: inline-block;
        max-width: 400px;
        font-size: 16px;
        line-height: 1.6;
        color: #444;
    }
    .check { color: #800020; margin-right: 10px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# =================================================================
# 4. IL DATABASE DEI VINI (Qui è dove aggiungi o modifichi i vini)
# =================================================================
# Ogni blocco tra { ... } è una bottiglia. Copia e incolla per aggiungerne altre.
vini = [
    {
        "nome": "Petite Arvine",
        "produttore": "Les Cretes",
        "regione": "Valle d'Aosta",
        "prezzo": "36 €",
        "uve": "Petite Arvine",
        "olfatto": "Note di frutta esotica, agrumi, bacche di ginepro, biancospino.",
        "gusto": "Sapido e fresco, minerale e bilanciato.",
        "immagine": "https://www.lescretes.it/wp-content/uploads/2021/04/Petite-Arvine-Les-Cretes.png",
        "tipo": "Bianco",
        "abbinamento": "Pesce",          # Deve coincidere con le opzioni del menu sotto
        "mood": "Cena con amici",       # Deve coincidere con le opzioni del menu sotto
        "link_carta": "https://www.cartavinidigitale.it/menu-digitale-wineart/#ancora"
    },
    {
        "nome": "Brunello di Montalcino",
        "produttore": "Casanova di Neri",
        "regione": "Toscana",
        "prezzo": "70 €",
        "uve": "Sangiovese 100%",
        "olfatto": "Ciliegia matura, sottobosco e cuoio.",
        "gusto": "Elegante, tannini setosi, grande persistenza.",
        "immagine": "https://www.casanovadineri.it/uploads/bottiglie/brunello-di-montalcino-docg.png",
        "tipo": "Rosso",
        "abbinamento": "Carne",
        "mood": "Incontro di lavoro",
        "link_carta": "https://www.cartavinidigitale.it/menu-digitale-wineart/#ancora"
    }
]

# =================================================================
# 5. INTERFACCIA UTENTE (Quello che vede il cliente)
# =================================================================
st.title("🍷 WineArt Selector")
st.subheader("La tua guida alla bottiglia perfetta")
st.divider()

# Creiamo due colonne per le domande
col1, col2 = st.columns(2)
with col1:
    # La lista dentro le parentesi [ ] deve contenere gli abbinamenti del database
    cibo = st.selectbox("Cosa mangerai?", ["Scegli...", "Pesce", "Carne", "Aperitivo"])
with col2:
    # La lista dentro le parentesi [ ] deve contenere i mood del database
    mood = st.selectbox("Che atmosfera cerchi?", ["Scegli...", "Cena con amici", "Incontro di lavoro", "Occasione Speciale"])

# =================================================================
# 6. LOGICA DI CALCOLO (Il "cervello" che sceglie il vino)
# =================================================================
if st.button("TROVA IL VINO IDEALE 🍇"):
    if cibo == "Scegli..." or mood == "Scegli...":
        st.warning("Per favore, seleziona sia il cibo che l'atmosfera!")
    else:
        # Il sommelier "pensa" per 1 secondo
        with st.spinner("Il sommelier sta consultando la cantina..."):
            time.sleep(1)
        
        # Filtriamo la lista vini in base alle scelte dell'utente
        match = [v for v in vini if v["abbinamento"] == cibo and v["mood"] == mood]
        
        # Se non troviamo il match perfetto, mostriamo i vini che vanno bene almeno col cibo
        if not match: 
            match = [v for v in vini if v["abbinamento"] == cibo]
        
        # Mostriamo i risultati
        if match:
            for vino in match:
                # Questa parte trasforma i dati del database in una scheda grafica (HTML)
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
                
                # Bottone esterno alla card per andare alla scheda tecnica reale
                st.link_button(f"📄 APRI CARTA: {vino['nome'].upper()}", vino['link_carta'])
        else:
            st.error("Nessun vino trovato! Prova a cambiare abbinamento.")

# =================================================================
# 7. PIE DI PAGINA (Footer)
# =================================================================
st.divider()
st.caption("WineArt Selector - Sviluppato con passione per il gusto.")
