# 🚴‍♂️🌤️ Urban Data Pipeline : ETL automatisé Météo & Mobilité

## Description
Ce projet est un pipeline de données complet (ETL) conçu pour extraire, transformer et stocker quotidiennement les données d'infrastructures urbaines (stations de vélos Vélib') croisées avec les conditions météorologiques. 

L'objectif est de démontrer la maîtrise des concepts fondamentaux du Data Engineering à travers une architecture simple, robuste et automatisée.

## 🛠️ Stack Technique
* **Extraction (Extract) :** Python (`requests`) via requêtes d'APIs REST publiques (Open-Meteo & CityBikes).
* **Transformation (Transform) :** Nettoyage, typage et structuration des données JSON brutes via Python (`pandas`).
* **Stockage (Load) :** Insertion des données propres dans une base de données relationnelle locale **SQLite**.
* **Restitution :** Dashboard interactif développé avec **Streamlit**.

## 🚀 Comment lancer le projet en local

### 1. Cloner le dépôt et préparer l'environnement
```bash
# Créer un environnement virtuel
python -m venv env

# Activer l'environnement (Windows)
env\Scripts\activate
# OU Activer l'environnement (Mac/Linux)
source env/bin/activate

# Installer les dépendances
pip install -r requirements.txt
