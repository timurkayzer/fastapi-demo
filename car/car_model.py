from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from .car_interfaces import CarBase

class Base (DeclarativeBase):
    pass

class CarModel(Base, CarBase):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    make: Mapped[str] = mapped_column()
    model: Mapped[str] = mapped_column()
    year: Mapped[int] = mapped_column()
    color: Mapped[str] = mapped_column()