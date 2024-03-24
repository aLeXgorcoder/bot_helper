from aiogram import F, Bot, Dispatcher
from aiogram import types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN = '6663686099:AAH5WU7TbjKzZT1mTojIjs703e9kclgQ4PU'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты'), KeyboardButton(text='Назад')]
], resize_keyboard=True, input_field_placeholder='Введи свой message...')

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Нажми меня!',
                          url='https://www.youtube.com/watch?v=qRyshRUA0xM&list=PLV0FNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM'
                              '&index=4')]
])


@dp.message(Command(commands=['start']))
async def hello(message: types.Message):
    await message.answer(
        text=f'Привет, {message.from_user.full_name}! Я telegram-bot Helper!  Я могу посчитать количество символов в '
             f'твоём сообщении, а так же отправить ID присланной тобой картинки или фотографии или твой личный ID: {message.from_user.id} !'
             f'Отправь '
             f'мне сообщение!', reply_markup=settings)


@dp.message(F.photo)
async def get_photo(message: types.Message):
    await message.answer(f'{message.from_user.full_name}, ID фото: {message.photo[-1].file_id}')


@dp.message()
async def len_str(message: types.Message):
    await message.answer(f'Число символов в сообщении:  {str(len(message.text))}', reply_markup=main)


if __name__ == '__main__':
    dp.run_polling(bot)
