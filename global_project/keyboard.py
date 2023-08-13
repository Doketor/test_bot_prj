from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

kbi = InlineKeyboardMarkup(row_width=3)
bi1=InlineKeyboardButton(text='❤️',
                         callback_data='like')
bi2=InlineKeyboardButton(text='👎',
                         callback_data='dislike')
bi3=InlineKeyboardButton(text='🔄',
                         callback_data='next')
bi4=InlineKeyboardButton(text='⬅️',
                         callback_data='main')
kbi.add(bi1,bi2,bi3).add(bi4)


kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb2=ReplyKeyboardMarkup(resize_keyboard=True)
b1=KeyboardButton(text='/help')
b2=KeyboardButton(text='/description')
b3=KeyboardButton(text='send foto')

b4=KeyboardButton(text='random')
b5=KeyboardButton(text='back')

kb.add(b1).add(b2,b3)
kb2.add(b4,b5)