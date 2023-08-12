from aiogram import Bot, types, Dispatcher, executor
import random

from config import TOKEN_API
from keyboard import kb

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

list_url = ['https://klike.net/uploads/posts/2022-06/1654842644_4.jpg','https://w.forfun.com/fetch/70/7047b702475924ba8f8044b5b5ca56ba.jpeg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_0CpUf0gItQwK6pm0oKMmkzWj53nUGtY427GQj_Ic&s']

async def on_startup(_):
    print('Start bot')


@dp.message_handler(commands=['start'])
async def send_echo(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='привет',
                           reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['help'])
async def send_echo(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='/help - помощь, /start - запуск, /description - описание')
    await message.delete()


@dp.message_handler(commands=['description'])
async def send_echo(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='это бот эхо')
    await message.delete()


@dp.message_handler()
async def send_echo(message: types.Message):
    if message.text == 'send foto':
        await bot.send_photo(chat_id=message.chat.id,
                             photo=random.choice(list_url),
                             caption='Случайны котик')
        await message.delete()




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)