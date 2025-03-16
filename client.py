import requests
import webbrowser
import time

def listen_for_signal():
    while True:
        try:
            response = requests.get('https://my-website-opener.onrender.com/get_url')  # Замените на ваш Render URL
            if response.status_code == 200:
                data = response.json()
                url = data.get('url')
                if url:
                    print(f"Opening website: {url}")
                    webbrowser.open(url)
                else:
                    print("No URL received.")
            else:
                print(f"Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Connection error: {e}")
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    listen_for_signal()