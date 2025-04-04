import json
import tkinter as tk
from tkinter import messagebox, ttk
from geopy.distance import geodesic
import time
import folium
from io import BytesIO
from PIL import ImageTk, Image
import os

# Predefined station coordinates (latitude, longitude)
stations = {
    "Jaysingpur": (16.7764, 74.5545),
    "Sangli": (16.8524, 74.5815),
    "Pune": (18.5204, 73.8567),
    "Mumbai": (19.0760, 72.8777),
    "Bangalore": (12.9716, 77.5946)
}

# Average bus speed (km/h)
bus_speed = 40

# Route history storage file
history_file = "route_history.json"

# Function to calculate travel time
def calculate_travel_time():
    source = entry_source.get()
    destination = entry_destination.get()

    # Check if stations are valid
    if source not in stations or destination not in stations:
        messagebox.showerror("Error", "Invalid station names!")
        return

    # Get the coordinates of the stations
    source_coords = stations[source]
    destination_coords = stations[destination]

    # Calculate estimated travel time
    estimated_time = get_travel_time(source_coords, destination_coords)

    if estimated_time:
        label_result.config(text=f"Estimated Time: {estimated_time} minutes")
        save_route_history(source, destination, estimated_time)
        show_map(source_coords, destination_coords)
        simulate_live_tracking(source, destination, estimated_time)
    else:
        messagebox.showerror("Error", "Unable to calculate time.")

# Calculate the travel time
def get_travel_time(source_coords, destination_coords):
    distance = geodesic(source_coords, destination_coords).km
    time_in_hours = distance / bus_speed
    time_in_minutes = time_in_hours * 60

    return round(time_in_minutes, 2)

# Save route history
def save_route_history(source, destination, estimated_time):
    data = {"source": source, "destination": destination, "estimated_time": estimated_time, "timestamp": time.time()}
    try:
        with open(history_file, "r") as file:
            history = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        history = []
    history.append(data)
    with open(history_file, "w") as file:
        json.dump(history, file, indent=4)

# Simulate live bus tracking without GPS
def simulate_live_tracking(source, destination, estimated_time):
    for i in range(1, 11):  # Simulating 10 steps of the journey
        progress = (i / 10) * 100
        label_live_tracking.config(text=f"Bus is {progress:.1f}% of the way from {source} to {destination}")
        root.update()
        time.sleep(estimated_time / 10)
    label_live_tracking.config(text=f"Bus has arrived at {destination}!")

# Show the route on a map using folium
def show_map(source_coords, destination_coords):
    # Create a map centered around the midpoint
    map_center = [(source_coords[0] + destination_coords[0]) / 2, (source_coords[1] + destination_coords[1]) / 2]
    bus_map = folium.Map(location=map_center, zoom_start=10)

    # Add markers for source and destination
    folium.Marker(source_coords, popup="Source").add_to(bus_map)
    folium.Marker(destination_coords, popup="Destination").add_to(bus_map)

    # Plot the route between source and destination
    folium.PolyLine([source_coords, destination_coords], color="blue", weight=2.5, opacity=1).add_to(bus_map)

    # Save the map to an HTML file
    map_filename = "bus_route_map.html"
    bus_map.save(map_filename)

    # Open the map in a browser
    os.system(f"start {map_filename}")

# Set up the Tkinter window
root = tk.Tk()
root.title("Bus Time Estimator")

# Add labels and input fields for source station
label_source = tk.Label(root, text="Source Station:")
label_source.pack()
entry_source = ttk.Combobox(root, values=list(stations.keys()))
entry_source.pack()

# Add labels and input fields for destination station
label_destination = tk.Label(root, text="Destination Station:")
label_destination.pack()
entry_destination = ttk.Combobox(root, values=list(stations.keys()))
entry_destination.pack()

# Button to calculate the travel time
button_estimate = tk.Button(root, text="Estimate Travel Time", command=calculate_travel_time)
button_estimate.pack()

# Label to display the result
label_result = tk.Label(root, text="")
label_result.pack()

# Live tracking status label
label_live_tracking = tk.Label(root, text="")
label_live_tracking.pack()

# Run the application
root.mainloop()
