import phonenumbers
from myPhone import number 
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

# Parse number
pepnumber = phonenumbers.parse(number, "IN")

# Get location name (e.g., "Maharashtra")
location_en = geocoder.description_for_number(pepnumber, "en")
location_hi = geocoder.description_for_number(pepnumber, "hi")
print("Location (English):", location_en)
print("स्थान (Hindi):", location_hi)

# Get carrier name
service_provider = carrier.name_for_number(pepnumber, "en")
print("Carrier:", service_provider)

# Geocode that location (add 'India' for context)
key = '5e8ff7e4fa184724a44b9139034a5990'
geo = OpenCageGeocode(key)
query = f"{location_en}, India"
print("Geocoding query:", query)

results = geo.geocode(query)

if results and len(results):
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(f"Coordinates: {lat}, {lng}")

    myMap = folium.Map(location=[lat, lng], zoom_start=8)
    folium.Marker([lat, lng], popup=location_en).add_to(myMap)

    myMap.save("Python Projects\\Project_4\\Track Location\\myLocation.html")
    print("Map saved successfully!")
else:
    print("Could not geocode the location.")
