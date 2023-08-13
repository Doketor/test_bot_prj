from aiogram import Bot, types, Dispatcher, executor
from aiogram.dispatcher.filters import Text
import random

from config import TOKEN_API
from keyboard import kb, kb2, kbi

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

list_url = ['https://klike.net/uploads/posts/2022-06/1654842644_4.jpg',
            'https://w.forfun.com/fetch/70/7047b702475924ba8f8044b5b5ca56ba.jpeg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_0CpUf0gItQwK6pm0oKMmkzWj53nUGtY427GQj_Ic&s']

random_choice=random.choice(list_url)

photos = dict(zip(list_url, ['1 котик', "2 котик", "3 котик"]))

flag = False

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
    random_choice=random.choice(list_url)
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random_choice,
                        caption=photos[random_choice],
                         reply_markup=kbi)
    await message.delete()


@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    global random_choice
    global flag
    if callback.data == 'like':
        if not flag:
            await callback.answer(text='вам понравилось')
            flag = not flag
        else:
            await callback.answer('вы уже лайкали')
    elif callback.data == 'dislike':
        await callback.answer(text='тебе не нравятся котики')
    elif callback.data == 'main':
        await callback.message.answer(text='главное меню',
                                      reply_markup=kb)
        await callback.message.delete()
        await callback.answer()
    else:
        random_choice = random.choice(list(filter(lambda x: x != random_choice, list_url)))
        await callback.message.edit_media(types.InputMedia(media=random_choice,
                                          type='photo',
                                          caption=photos[random_choice]),
                                          reply_markup=kbi)
        await callback.answer()




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)