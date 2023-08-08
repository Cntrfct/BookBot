from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon import LEXICON
from services import book


def create_bookmarks_keyboard(*args: int) -> InlineKeyboardMarkup:
    # создаем объект клавиатуры
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # наполняем клавиатуру кнопками-закладками в порядке возрастания
    for button in sorted(args):
        kb_builder.row(InlineKeyboardButton(
            text=f'{button} - {book[button][:100]}',
            callback_data=str(button)))
    # добавляем в клавиатуру в конце две кнопки "Редактировать" и "Отменить"
    kb_builder.row(InlineKeyboardButton(
        text=LEXICON['edit_bookmarks_button'],
        callback_data='edit_bookmarks'),
        InlineKeyboardButton(
            text=LEXICON['cancel'],
            callback_data='cancel'),
        width=2)
    return kb_builder.as_markup()

def create_edit_keyboard(*args: int) -> InlineKeyboardMarkup:
    # создаем объект клавиатуры
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # наполняем клавиатуру кнопками-закладками в порядке возрастания
    for button in sorted(args):
        kb_builder.row(InlineKeyboardButton(
            text=f'{LEXICON["del"]} {button} - {book[button][:100]}',
            callback_data=f'{button}del'))
    # добавляем в конец клавиатры кнопку "Отменить"
    kb_builder.row(InlineKeyboardButton(
            text=LEXICON['cancel'],
            callback_data='cancel'))
    return kb_builder.as_markup()
