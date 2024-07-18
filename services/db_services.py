import asyncio
import logging

from sqlalchemy.ext.asyncio import async_sessionmaker
from database import User
from .constants import *

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
    user = User(telegram_id=telegram_id,
                first_name=first_name,
                last_name=last_name,
                location=BASE,
                health=100,
                bioresourse=0,
                crystals=0,
                equipment=START_EQUIPMENT
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
