import asyncio
import logging

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.dialects.postgresql import insert
from database import User, Equipment
from .constants import *
from .classes import ItemEquipment

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
           '[%(asctime)s] - %(name)s - %(message)s')


# Add New User to Database
async def create_user(session: AsyncSession,
                      telegram_id: int,
                      first_name: str,
                      last_name: str | None = None
                      ):
    user = insert(User).values(
            {
                'telegram_id': telegram_id,
                'first_name': first_name,
                'last_name': last_name,
                'location': BASE,
                'health': 100,
                'bioresource': 0,
                'crystals': 0,
                'equipment': START_EQUIPMENT
                }    
            )

    await session.execute(user)
    await session.commit()
    logger.info(f'New user created {user}')
    

# Read User data from Database
async def get_user(session: AsyncSession,
                   telegram_id: int
                   ) -> User | None:
    
    user = await session.get(
            User, {'telegram_id': telegram_id}
            )
    logger.info(f'User from database {user}')
    
    return user


# Add item of equipment to Database
async def create_equipment(sessionmaker: async_sessionmaker,
                           item: dict
                           ):
   
    equipment = Equipment(**item)

    async with sessionmaker() as session:
        session.add(equipment)
        await session.commit()
    logger.info(f'Added new equipment to Database: {equipment}')
    
        
# Getting Equipment from database by Item ID and wrapping to Equipment Class
async def get_equipment(session: AsyncSession,
                        item_id: int,
                        health_current: int,
                        ) -> Equipment | None:
    logger.info(f'Gettin item with id {item_id}')  
    result = await session.get(
                   Equipment, {'item_id': int(item_id)}
                   )
    logger.info(f'EquipmentItem from Database {result}')
    
    if result is not None:
        item = ItemEquipment(item_id = result.item_id,
                             item_type = result.item_type,
                             name = result.name,
                             effect = result.effect,
                             health_max = result.health_max,
                             bio_cost = result.bio_cost,    
                             health_current = int(result.health_max * health_current),
                             repair_weak = result.repair_weak,                  
                             repair_strong = result.repair_strong,              
                             cost_repair_weak = result.cost_repair_weak,        
                             cost_repair_strong = result.cost_repair_strong,    
                             description = result.description 
                             )
        return item
    else:
        return None
    
    
    
    
