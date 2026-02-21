from fastapi import FastAPI
from car.car_controller import router as car_router

app = FastAPI()

app.include_router(car_router)