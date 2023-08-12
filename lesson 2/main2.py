from aiogram import Bot, types, Dispatcher, executor

from config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    # await bot.send_message(chat_id=message.from_user.id,
    #                        text='Hello')
    await bot.send_message(chat_id=message.from_user.id,
                           text='<b>HELP</b>',
                           parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['картинка'])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo='https://bipbap.ru/wp-content/uploads/2017/04/image.jpeg')
    await message.delete()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)