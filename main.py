import requests
import folium

overpass_url = "http://overpass-api.de/api/interpreter"
overpass_query = """
[out:json];
area[name="Roma"][boundary="administrative"][admin_level=8];
(node["amenity"="drinking_water"](area);
 );
out center;
"""

response = requests.get(overpass_url, params={'data': overpass_query})
data = response.json()
coords = []

for element in data['elements']:
  if element['type'] == 'node':
    lon = element['lon']
    lat = element['lat']
    coords.append((lon, lat))
print(coords)
d = dict(coords)
print(d)

map = folium.Map(location=[41.9260, 12.4686], zoom_start = 13,   tiles = "Stamen Toner")
for k, v in d.items():
    folium.Marker(location=[v, k], popup= "Aqua Potabile", icon=folium.Icon(color = 'gray')).add_to(map)
map.save("map1.html")