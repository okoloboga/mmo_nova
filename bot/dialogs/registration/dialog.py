from aiogram.types import ContentType

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.kbd import Button, Row

from .getter import *
from .handler import *
from states import RegistrationSG


'''Registration of new player'''
registration_dialog = Dialog(
    Window(
        Format('{start_speech}'),
        Button(Format('{button_next}'), id='b_next', on_click=registration),
        getter=registration_getter,
        state=RegistrationSG.speech_a
        ),
    Window(
        Format('{start_speech}'),
        Button(Format('{button_next}'), id='b_next', on_click=registration),
        getter=registration_getter,
        state=RegistrationSG.speech_b
        ) 
)
