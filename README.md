# 🚴‍♂️🌤️ Urban Data Pipeline : ETL automatisé Météo & Mobilité

## Description
Ce projet est un pipeline de données complet (ETL) conçu pour extraire, transformer et stocker quotidiennement les données d'infrastructures urbaines (stations de vélos Vélib') croisées avec les conditions météorologiques. 

L'objectif est de démontrer la maîtrise des concepts fondamentaux du Data Engineering à travers une architecture simple, robuste et automatisée.

## 🛠️ Stack Technique
* **Extraction (Extract) :** Python (`requests`) via requêtes d'APIs REST publiques (Open-Meteo & CityBikes).
* **Transformation (Transform) :** Nettoyage, typage et structuration des données JSON brutes via Python (`pandas`).
* **Stockage (Load) :** Insertion des données propres dans une base de données relationnelle locale **SQLite**.
* **Restitution :** Dashboard interactif développé avec **Streamlit**.
* **Automatisation :** Planification via `cron` (toutes les 15 minutes).

## 🚀 Installation et Utilisation

### 1. Prérequis
Assurez-vous d'avoir Python 3 et Git installés sur votre machine. Clonez ce dépôt puis placez-vous dans le dossier du projet :
```bash
git clone git@github.com:Madacoeur/daily-city-metrics-engine.git
cd VelibProject
```

### 2. Créer l'environnement virtuel
Il est fortement recommandé d'isoler les dépendances du projet :
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Lancer l'extraction de données (ETL)
Pour générer la base de données locale et y insérer les premières données :
```bash
python3 extract.py
```

### 5. Démarrer le Dashboard web
Lancez l'interface Streamlit pour visualiser les données et la carte interactive :
```bash
streamlit run app.py
```
L'application s'ouvrira automatiquement dans votre navigateur local.

## 📂 Structure du projet
* `extract.py` : Script ETL principal (Extraction, Transformation, Chargement).
* `app.py` : Application web Streamlit (Visualisation).
* `requirements.txt` : Liste des dépendances Python nécessaires.
* `.gitignore` : Règles d'exclusion pour le dépôt Git.
