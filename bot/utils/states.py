from aiogram.fsm.state import State, StatesGroup


class Algebra(StatesGroup):
    q1 = State()
    q2 = State()
    q3 = State()
    q4 = State()


class Geography(StatesGroup):
    im1 = State()
    im2 = State()
    im3 = State()
    im4 = State()


class Translate(StatesGroup):
    msg = State()