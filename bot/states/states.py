from aiogram.fsm.state import State, StatesGroup

class RegistrationSG(StatesGroup):
    speech_a = State()
    speech_b = State()

class MainSG(StatesGroup):
    main = State()

class BagSG(StatesGroup):
    main = State()

class LocationSG(StatesGroup):
    main = State()

class StatsSG(StatesGroup):
    main = State()
    armor = State()
    weapon = State()
    details = State()
