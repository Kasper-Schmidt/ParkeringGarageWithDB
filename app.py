import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from database import (
create_database,
create_car_in_database,
get_all_cars_in_database,
remove_car_from_database,
)

app = FastAPI(
    title="Parkering system",
    description="Her kan man parkere og fjerne sin bil fra systemet igen"
)

create_database()

class CarCreate(BaseModel):
    plate: str



@app.get("/")
def home():
    return {
        "message": "Parkering System kører",
        "docs": "/docs"
    }



@app.post("/cars", status_code=201)
def create_car(car: CarCreate):

    try:
        create_car_in_database(car.plate)

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail=f"En bil med nummerplade {car.plate} findes allerede"
        )

    return {
        "message": f"Bilen med nummerplade {car.plate} er parkeret nu"
    }



@app.get("/cars")
def get_all_cars():
    return get_all_cars_in_database()



@app.delete("/cars/{plate}")
def remove_car(plate: str):

    deleted = remove_car_from_database(plate)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Bilen blev ikke fundet i databasen"
        )
    
    return {
        "message": f"Bilen med nummerplade {plate} er fjernet fra parkeringen"
    }