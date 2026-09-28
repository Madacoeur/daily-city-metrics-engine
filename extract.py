import requests
import pandas as pd

def get_weather():
    #URL adress with which we extract the actual weather in Paris
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&current_weather=true"
    response = requests.get(url)
    #security: we check if the API answered right (code 200)
    response.raise_for_status()
    #Converting the response into JSON format
    data = response.json()
    temperature = data['current_weather']['temperature']
    print(f"Test Meteo : Il fait actuellement {temperature}°C à Paris.")

    return temperature

def get_stations():
    url = "https://api.citybik.es/v2/networks/velib"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    #Isolating the list of stations
    stations = data['network']['stations']
    
    print(f"Succes : {len(stations)} stations Velib 'recuperees!")
    print("\nApercu de la premiere station (index 0) :")
    print(stations[0])

    return stations

def transform_data(stations, temperature):
    #Converting the dictionary into a Pandas Array(DataFrame)
    df = pd.DataFrame(stations)

    #Filtration : Only keeping the useful colons for our dashboard
    colonnes_utiles = ['name', 'free_bikes', 'empty_slots', 'latitude', 'longitude', 'timestamp']
    df_clean = df[colonnes_utiles].copy()
    #adding an extra colon for the weather
    df_clean['temperature'] = temperature
    print("\nApercu du DataFrame apres nettoyage :")

    #.head() allows to only read the 5 first lines
    print(df_clean.head())

    return df_clean

if __name__ == "__main__":
    print("---1.EXTRACTION ---")
    temperature = get_weather()
    stations_data = get_stations()

    print("\n--- 2.TRANSFORMATION---")
    df_cleaned = transform_data(stations_data, temperature)
