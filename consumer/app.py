import requests
import time

while True:
    try:
        response = requests.get("http://producer:5000/data")
        if response.status_code == 200:
            log = response.json().get("log")
            print(f"Received: {log}")
            
            # Store data in a shared volume
            with open("/data/logs.txt", "a") as file:
                file.write(log + "\n")
        else:
            print("Failed to fetch data")

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(3)  # Fetch new data every 3 seconds
