from flask import Flask, request, jsonify, render_template
import sqlite3
import folium
from markupsafe import Markup


app = Flask(__name__)

# Function to insert vehicle location into database
def insert_location(vehicle_id, latitude, longitude):
    conn = sqlite3.connect('vehicle_tracking.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO vehicles (vehicle_id, latitude, longitude) VALUES (?, ?, ?)",
                   (vehicle_id, latitude, longitude))
    conn.commit()
    conn.close()

# API to receive vehicle location updates
@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.json
    vehicle_id = data.get("vehicle_id")
    latitude = data.get("latitude")
    longitude = data.get("longitude")

    if not (vehicle_id and latitude and longitude):
        return jsonify({"error": "Missing data"}), 400

    insert_location(vehicle_id, latitude, longitude)
    return jsonify({"message": "Location updated"}), 200

# Fetch latest vehicle locations
def get_vehicle_locations():
    conn = sqlite3.connect('vehicle_tracking.db')
    cursor = conn.cursor()
    cursor.execute("SELECT vehicle_id, latitude, longitude FROM vehicles ORDER BY timestamp DESC")
    vehicles = cursor.fetchall()
    conn.close()
    return vehicles

# Generate live map
@app.route('/')
def index():
    vehicles = get_vehicle_locations()
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)  # Centered in India

    for vehicle in vehicles:
        folium.Marker(location=[vehicle[1], vehicle[2]], popup=f"Vehicle {vehicle[0]}").add_to(m)

    return Markup(m._repr_html_())

if __name__ == '__main__':
    app.run(debug=True, port=5001)
    
@app.route('/')
def home():
    return "Flask is working! 🚀"



