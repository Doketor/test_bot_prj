from aiogram import Bot, types, Dispatcher, executor
from aiogram.dispatcher.filters import Text
import random

from config import TOKEN_API
from keyboard import kb, kb2, kbi

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


@dp.message_handler(Text(equals='send foto'))
async def open_kb_photo(message: types.Message):
    await message.answer(text='Что бы отправить рандомную фотку нажим "random"',
                         reply_markup=kb2)
    await message.delete()

@dp.message_handler(Text(equals='back'))
async def open_kb(message: types.Message):
    await message.answer(text='главное меню',
                         reply_markup=kb)
    await message.delete()

@dp.message_handler(Text(equals='random'))
async def send_random_photo(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random.choice(list_url),
                        caption='рандомный котик')
    await message.delete()


@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer(text='тебе нравятся котики')
    elif callback.data == 'dislike':
        await callback.answer(text='тебе не нравятся котики')




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)