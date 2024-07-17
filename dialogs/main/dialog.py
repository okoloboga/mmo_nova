from aiogram.types import ContentType

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.kbd import Button, Row

from .getter import *
from .handler import *
from states import MainSG

main_dialog = Dialog(
    Window(
        Format('{current_location}'),
        Button(Format('{button_stats}'), id='b_stats', on_click=switch_to_stats),
        Row(
            Button(Format('{button_bag}'), id='b_bag', on_click=switch_to_bag),
            Button(Format('{button_location}'), id='b_location', on_click=switch_to_location)
        ),
        getter=main_getter,
        state=MainSG.main
    )
)