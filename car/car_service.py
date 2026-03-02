from db.engine import session
from car.car_model import Car


class CarService:
    def get_by_id(self, car_id):
        return session.query(Car).filter_by(id=car_id).first()

    def get_all(self):
        return session.query(Car).all()
    
    def create(self, car_data):
        new_car = Car(**car_data)
        session.add(new_car)
        session.commit()
        return new_car
    
    def update(self, car_id, car_data):
        car = session.query(Car).filter_by(id=car_id).first()
        if not car:
            return None
        for key, value in car_data.items():
            setattr(car, key, value)
        session.commit()
        return car
    
    def delete(self, car_id):
        car = session.query(Car).filter_by(id=car_id).first()
        if not car:
            return False
        session.delete(car)
        session.commit()
        return True
    