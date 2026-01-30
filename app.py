import streamlit as st
import time
import random

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="WineArt Selector", page_icon="🍷", layout="centered")

# --- 2. STILE CSS (WineArt Design) ---
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
    .wine-price { 
        color: #800020; 
        font-size: 26px; 
        font-weight: bold; 
        margin-top: 10px;
    }
    .stButton>button { 
        width: 100%; 
        border-radius: 25px; 
        height: 3.5em; 
        background-color: #800020; 
        color: white; 
        font-weight: bold;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DATABASE VINI REALI (Dalla tua carta WineArt) ---
vini = [
    # BOLLICINE
    {
        "nome": "Champagne Vintage 2013", "cantina": "Dom Pérignon", "tipo": "Bollicine",
        "corpo": "Robusto", "stile": "Minerale", "abbinamento": "Pesce", "mood": "Occasione Speciale",
        "prezzo": "280.00€", "descr": "Un'icona di equilibrio e complessità, note floreali e minerali.",
        "perche": "Per rendere un momento storico assolutamente indimenticabile."
    },
    {
        "nome": "Franciacorta Cuveé Prestige", "cantina": "Ca' del Bosco", "tipo": "Bollicine",
        "corpo": "Leggero", "stile": "Secco", "abbinamento": "Aperitivo", "mood": "Cena con amici",
        "prezzo": "45.00€", "descr": "Equilibrato, fresco e piacevolmente acido.",
        "perche": "Il classico intramontabile per iniziare ogni serata col piede giusto."
    },
    {
        "nome": "Prosecco Valdobbiadene Sup. DOCG", "cantina": "Col Vetoraz", "tipo": "Bollicine",
        "corpo": "Leggero", "stile": "Fruttato", "abbinamento": "Aperitivo", "mood": "Cena con amici",
        "prezzo": "22.00€", "descr": "Note di mela, pera e fiori d'acacia.",
        "perche": "Freschezza e brio per un brindisi leggero e profumato."
    },

    # BIANCHI
    {
        "nome": "Greco di Tufo Giallo d'Arles", "cantina": "Quintodecimo", "tipo": "Bianco",
        "corpo": "Di Medio Corpo", "stile": "Minerale", "abbinamento": "Pesce", "mood": "Serata romantica",
        "prezzo": "55.00€", "descr": "Giallo oro, sentori di albicocca e note minerali profonde.",
        "perche": "Un bianco di grande carattere che incanta per la sua sapidità."
    },
    {
        "nome": "Chardonnay Lowengang", "cantina": "Alois Lageder", "tipo": "Bianco",
        "corpo": "Robusto", "stile": "Secco", "abbinamento": "Pesce", "mood": "Occasione Speciale",
        "prezzo": "75.00€", "descr": "Affidato al legno, complesso, con note di burro e vaniglia.",
        "perche": "Se cerchi un bianco che abbia la struttura di un grande rosso."
    },
    {
        "nome": "Sauvignon Winkl", "cantina": "Terlan", "tipo": "Bianco",
        "corpo": "Leggero", "stile": "Aromatico", "abbinamento": "Pesce", "mood": "Cena con amici",
        "prezzo": "32.00€", "descr": "Note intense di sambuco, frutta tropicale e peperone giallo.",
        "perche": "L'aperitivo o la cena di pesce trovano il compagno ideale per profumi e freschezza."
    },

    # ROSSI
    {
        "nome": "Sassicaia 2020", "cantina": "Tenuta San Guido", "tipo": "Rosso",
        "corpo": "Robusto", "stile": "Secco", "abbinamento": "Carne", "mood": "Occasione Speciale",
        "prezzo": "350.00€", "descr": "Maestoso, note di piccoli frutti rossi, erbe aromatiche e tannini setosi.",
        "perche": "Stai scegliendo la storia dell'enologia mondiale. Non serve aggiungere altro."
    },
    {
        "nome": "Tignanello 2020", "cantina": "Antinori", "tipo": "Rosso",
        "corpo": "Robusto", "stile": "Fruttato", "abbinamento": "Carne", "mood": "Occasione Speciale",
        "prezzo": "160.00€", "descr": "Note di frutti rossi maturi, vaniglia e pepe nero.",
        "perche": "Un supertuscan leggendario per chi vuole eleganza e potenza."
    },
    {
        "nome": "Brunello di Montalcino", "cantina": "Casanova di Neri", "tipo": "Rosso",
        "corpo": "Di Medio Corpo", "stile": "Secco", "abbinamento": "Carne", "mood": "Serata romantica",
        "prezzo": "70.00€", "descr": "Grande bevibilità, ciliegia, cuoio e sottobosco.",
        "perche": "L'eleganza del Sangiovese in purezza per una cena di classe."
    },
    {
        "nome": "Primitivo di Manduria Es", "cantina": "Gianfranco Fino", "tipo": "Rosso",
        "corpo": "Robusto", "stile": "Fruttato", "abbinamento": "Carne", "mood": "Cena con amici",
        "prezzo": "85.00€", "descr": "Un'esplosione di frutta rossa in confettura e spezie dolci.",
        "perche": "Un vino generoso, avvolgente e potente che scalda la serata."
    },
    {
        "nome": "Pinot Nero Barthenau", "cantina": "J. Hofstatter", "tipo": "Rosso",
        "corpo": "Leggero", "stile": "Aromatico", "abbinamento": "Carne", "mood": "Serata romantica",
        "prezzo": "90.00€", "descr": "Finezza assoluta, note di lampone e frutti di bosco.",
        "perche": "Il vino della seduzione: leggero, profumato e incredibilmente elegante."
    }
]

# --- 4. INTERFACCIA UTENTE ---
st.title("🍷 WineArt Selector")
st.subheader("Trova la bottiglia ideale dalla nostra carta")
st.divider()

col1, col2 = st.columns(2)
with col1:
    cibo = st.selectbox("1. Cosa c'è nel piatto?", ["Scegli...", "Aperitivo", "Pesce", "Carne"])
    corpo = st.selectbox("3. Struttura del vino?", ["Scegli...", "Leggero", "Di Medio Corpo", "Robusto"])

with col2:
    mood = st.selectbox("2. Che atmosfera cerchi?", ["Scegli...", "Cena con amici", "Serata romantica", "Occasione Speciale"])
    stile = st.selectbox("4. Carattere preferito?", ["Scegli...", "Secco", "Fruttato", "Aromatico", "Minerale"])

st.write("")

# --- 5. LOGICA DI RICERCA ---
if st.button("INTERROGA IL SOMMELIER 🍇"):
    if cibo == "Scegli..." or mood == "Scegli...":
        st.warning("Seleziona almeno Cibo e Atmosfera!")
    else:
        with st.spinner("Sto consultando la cantina WineArt..."):
            time.sleep(1.2)
        
        # Iniziamo filtrando per Cibo (fondamentale)
        match = [v for v in vini if v["abbinamento"] == cibo]
        
        # Filtriamo per Mood
        if mood != "Scegli...":
            match = [v for v in match if v["mood"] == mood]
        
        # Se l'utente ha scelto anche Corpo o Stile, proviamo a restringere
        # Ma se la ricerca diventa troppo stretta (0 risultati), mostriamo comunque i match precedenti
        match_stretto = match.copy()
        if corpo != "Scegli...":
            match_stretto = [v for v in match_stretto if v["corpo"] == corpo]
        if stile != "Scegli...":
            match_stretto = [v for v in match_stretto if v["stile"] == stile]

        final_list = match_stretto if match_stretto else match

        # --- 6. RISULTATI ---
        if final_list:
            st.success(f"Dalla nostra carta, ecco {len(final_list)} proposte per te:")
            for vino in final_list:
                st.markdown(f"""
                <div class="wine-card">
                    <small style="color: #888;">{vino['tipo']} • {vino['corpo']} • {vino['stile']}</small>
                    <h1 style="color: #800020; margin: 5px 0;">{vino['nome']}</h1>
                    <p style="margin: 0; font-weight: bold;">{vino['cantina']}</p>
                    <p style="margin-top: 10px; font-style: italic;">"{vino['descr']}"</p>
                    <div style="background-color: #f9f0f2; padding: 12px; border-radius: 8px; border-left: 4px solid #800020; margin-top: 15px;">
                        <b>IL CONSIGLIO:</b> {vino['perche']}
                    </div>
                    <div class="wine-price">{vino['prezzo']}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.error("Nessun vino trovato. Chiedi al sommelier in sala, ha sempre qualche rarità fuori carta!")

st.divider()
st.caption("WineArt Selector - Scegli l'eccellenza.")
