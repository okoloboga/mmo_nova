import logging

from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, Select
from fluentogram import TranslatorRunner

from states import StatsSG


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
    await callback.answer()


# Processing press Weapon Selecter
async def select_weapon(callback: CallbackQuery,
                        widget: Select,
                        dialog_manager: DialogManager,
                        weapon: str):
    await callback.answer()

