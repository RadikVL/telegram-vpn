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
    [InlineKeyboardButton(text='Aктивные Соединения', callback_data='connection')],
    [InlineKeyboardButton(text='Купить VPN', callback_data='payment'), InlineKeyboardButton(text='Настройки', callback_data='settings')],
    [InlineKeyboardButton(text='Обновить Статус', callback_data='status')]
])

# user connections keyboard - доступные соединения - custom for each user
conn = ['USA', 'UK', 'Russia', 'Словакия', 'Корея', 'Япония']
async def user_avail_connections():
    builder = InlineKeyboardBuilder()
    builder.add(*[InlineKeyboardButton(text=el, callback_data=f'conn_{el}') for el in conn])
    builder.adjust(2)
    builder.row(InlineKeyboardButton(text="🔙 На главную", callback_data="mainpage"))
    return builder.as_markup()

# connections places - availiable to buy
conn = ['USA', 'UK', 'Russia', 'Словакия', 'Корея', 'Япония']
async def server_avail_connections():
    builder = InlineKeyboardBuilder()
    builder.add(*[InlineKeyboardButton(text=el, callback_data=f'conn_{el}') for el in conn])
    builder.adjust(2)
    builder.row(InlineKeyboardButton(text="🔙 На главную", callback_data="mainpage"))
    return builder.as_markup()

# settings keyboard
sett = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='settings page', callback_data='test_setting')],
    [InlineKeyboardButton(text='🔙 На главную', callback_data='mainpage')]
])