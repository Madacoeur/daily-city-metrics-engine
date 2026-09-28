import requests

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
if __name__ == "__main__":
    temperature = get_weather()
    stations_data = get_stations()
