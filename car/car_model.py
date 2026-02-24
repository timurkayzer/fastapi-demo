from pydantic import BaseModel

class CarBase(BaseModel):
    make: str
    model: str
    year: int
    color: str

class Car(CarBase):
    id: int