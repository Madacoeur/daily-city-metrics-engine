import streamlit as st
import pandas as pd
import sqlite3

st.title("Dashboard Urban Data : Velib & Meteo")
st.markdown("Bienvenue sur la vitrine de mon projet ETL. Ce tableau de bord affiche les donnees des stations Velib a Paris, enrichies avec la temperature actuelle.")

#Connexion a la base de donnees
def load_data():
    conn = sqlite3.connect("pipeline_ville.db")

    query = "SELECT * FROM stations"
    df = pd.read_sql(query, conn)

    conn.close()

    return df

df_stations = load_data()

st.subheader("Apercu des donnees extraites")

st.dataframe(df_stations.head(10))

#4. Indicateurs clés (KPIs) ---
st.subheader("📊 Résumé en temps réel")

# on utilise Pandas pour faire des calculs sur notre tableau
# sum() additionne toutes les valeurs de la colonne
total_velos = int(df_stations['free_bikes'].sum())
total_places = int(df_stations['empty_slots'].sum())

# .iloc[0] permet de récupérer la valeur de la toute première ligne (index 0)
temp_actuelle = df_stations['temperature'].iloc[0]

# streamlit permet de diviser la page en plusieurs colonnes invisibles
col1, col2, col3 = st.columns(3)

# on place un indicateur (metric) dans chaque colonne
with col1:
    st.metric(label="🌡️ Température", value=f"{temp_actuelle} °C")
with col2:
    st.metric(label="🚲 Vélos disponibles", value=total_velos)
with col3:
    st.metric(label="🅿️ Places libres", value=total_places)


# 5. Carte Interactive ---
st.subheader("📍 Carte des stations")

# streamlit possède une fonction magique pour les cartes. 
# si DataFrame contient des colonnes nommées exactement 'latitude' et 'longitude', 
# il place automatiquement les points dessus
st.map(df_stations)
