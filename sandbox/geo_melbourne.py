import folium
import webbrowser

# Create a map centered on Melbourne
melbourne_map = folium.Map(location=[-37.8136, 144.9631], zoom_start=13)

# Add a marker for Melbourne
# folium.Marker([-37.8136, 144.9631], popup='Melbourne').add_to(melbourne_map)

# Melbourne CBD coordinates
cbd_latitude = -37.8136
cbd_longitude = 144.9631

# Locations and their coordinates
locations = [
    ("Parkville", -37.7840, 144.9472),
    ("Kensington", -37.7945, 144.9303),
    ("Carlton", -37.8002, 144.9669),
    ("Backlands", -37.8136, 144.9631),
    ("South Bank", -37.8216, 144.9646),
    ("Port Melbourne", -37.8341, 144.9381),
    ("South Yarra", -37.8375, 144.9934),
    ("Torah", -37.8149, 144.9632)
]

# Create a map centered around Melbourne CBD
m = folium.Map(location=[cbd_latitude, cbd_longitude], zoom_start=14)

# Add markers for each location
for location in locations:
    name, latitude, longitude = location
    folium.Marker(location=[latitude, longitude], popup=name).add_to(melbourne_map)

melbourne_map.save("melbourne_map.html")
#webbrowser.open("melbourne_map.html")