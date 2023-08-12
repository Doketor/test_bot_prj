from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup

from config import TOKEN_API

async def on_startup(_):
    print('я запустился')


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='/links')
kb.add(b1)

kbi = InlineKeyboardMarkup()
ib1 = InlineKeyboardButton(text='Кнопка',
                          url='https://www.youtube.com/watch?v=5_EHfHbzUCo&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=12')
ib2 = InlineKeyboardButton(text='ryjgrf',
                          url='https://www.youtube.com/watch?v=5_EHfHbzUCo&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=12')
kbi.add(ib1, ib2)



@dp.message_handler(commands=['start'])
async def comands_links(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='hello world',
                           reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['links'])
async def comands_links(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='hello world',
                           reply_markup=kbi)
    await message.delete()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


