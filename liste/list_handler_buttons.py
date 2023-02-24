from config.config import bot, types
from liste.liste_button import *
from database.database_queries.sqlite_config import *

async def menu_my_list(call: types.CallbackQuery):
    a = call.data
    if a.split("|")[1] == str(call.from_user.id):

    	await call.message.edit_text(text = "Использование списка:\nДобавить {то что хотите добавить в список}\nУбрать {то что хотите убрать из списка}", reply_markup=await button())
    else:
    	await bot.answer_callback_query(callback_query_id=call.id, text="не нажимай, кнопка не для тебя", show_alert=True)

async def clear_my_list(call: types.CallbackQuery):
	status = await delete_list(call.from_user.id)
	if status == "отчищено":
		await call.message.edit_text(text = "Теперт ваш список пуст",reply_markup=await back_spi()) 

async def back_menu_my_list(call: types.CallbackQuery):
	await call.message.edit_text(text = "Использование списка:\nДобавить {то что хотите добавить в список}\nУбрать {то что хотите убрать из списка}", reply_markup=await button())

async def my_list_status(call: types.CallbackQuery):
	spisok = await look(call.from_user.id)
	try:
		spi = spisok.split(",")
	except:
		await call.message.edit_text(text ="Ваш список пуст", reply_markup = await back_spi())
	else:
	    sp="\n".join(spi[1:])
	    await call.message.edit_text(text = f"Ваш список:\n{sp}",reply_markup=await button())

