import requests



url = 'http://localhost:8686/predict'



data = {"monsoonintensity": 7.0, "topographydrainage": 2.0, 
        "rivermanagement": 5.0, "climatechange": 7.0, 
        "encroachments": 9.0, "coastalvulnerability": 7.0, 
        "landslides": 8.0, "populationscore": 3.0, "wetlandloss": 8.0, 
        "human_activities": 7.0, "societal_vulnerability": 1.6,
        "water_infrastructure": 11.3}


response = requests.post(url, json=data).json()
print(response)

