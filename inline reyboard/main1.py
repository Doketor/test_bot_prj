from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Button 1',
                           url='https://www.youtube.com/watch?v=5_EHfHbzUCo&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=12')
ib2 = InlineKeyboardButton(text='Button 2',
                           url='https://www.youtube.com/watch?v=5_EHfHbzUCo&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=12')

ikb.add(ib1, ib2)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message()
    await message.delete()


@dp.message_handler()
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Hello World')


if __name__ == '__main__':
    executor.start_polling(dp)