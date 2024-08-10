from typing import Annotated
from datetime import datetime

from sqlalchemy import BigInteger, String, DateTime, Integer, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# Define types
tg_id = Annotated[int, mapped_column(BigInteger, primary_key=True)]
item_id = Annotated[int, mapped_column(Integer, primary_key=True)]
optional_str = Annotated[str | None, mapped_column(String, nullable=True)]
required_int = Annotated[int, mapped_column(Integer, nullable=False)]
optional_int = Annotated[int | None, mapped_column(Integer, nullable=True)]
required_str = Annotated[str, mapped_column(String, nullable=False)]


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    telegram_id: Mapped[tg_id]
    first_name: Mapped[required_str]
    last_name: Mapped[optional_str]
    location: Mapped[required_str]
    destination: Mapped[optional_str]
    health: Mapped[required_int]
    bioresource: Mapped[required_int]
    crystals: Mapped[required_int]
    equipment: Mapped[required_str]
    bag: Mapped[required_str]
    created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            nullable=False,
            server_default=func.now()
            )
    
    def __repr__(self) -> str:
        if self.last_name is None:
            name = self.first_name
        else:
            name = f'{self.first_name} {self.last_name}'
        return f'[{self.telegram_id}] {name}'

    
class Equipment(Base):
    __tablename__ = 'equipment'
    
    item_id: Mapped[item_id]
    item_type: Mapped[required_str]
    name: Mapped[required_str]
    effect: Mapped[required_str]
    health_max: Mapped[required_int]
    bio_cost: Mapped[required_int]
    repair_weak: Mapped[required_int]
    repair_strong: Mapped[required_int]
    cost_repair_weak: Mapped[required_str]
    cost_repair_strong: Mapped[required_int]
    description: Mapped[required_str]
    
    def __repr__(self) -> str:
        return f'{self.item_type}{self.item_id}_{self.effect}'

