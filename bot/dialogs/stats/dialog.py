import logging

from aiogram import Router
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.kbd import Button, Row, Group, Select

from .handler import *
from .getter import *
from states import StatsSG
from dialogs.buttons import back


logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
           '[%(asctime)s] - %(name)s - %(message)s')


# Statistics of Character, items
stats_dialog = Dialog(
    Window(
        Format('{characters_stats}'),
        Row(
            Button(Format('{button_armor}'), id='b_stats_armor', on_click=stats_armor),
            Button(Format('{button_weapon}'), id='b_stats_weapon', on_click=stats_weapon)
            ),
        Button(Format('{button_back}'), id='b_back', on_click=back),
        getter=character_stats_getter,
        state=StatsSG.main
        ),
    Window(
        Format('{characters_armor}'),
        Group(
            # [Armor name] [Armor stats]
            Select(
                Format('{item}'),
                id='armor',
                item_id_getter=lambda x: x[0],
                items='armor_list',
                on_click=select_armor
                ),
            width=2
            ),
        Button(Format('{button_back}'), id='b_back', on_click=back),
        getter=character_armor_getter,
        state=StatsSG.armor
        ),
    Window(
        Format('{characters_weapon}'),
        Group(
            # [Weapon name] [Weapon stats]
            Select(
                Format('{item}'),
                id='weapon',
                item_id_getter=lambda x: x[0],
                items='weapon_list',
                on_click=select_weapon
                ),
            width=2
            ),
        Button(Format('{button_back}'), id='b_back', on_click=back),
        getter=character_weapon_getter,
        state=StatsSG.weapon
    )
)
