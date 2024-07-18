import asyncio

from sqlalchemy import BigInteger, DateTime, Text, func
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from config import get_config, DbConfig, Config, load_config

from .db_services import create_equipment
from .objects import total_dict


async def main():
    
    # Config
    db_config = get_config(DbConfig, "db")

    engine = create_async_engine(
        url=str(db_config.dsn),
        echo=False
    )
    Sessionmaker = async_sessionmaker(engine, expire_on_commit=False)

    for value in total_dict.values(): 
        ''' 
        await create_equipment(sessionmaker=Sessionmaker,
                               item_id=value['item_id'],
                               item_type=value['item_type'],
                               name=value['name'],
                               effect=value['effect'],
                               health_max=value['health_max'],
                               bio_cost=value['bio_cost'],
                               repair_weak=value['repair_weak'],
                               repair_strong=value['repair_strong'],
                               cost_repair_weak=value['cost_repair_weak'],
                               cost_repair_strong=value['cost_repair_strong'],
                               description=value['description'])
        '''
        await create_equipment(sessionmaker=Sessionmaker, **value)

if __name__ == '__main__':
    asyncio.run(main())