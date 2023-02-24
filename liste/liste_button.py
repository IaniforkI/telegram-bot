from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def knopka(id):
	inline_btn_1 = InlineKeyboardButton('Меню', callback_data=f'button1|{id}')
	inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
	return inline_kb1

async def back_spi():
	inline_btn_2 = InlineKeyboardButton('Назад', callback_data='back_spi')
	kb = InlineKeyboardMarkup().add(inline_btn_2)
	return kb

async def button():
	inline_btn_2 = InlineKeyboardButton('Отчистить', callback_data='button2')

	inline_btn_3 = InlineKeyboardButton('Посмотреть', callback_data='button3')
	
	kb = InlineKeyboardMarkup(row_width=2).add(inline_btn_2,inline_btn_3)
	return kb

async def name(id):
	kb2 = InlineKeyboardMarkup()
	
	btn_1 = InlineKeyboardButton('Посмотреть слово', callback_data=f'слово|{id}')
	
	btn_2 = InlineKeyboardButton('Поменять слово', callback_data=f'мен|{id}')
	kb2.add(btn_1, btn_2)
	return kb2
