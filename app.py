import streamlit as st
import pandas as pd
from datetime import datetime

# Categorie disponibili
CATEGORIE = [
    "Filtri",
    "Pastiglie anteriori",
    "Pastiglie posteriori",
    "Segnalatore d'usura anteriore",
    "Segnalatore d'usura posteriore",
    "Dischi anteriori",
    "Dischi posteriori",
    "Candele",
    "Candelette"
]

# Inizializza session state per log
if 'log' not in st.session_state:
    st.session_state['log'] = []

st.title("Ricerca Rapida Ricambi - YQ Service")

vin = st.text_input("Inserisci VIN")
categoria = st.selectbox("Seleziona Categoria", CATEGORIE)

if st.button("Cerca"):
    # Simulazione risultati (da sostituire con chiamata API in futuro)
    risultati = pd.DataFrame({
        "Codice OEM": ["12345-ABC", "67890-DEF"],
        "Descrizione": ["Filtro Olio OEM", "Filtro Abitacolo OEM"]
    }) if categoria == "Filtri" else pd.DataFrame({
        "Codice OEM": ["99999-ZZZ"],
        "Descrizione": [f"{categoria} OEM"]
    })

    # Visualizza risultati
    st.subheader("Risultati Ricerca")
    st.dataframe(risultati)

    # Esporta in Excel
    excel_filename = f"risultati_{vin}_{categoria.replace(' ', '_')}.xlsx"
    risultati.to_excel(excel_filename, index=False)
    with open(excel_filename, "rb") as f:
        st.download_button("Scarica risultati in Excel", f, file_name=excel_filename)

    # Log ricerca
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state['log'].append({
        "timestamp": timestamp,
        "vin": vin,
        "categoria": categoria
    })

# Mostra log ricerche precedenti
if st.session_state['log']:
    st.subheader("Log Ricerche Effettuate")
    log_df = pd.DataFrame(st.session_state['log'])
    st.dataframe(log_df)
    log_csv = log_df.to_csv(index=False).encode('utf-8')
    st.download_button("Scarica Log in CSV", log_csv, file_name="log_ricerche.csv")
