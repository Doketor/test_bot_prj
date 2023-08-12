from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import KeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup

from config import TOKEN_API

bot = Bot(TOKEN_API, parse_mode='HTML')
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/descriptiom')

kb.add(b1).add(b2)

@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text='sdgdsg',
                           reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id, text='Здесь должен быть хэлп')
    await message.delete()

@dp.message_handler(commands=['descriptiom'])
async def descriptiom_command(message: types.Message):
    await bot.send_message(message.chat.id, text='Здесь должно быть описание', reply_markup=ReplyKeyboardRemove())
    await message.delete()

@dp.message_handler()
async def help_command(message: types.Message):
    if message.text == '❤️':
        await bot.send_sticker(message.chat.id, sticker='CAACAgQAAxkBAAEJ8BFkz7bTgQjYdrmBkWmC4MEvcdcK6AACJQEAAqghIQbYv0ET_Pm8ei8E')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)