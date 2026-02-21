from fastapi import APIRouter, HTTPException
from .car_model import Car

router = APIRouter(prefix="/car", tags=["car"])

@router.get("/{car_id}", response_model=Car)
async def get_car(car_id: int):
    # For demonstration, we will return a dummy car. In a real application, you would fetch this from a database.
    if car_id == 1:
        return Car(id=1, make="Toyota", model="Corolla", year=2020, color="Blue")
    else:
        raise HTTPException(status_code=404, detail="Car not found")
    
@router.post("/", response_model=Car)
async def create_car(car: Car):
    # In a real application, you would save the car to a database and return the saved object.
    return car