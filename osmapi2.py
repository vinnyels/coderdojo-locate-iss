import requests

def reverse_geocode_v2(lat, lon):
    url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        'lat': lat,
        'lon': lon,
        'format': 'json',
        'addressdetails': 1,
        'accept-language': 'en'  # Specify language
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
        'Accept': 'application/json'
    }
    
    response = requests.get(url, params=params, headers=headers, timeout=10)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# Test
result = reverse_geocode_v2(48.8584, 2.2945)
print(result)
