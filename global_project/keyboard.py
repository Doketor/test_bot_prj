from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1=KeyboardButton(text='/help')
b2=KeyboardButton(text='/description')
b3=KeyboardButton(text='send foto')

kb.add(b1).add(b2,b3)