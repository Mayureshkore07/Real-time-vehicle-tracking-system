import sqlite3

def setup_database():
    conn = sqlite3.connect('vehicle_tracking.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS vehicles (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        vehicle_id TEXT,
                        latitude REAL,
                        longitude REAL,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                    )''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    print("Database created successfully.")
