from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

kbi = InlineKeyboardMarkup(row_width=3)


kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1=KeyboardButton(text='/help')
b2=KeyboardButton(text='/description')
b3=KeyboardButton(text='send foto')

kb.add(b1).add(b2,b3)