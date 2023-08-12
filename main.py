from aiogram import Bot, executor, Dispatcher, types

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Я запустился')

HELP_INFO = '''
<b>/give</b> - <i>получаешь смешного котика</i>
<b>/help</b> - <i>получаешь помошь</i>
'''


@dp.message_handler(commands=['give'])
async def send_stikers(message: types.Message):
    await message.answer(text='Смотри какой смешной кот')
    await message.answer_sticker(sticker='CAACAgQAAxkBAAEJ8BFkz7bTgQjYdrmBkWmC4MEvcdcK6AACJQEAAqghIQbYv0ET_Pm8ei8E')


@dp.message_handler(commands='help')
async def get_help(message: types.Message):
    await message.answer(HELP_INFO, parse_mode='HTML')

@dp.message_handler(content_types=['sticker'])
async def send_stikers_id(message: types.Message):
    await message.answer(text=message.sticker.file_id)


@dp.message_handler()
async def send_black_heart(message: types.Message):
    if '❤️'  in message.text:
        return await message.answer(text='🖤')
    if '✅' in message.text:
        return await message.answer(text=str(message.text.count('✅')))
    await message.answer('Ты красавчик')




if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)


