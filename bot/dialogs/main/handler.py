import logging

from aiogram import Router
from aiogram.utils.deep_linking import decode_payload
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from states import LocationSG, BagSG, StatsSG

main_router = Router()

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
           '[%(asctime)s] - %(name)s - %(message)s')


# Switch to Characters stats
async def switch_to_stats(callback: CallbackQuery,
                          button: Button,
                          dialog_manager: DialogManager):
    logger.info(f'User {callback.from_user.id} switch to Stats')
    await dialog_manager.start(StatsSG.main)


# Switch to Characters Bag and Storage
async def switch_to_bag(callback: CallbackQuery,
                        button: Button,
                        dialog_manager: DialogManager):    
    logger.info(f'User {callback.from_user.id} switch to Bag')
    await dialog_manager.start(BagSG.main)


# Switch to Location observation
async def switch_to_location(callback: CallbackQuery,
                             button: Button,
                             dialog_manager: DialogManager):  
    logger.info(f'User {callback.from_user.id} switch to Location')
    await dialog_manager.start(LocationSG.main)
