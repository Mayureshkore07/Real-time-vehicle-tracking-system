from geopy.distance import geodesic

# Sample station coordinates (latitude, longitude)
stations = {
    "Station A": (12.9716, 77.5946),
    "Station B": (12.9350, 77.6249),
    "Station C": (12.9141, 77.6232),
}

# Average bus speed (km/h)
bus_speed = 30

def calculate_travel_time(source, destination):
    if source not in stations or destination not in stations:
        return "Invalid stations!"

    # Get the coordinates for the stations
    source_coords = stations[source]
    destination_coords = stations[destination]

    # Calculate the distance between stations
    distance = geodesic(source_coords, destination_coords).km
    # Calculate the time in hours
    time_in_hours = distance / bus_speed
    # Convert time to minutes
    time_in_minutes = time_in_hours * 60

    return round(time_in_minutes, 2)

# Example usage
source = "Station A"
destination = "Station B"
estimated_time = calculate_travel_time(source, destination)
print(f"Estimated time: {estimated_time} minutes")
