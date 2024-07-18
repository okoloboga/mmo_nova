from aiogram.fsm.state import State, StatesGroup

class RegistrationSG(StatesGroup):
    speech_a = State()
    speech_b = State()

class MainSG(StatesGroup):
    main = State()

class BagSG(StateGroup):
    main = State()

class LocationSG(StateGroup):
    main = State()

class StatsSG(StateGroup):
    main = State()
    armor = State()
    weapon = State()
