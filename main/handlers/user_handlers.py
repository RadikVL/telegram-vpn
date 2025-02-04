from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import main.keyboards.user_keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply('main page', reply_markup=kb.main)

@router.callback_query(F.data == 'mainpage')
async def main_page(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(text='main page', reply_markup=kb.main)

@router.callback_query(F.data == 'connection')
async def connection(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('info', reply_markup=await kb.inline_connections())