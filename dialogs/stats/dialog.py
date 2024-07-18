import logging

from aiogram import Router
from aiogram.utils.deep_linking import decode_payload
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from sqlalchemy.ext.asyncio import async_sessionmaker

from states import StatsSG

stats_router = Router()

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
           '[%(asctime)s] - %(name)s - %(message)s')

# Statistics of Character, items
stats_dialog = Dialog(
    Window(
        Format('{character_stats}'),
        Row(
            Button(Format('{button_armor}'), id='b_stats_armor', on_click=stats_armor),
            Button(Format('{button_weapon}'), id='b_stats_weapon', on_click=stats_weapon)
            ),
        Button(Format('{button_back}'), id='b_back', on_click=back),
        getter=character_stats_getter,
        state=StatsSG.main
        ),
    Window(

        )
    )
