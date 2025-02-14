import requests
import time

while True:
    try:
        response = requests.get("http://producer:5000")
        if response.status_code == 200:
            log = response.json().get("log")
            print(f"Received: {log}", flush=True)  # Ensure immediate printing
            with open("/data/logs.txt", "a") as file:
                file.write(log + "\n")
        else:
            print("Failed to fetch data", flush=True)
    except Exception as e:
        print(f"Error: {e}", flush=True)
    
    time.sleep(3)
