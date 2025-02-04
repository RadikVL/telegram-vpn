from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import (InlineKeyboardBuilder, ReplyKeyboardBuilder)

# main = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Соединения')],
#     [KeyboardButton(text='Купить'), KeyboardButton(text='Настройки')],
#     [KeyboardButton(text='Обновить Статус')]
# ],
#     resize_keyboard=True
# )

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Соединения', callback_data='connection')],
    [InlineKeyboardButton(text='Купить', callback_data='payment'), InlineKeyboardButton(text='Настройки', callback_data='settings')],
    [InlineKeyboardButton(text='Обновить Статус', callback_data='status')]
])

conn = ['USA', 'UK', 'Russia', 'Словакия', 'Корея', 'Япония']
async def inline_connections():
    builder = InlineKeyboardBuilder()
    builder.add(*[InlineKeyboardButton(text=el, callback_data=f'conn_{el}') for el in conn])
    builder.adjust(2)
    builder.row(InlineKeyboardButton(text="🔙 На главную", callback_data="mainpage"))
    return builder.as_markup()
