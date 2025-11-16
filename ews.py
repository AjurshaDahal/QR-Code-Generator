import requests
import time
from datetime import datetime

# --- Configuration ---
API_KEY = "ad317ca7c341429488c123408252409"  # ← your WeatherAPI key
LOCATION = "Kathmandu"
THRESHOLD_RAIN_MM = 1.00          # mm of rain in past hour to trigger warning
CHECK_INTERVAL = 10 * 60          # check every 10 minutes (in seconds)

def get_weather():
    """
    Fetch weather data from WeatherAPI for the specified location.
    Returns precipitation in mm (past hour).
    """
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={LOCATION}&aqi=no"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    # “precip_mm” gives precipitation in millimeters
    return data.get("current", {}).get("precip_mm", 0.0)

def send_alert(precip_mm):
    """
    Send an alert. Here we just print to console,
    but you can extend this to email, SMS, etc.
    """
    print(f"[ALERT {datetime.now():%Y-%m-%d %H:%M:%S}] "
          f"Precipitation = {precip_mm} mm — exceeds threshold {THRESHOLD_RAIN_MM} mm!")

def monitor():
    print("Starting weather-based Early Warning Monitor...")
    while True:
        try:
            precip = get_weather()
            print(f"{datetime.now():%H:%M:%S} | Precipitation (past hour): {precip} mm")
            if precip >= THRESHOLD_RAIN_MM:
                send_alert(precip)
        except Exception as e:
            print(f"Error fetching weather data: {e}")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor()
