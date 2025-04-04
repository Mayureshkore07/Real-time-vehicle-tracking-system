import folium

# Initialize a map centered around a station
map = folium.Map(location=[12.9716, 77.5946], zoom_start=13)

# Example bus stop locations (latitude, longitude)
bus_stops = {
    "Station A": [12.9716, 77.5946],
    "Station B": [12.9350, 77.6249],
}

# Adding markers for each bus stop
for station, coords in bus_stops.items():
    folium.Marker(coords, popup=station).add_to(map)

# Save the map as an HTML file
map.save("bus_map.html")
