import logging

from aiogram_dialog import DialogManager
from aiogram.types import User
from fluentogram import TranslatorRunner

from sqlalchemy.ext.asyncio import AsyncSession

from services import get_user, create_user
from services.constants import *

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
           '[%(asctime)s] - %(name)s - %(message)s')


# Starts from here, if not new user
async def main_getter(dialog_manager: DialogManager,
                      session: AsyncSession,
                      i18n: TranslatorRunner,
                      event_from_user: User,
                      **kwargs) -> dict:

    user = await get_user(session, 
                          event_from_user.id)
    if user.location == BASE or user.location == FIELDS:
        location = i18n.current.location(location=user.location)
    elif user.location == IN_TRANSIT:
        location = i18n.location.intransit(destination=user.location)
    
    return {
            'current_location': location,
            'button_stats': i18n.button.stats(),
            'button_bag': i18n.button.bag(),
            'button_location': i18n.button.location()
            }
