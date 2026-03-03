from db.engine import session
from car.car_model import CarModel


class CarService:
    async def get_by_id(self, car_id):
        return await session.query(CarModel).filter_by(id=car_id).first()

    async def get_all(self):
        return await session.query(CarModel).all()
    
    async def create(self, car_data):
        new_car = CarModel(**car_data)
        session.add(new_car)
        await session.commit()
        return new_car
    
    async def update(self, car_id, car_data):
        car = await self.get_by_id(car_id)
        if not car:
            return None
        for key, value in car_data.items():
            setattr(car, key, value)
        await session.commit()
        return car
    
    async def delete(self, car_id):
        car = await self.get_by_id(car_id)
        if not car:
            return False
        session.delete(car)
        session.commit()
        return True
    

car_service = CarService()