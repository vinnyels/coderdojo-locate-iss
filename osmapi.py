import requests

def reverse_geocode(lat, lon):
    """Convert coordinates to location information"""
    url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        'lat': lat,
        'lon': lon,
        'format': 'json',
        'addressdetails': 1  # Get detailed address components
    }
    headers = {
        'User-Agent': 'YourAppName/1.0 (your.email@example.com)'  # Required!
    }
    
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    
    if data and 'address' in data:
        address = data['address']
        return {
            'country': address.get('country'),
            'city': address.get('city') or address.get('town') or address.get('village'),
            'state': address.get('state'),
            'display_name': data.get('display_name')
        }
    return None

# Example usage
location = reverse_geocode(48.8584, 2.2945)  # Eiffel Tower
if location:
    print(f"Country: {location['country']}")
    print(f"City: {location['city']}")
