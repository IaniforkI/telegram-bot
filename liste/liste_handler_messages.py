from config.config import bot, types
from liste.liste_button import *
from database.database_queries.sqlite_config import *

async def remove_my_list(message: types):
	msg = message.text
	d = msg.split()
	if len(d) == 1:
		await bot.send_message(message.from_user.id,"А что уберать?")
		return
	s = await remove_list(message.from_user.id, " ".join(d[1:]))
	if s == "изменено":
		await bot.send_message(message.from_user.id, "Вы убрали элимент из списка", reply_markup=await button())
	elif s == "нету":
		await bot.send_message(message.from_user.id, "Простите такого элимента нет", reply_markup=await button())

async def append_my_list(message: types):
	msg = message.text
	d = msg.split()
	s = await append_list(message.from_user.id, " ".join(d[1:]))
	if s == "изменено":
		await bot.send_message(message.from_user.id, "Ваш список изменён",reply_markup=await button())

async def my_list(message: types):
	a = await chek_user_database(message.from_user.id)
	if a == "создано":
		await bot.send_message(message.from_user.id, "Вы создади список", reply_markup=await knopka(str(message.from_user.id)))
	elif a == "существует":
		await bot.send_message(message.chat.id, "Управление списком",reply_markup=await knopka(str(message.from_user.id)))