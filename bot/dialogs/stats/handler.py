import logging

from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, Select
from fluentogram import TranslatorRunner

from states import StatsSG
from services import unequip_to_bag

stats_router = Router()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format='%(filename)s:%(lineno)d #%(levelname)-8s '
                           '[%(asctime)s] - %(name)s - %(message)s')


# Process pressing Armor button to get stats
async def stats_armor(callback: CallbackQuery,
                      button: Button,
                      dialog_manager: DialogManager):

    user_id = callback.from_user.id
    logger.info(f'User {user_id} getting Armor stats')

    await dialog_manager.switch_to(StatsSG.armor)


# Process pressing Weapon button to get stats
async def stats_weapon(callback: CallbackQuery,
                       button: Button,
                       dialog_manager: DialogManager):

    user_id = callback.from_user.id
    logger.info(f'User {user_id} getting Weapon stats')

    await dialog_manager.switch_to(StatsSG.weapon)


# Processing press Armor Selecter
async def select_armor(callback: CallbackQuery,
                       widget: Select,
                       dialog_manager: DialogManager,
                       armor: str):

    user_id = callback.from_user.id
    logger.info(f'User {user_id} getting {armor} details')
    dialog_manager.current_context().dialog_data['selected_item'] = armor

    await dialog_manager.switch_to(StatsSG.details)


# Processing press Weapon Selecter
async def select_weapon(callback: CallbackQuery,
                        widget: Select,
                        dialog_manager: DialogManager,
                        weapon: str):

    user_id = callback.from_user.id
    logger.info(f'User {user_id} getting {weapon} details')
    dialog_manager.current_context().dialog_data['selected_item'] = weapon

    await dialog_manager.switch_to(StatsSG.details)


# Unequip item to Bag
async def unequip(callback: CallbackQuery,
                  button: Button,
                  dialog_manager: DialogManager):
    
    user_id = callback.from_user.id
    item = dialog_manager.current_context().dialog_data['selected_item']
    equipment = dialog_manager.current_context().dialog_data['equipment']
    session = dialog_manager.middleware_data.get('session')
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    
    logger.info(f'User {user_id} want to unequip his {item}')
    result = await unequip_to_bag(session, equipment, item, user_id, i18n)

    await callback.message.answer(text=result)

    

























