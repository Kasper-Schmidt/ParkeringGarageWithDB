import sqlite3

DATABASE_NAME = "ParkingGarage.db"

def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection

def create_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS parked_cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plate TEXT NOT NULL UNIQUE,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP         
        )                     
    """)

    connection.commit()
    connection.close()


def create_car_in_database(plate):
    connection = get_connection()

    connection.execute("""
        INSERT INTO parked_cars (plate)
        VALUES (?)                         
    """, (plate,))

    connection.commit()
    connection.close()


def get_all_cars_in_database():
    connection = get_connection()

    cars = connection.execute("""
        SELECT * 
        FROM parked_cars
        ORDER BY created_at                          
    """).fetchall()

    connection.close()

    return [dict(car) for car in cars]


def remove_car_from_database(plate):
    connection = get_connection()

    cursor = connection.execute("""
        DELETE FROM parked_cars
        WHERE plate = ?                   
    """, (plate,))

    connection.commit()
    connection.close()

    return cursor.rowcount > 0