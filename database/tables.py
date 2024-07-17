from typing import Annotated
from datetime import datetime

from sqlalchemy import BigInteger, String, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# Define types
tg_id = Annotated[int, mapped_column(BigInteger, primary_key=True)]
required_short_str = Annotated[str, mapped_column(String(15), nullable=False)]
optional_str = Annotated[str | None, mapped_column(String, nullable=True)]


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    telegram_id: Mapped[tg_id]
    first_name: Mapped[required_short_str]
    last_name: Mapped[optional_str]
    location: Mapped[required_short_str]
    destination: Mapped[optional_str]
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

