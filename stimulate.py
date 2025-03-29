import requests
import random
import time

vehicle_ids = ["V001", "V002", "V003"]  # Vehicle IDs

while True:
    for vehicle in vehicle_ids:
        latitude = random.uniform(18.5, 19.5)  # Random latitude
        longitude = random.uniform(73.5, 74.5)  # Random longitude

        data = {"vehicle_id": vehicle, "latitude": latitude, "longitude": longitude}

        response = requests.post("http://127.0.0.1:5000/update_location", json=data)
        print(response.json())

    time.sleep(5)  # Updates every 5 seconds
