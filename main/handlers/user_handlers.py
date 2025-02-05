from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import main.keyboards.user_keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply('*main page*', reply_markup=kb.main)

@router.callback_query(F.data == 'mainpage')
async def main_page(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text='*main page*', reply_markup=kb.main)

# callback-handlers for 'main' keyboard
@router.callback_query(F.data == 'connection')
async def connection(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text='Доступные соединения:', reply_markup=await kb.inline_connections())

@router.callback_query(F.data == 'payment')
async def payment(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text='Доступные регионы:', reply_markup=kb.main)

@router.callback_query(F.data == 'settings')
async def settings(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text='Настройки', reply_markup=kb.main)

@router.callback_query(F.data == 'status')
async def status(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text='*connection status - etc.*', reply_markup=kb.main)
    