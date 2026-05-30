import requests
import time
from datetime import datetime
from urllib.request import urlopen
import json

def get_iss_location():
    """Fetches the current location of the ISS from the wheretheiss.at API."""
    api_url = "http://api.open-notify.org/iss-now.json"

    print(f"Attempting to fetch ISS location from: {api_url}")
    try:
        # Make the GET request to the API
        response = requests.get(api_url)
        response.raise_for_status() # Raises HTTPError for bad responses (4xx or 5xx)

        # Parse the JSON response
        data = response.json()

        # Check if the API call was successful according to its own message
        if data.get("message") == "success":
            timestamp = data.get("timestamp")
            iss_position = data.get("iss_position", {})
            latitude = iss_position.get("latitude")
            longitude = iss_position.get("longitude")

            # Convert timestamp to a human-readable date and time
            dt_object = datetime.fromtimestamp(timestamp)

            print(f"\n--- ISS Location Data ---")
            print(f"Time (UTC): {dt_object}")
            print(f"Latitude: {latitude}°")
            print(f"Longitude: {longitude}°")
            print(f"Raw Timestamp: {timestamp}")
            print(f"Message: {data.get('message')}")

            return latitude, longitude, dt_object
        else:
            print(f"API returned an error message: {data.get('message')}")
            return None, None, None

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Status code: {response.status_code}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err} - Could not connect to the API.")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err} - The request took too long.")
    except requests.exceptions.RequestException as req_err:
        print(f"An unexpected error occurred: {req_err}")
    except ValueError:
        print("Error parsing JSON response. The API might have returned invalid data.")

    return None, None, None

if __name__ == "__main__":
    # Example of continuous tracking
    print("Starting real-time ISS tracking (Ctrl+C to stop)...")
    while True:
        lat, lon, time_str = get_iss_location()
        if lat is not None:
            print(f"Current ISS position: Lat {lat}, Lon {lon} at {time_str} UTC")
        else:
            print("Failed to retrieve ISS location.")

        # Wait for a few seconds before the next request to avoid excessive polling
        # and to give the ISS time to move noticeably.
        time.sleep(5) 
