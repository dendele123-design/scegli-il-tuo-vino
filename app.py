import streamlit as st
import time
import random

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="WineArt Selector", page_icon="🍷", layout="centered")

# --- 2. STILE CSS (Look Professionale WineArt) ---
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
    .stButton>button:hover {
        background-color: #a00028;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DATABASE VINI (Aggiungi qui i tuoi vini reali) ---
# Ricordati: ogni riga deve finire con la virgola, tranne l'ultima del blocco.
vini = [
    {
        "nome": "Amarone della Valpolicella",
        "cantina": "Bertani",
        "tipo": "Rosso",
        "corpo": "Robusto",
        "stile": "Fruttato",
        "abbinamento": "Carne",
        "mood": "Occasione Speciale",
        "prezzo": "85.00€",
        "descr": "Note di amarena, cioccolato e spezie. Un classico intramontabile.",
        "perche": "La sua potenza ed eleganza lo rendono perfetto per i momenti che contano."
    },
    {
        "nome": "Vermentino di Gallura",
        "cantina": "Sella & Mosca",
        "tipo": "Bianco",
        "corpo": "Leggero",
        "stile": "Minerale",
        "abbinamento": "Pesce",
        "mood": "Cena con amici",
        "prezzo": "28.00€",
        "descr": "Sapido, fresco, con richiami di macchia mediterranea.",
        "perche": "Perfetto per accompagnare crudi di pesce e risate in compagnia."
    },
    {
        "nome": "Franciacorta Brut DOCG",
        "cantina": "Bellavista",
        "tipo": "Bollicine",
        "corpo": "Leggero",
        "stile": "Secco",
        "abbinamento": "Aperitivo",
        "mood": "Serata romantica",
        "prezzo": "45.00€",
        "descr": "Perlage fine, note di crosta di pane e agrumi.",
        "perche": "Le bollicine sono l'inizio universale di ogni grande serata d'amore."
    },
    {
        "nome": "Gewürztraminer",
        "cantina": "Tramin",
        "tipo": "Bianco",
        "corpo": "Di Medio Corpo",
        "stile": "Aromatico",
        "abbinamento": "Pesce",
        "mood": "Serata romantica",
        "prezzo": "32.00€",
        "descr": "Profumi intensi di litchi, rosa e spezie orientali.",
        "perche": "Il suo carattere avvolgente incanta i sensi fin dal primo sorso."
    },
    {
        "nome": "Brunello di Montalcino",
        "cantina": "Biondi Santi",
        "tipo": "Rosso",
        "corpo": "Robusto",
        "stile": "Secco",
        "abbinamento": "Carne",
        "mood": "Occasione Speciale",
        "prezzo": "95.00€",
        "descr": "Struttura eterna, note di cuoio, tabacco e frutti neri.",
        "perche": "Se cerchi il massimo dell'eleganza toscana, non puoi sbagliare."
    },
    {
        "nome": "Moscato d'Asti DOCG",
        "cantina": "Vietti",
        "tipo": "Dolce",
        "corpo": "Leggero",
        "stile": "Fruttato",
        "abbinamento": "Dessert",
        "mood": "Cena con amici",
        "prezzo": "22.00€",
        "descr": "Dolce, frizzante e incredibilmente fresco.",
        "perche": "Per chiudere la cena con una nota allegra e zuccherina."
    }
]

# --- 4. INTERFACCIA UTENTE ---
st.title("🍷 WineArt Selector")
st.subheader("Trova la bottiglia ideale per la tua serata")
st.write("Rispondi alle domande e lascia che il sommelier scelga per te.")
st.divider()

# Griglia di selezione (2 colonne)
col1, col2 = st.columns(2)

with col1:
    cibo = st.selectbox("1. Cosa c'è nel piatto?", ["Scegli...", "Aperitivo", "Pesce", "Carne", "Dessert"])
    corpo = st.selectbox("3. Struttura del vino?", ["Scegli...", "Leggero", "Di Medio Corpo", "Robusto"])

with col2:
    mood = st.selectbox("2. Che atmosfera cerchi?", ["Scegli...", "Cena con amici", "Serata romantica", "Occasione Speciale"])
    stile = st.selectbox("4. Carattere preferito?", ["Scegli...", "Secco", "Fruttato", "Aromatico", "Minerale"])

st.write("")

# --- 5. LOGICA DI RICERCA ---
if st.button("TROVA IL VINO IDEALE 🍇"):
    
    if cibo == "Scegli..." or mood == "Scegli...":
        st.warning("Seleziona almeno i primi due campi (Cibo e Atmosfera)!")
    else:
        with st.spinner("Il sommelier sta consultando la cantina..."):
            time.sleep(1.2)
        
        # Iniziamo con tutti i vini che si abbinano al cibo scelto
        match = [v for v in vini if v["abbinamento"] == cibo]
        
        # Raffiniamo la ricerca in base alle altre scelte (se effettuate)
        if mood != "Scegli...":
            match = [v for v in match if v["mood"] == mood]
        
        if corpo != "Scegli...":
            match = [v for v in match if v["corpo"] == corpo]
            
        if stile != "Scegli...":
            match = [v for v in match if v["stile"] == stile]

        # --- 6. RISULTATI ---
        if match:
            st.success(f"Ho trovato {len(match)} proposta/e perfetta/e per te:")
            for vino in match:
                st.markdown(f"""
                <div class="wine-card">
                    <small style="color: #888; text-transform: uppercase;">{vino['tipo']} • {vino['corpo']} • {stile if stile != 'Scegli...' else vino['stile']}</small>
                    <h1 style="color: #800020; margin: 5px 0;">{vino['nome']}</h1>
                    <p style="margin: 0; font-weight: bold;">Cantina: {vino['cantina']}</p>
                    <p style="margin-top: 10px; font-style: italic; color: #444;">"{vino['descr']}"</p>
                    <div style="background-color: #f9f0f2; padding: 15px; border-radius: 8px; border-left: 4px solid #800020; margin-top: 15px;">
                        <b>IL SOMMELIER DICE:</b> {vino['perche']}
                    </div>
                    <div class="wine-price">{vino['prezzo']}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.error("Purtroppo non ho un vino che soddisfi tutti i criteri contemporaneamente. Prova a cambiare 'Struttura' o 'Carattere'!")

# --- 7. FOOTER ---
st.divider()
st.caption("WineArt Selector - Tecnologia applicata all'eccellenza enologica.")
