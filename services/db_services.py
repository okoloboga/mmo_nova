import asyncio
import logging

from sqlalchemy.ext.asyncio import async_sessionmaker
from database import User, Equipment
from .constants import *
from services import ItemEquipment

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
           '[%(asctime)s] - %(name)s - %(message)s')


# Add New User to Database
async def create_user(sessionmaker: async_sessionmaker,
                      telegram_id: int,
                      first_name: str,
                      last_name: str | None = None
                      ):
    user = User(telegram_id = telegram_id,
                first_name = first_name,
                last_name = last_name,
                location = BASE,
                health = 100,
                bioresourse = 0,
                crystals = 0,
                equipment = START_EQUIPMENT
                )
    
    async with sessionmaker() as session:
        session.add(user)
        await session.commit()
        logger.info(f'New user created {user}')
        

# Read User data from Database
async def get_user(sessionmaker: async_sessionmaker,
                   telegram_id: int
                   ) -> User | None:
    async with sessionmaker() as session:
        result = await session.get(User, telegram_id)
    
    logger.info(f'User from database {result}')
    
    return result


# Add item of equipment to Database
async def create_equipment(sessionmaker: async_sessionmaker,
                           item_id: int,
                           item_type: str,
                           name: str, 
                           effect: str, 
                           health_max: int,
                           bio_cost: int,
                           repair_weak: str,
                           repair_strong: int,
                           cost_repair_weak: str,
                           cost_repair_strong: int,
                           description: str
                           ):
    
    equipment = Equipment(item_id = item_id,                  
                          item_type = item_type,                      
                          name = name,                     
                          effect = effect,                                                                                
                          health_max = health_max,                    
                          bio_cost = bio_cost,                           
                          repair_weak = repair_weak,                  
                          repair_strong = repair_strong,              
                          cost_repair_weak = cost_repair_weak,        
                          cost_repair_strong = cost_repair_strong,    
                          description = description 
                          )
    
    async with sessionmaker() as session:
        session.add(equipment)
        await session.commit()
        logger.info(f'Added new equipment to Database: {user}')
        
        
# Getting Equipment from database by Item ID and wrapping to Equipment Class
async def get_equipment(sessionmaker: async_sessionmaker,
                        item_id: int,
                        health_current: int,
                        ) -> ItemEquipment | None:
    
    async with sessionmaker() as session:
        result = await session.get(Equipment, item_id)
        
    logger.info(f'EquipmentItem from Database {result}')
    
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

    
    
    
    
    
