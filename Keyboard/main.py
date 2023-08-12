from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('/photo')
kb.add(b1, b2).add(b3)

HELP_COMMAND = '''
<b>/help</b> - <i>список команд</i>
<b>/start</b> - <i>запуск бота</i>
<b>/description</b> - <i>описание бота</i>
<b>/photo</b> - <i>получать фото</i>
'''

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML')
    await message.delete()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ты козел',
                           reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['description'])
async def info_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Наш бот умеет отправлять фотографии')
    await message.delete()

@dp.message_handler(commands=['photo'])
async def photo_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                           photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5eW59lfW4jvk2yl2IMM5GoJ7zpzfelwl-48LT09TB&s')
    await message.delete()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)