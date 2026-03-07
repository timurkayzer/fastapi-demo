from fastapi import APIRouter, HTTPException
from .car_model import CarBase
from .car_service import car_service

router = APIRouter(prefix="/car", tags=["car"])

@router.get("/")
async def get_car():
    # For demonstration, we will return a dummy car. In a real application, you would fetch this from a database.
    return car_service.get_all()

@router.get("/{car_id}")
async def get_car(car_id: int):
    # For demonstration, we will return a dummy car. In a real application, you would fetch this from a database.
    car = await car_service.get_by_id(car_id)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    else:
        return car
    
@router.post("/")
async def create_car(car: CarBase):
    # In a real application, you would save the car to a database and return the saved object.
    return car_service.create(car)