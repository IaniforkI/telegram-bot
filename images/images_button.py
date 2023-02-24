from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def image_rand():
	kb_test = InlineKeyboardMarkup()

	btn_10 = InlineKeyboardButton('⏩', callback_data="вперëд")

	btn_20 = InlineKeyboardButton('⏪', callback_data="Назад")
	kb_test.add(btn_20,btn_10)

	btn_30 = InlineKeyboardButton('🔁', callback_data="слайд")
	kb_test.add(btn_30)

	btn_40 = InlineKeyboardButton('🔀', callback_data="Рандом")
	kb_test.add(btn_40)
	return kb_test
	
async def image_next():
	btn_10 = InlineKeyboardButton('⏩', callback_data="вперëд")
	kb10 = InlineKeyboardMarkup().add(btn_10)
	return kb10