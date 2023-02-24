from config.config import bot, types

async def help_list(message: types):
	await bot.send_message(message.chat.id,"список(только в ЛС бота):\n¹)убрать {слово}—уберает слово из списка\n²)добавить {слово}—добавляет слово в список\n³)список—меню\nостальное управление кнопками")