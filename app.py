import streamlit as st
import pandas as pd
import sqlite3

#st.title et st.markdown permettent decrire du texte in the page web
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
