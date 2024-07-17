from aiogram.fsm.state import State, StatesGroup

class RegistrationSG(StatesGroup):
    speech_a = State()
    speech_b = State()

class MainSG(StatesGroup):
    main = State()
