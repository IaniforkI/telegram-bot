from config.config import types, bot
from database.database_queries.sqlite_config import c, conn
import asyncio
import os
from aiogram.utils.exceptions import BadRequest, RetryAfter, MessageNotModified, MessageToEditNotFound
async def next_image(call: types.CallbackQuery):
	anime=os.listdir("Аниме")
	photo = open(f"Аниме/{random.choice(anime)}", 'rb')
	id = call.message.chat.id
	use_id = """SELECT * from image"""
	c.execute(use_id)
	re = c.fetchall()
	for i in re:
		if i[0] == str(id):
			link = i[1]
			links = i[3]
			
	if links != "None":
		photo = open(f"Аниме/{links}", 'rb')
		c.execute("UPDATE image SET linkse = ? WHERE id = ?", ("None",id))
		conn.commit()
		await bot.edit_message_media(media=types.InputMedia(type='photo', media=photo, caption = f"Если картинка не по теме аниме то вы всегда можете сообщить об этом\n/report_image `{((photo.name).split('/')[-1])}`",parse_mode="MarkDown"), chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup = await image_rand())
		await asyncio.sleep(1)
	else:
		c.execute("UPDATE image SET link = ?, links = ? WHERE id = ?", ((photo.name).split("/")[-1],link,id))
		conn.commit()
		try:
			await bot.edit_message_media(media=types.InputMedia(type='photo', media=photo, caption = f"Если картинка не по теме аниме то вы всегда можете сообщить об этом\n/report_image `{((photo.name).split('/')[-1])}`",parse_mode="MarkDown"), chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup = await image_rand())
		except RetryAfter:
			pass
		except BadRequest:
			pass
		await asyncio.sleep(1)

async def back_image(call: types.CallbackQuery):
	chat = call.message.chat.id
	use_id = """SELECT * from image"""
	c.execute(use_id)
	re = c.fetchall()
	for i in re:
		if i[0] == str(chat):
			link = i[2]
			links = i[1]
	c.execute("UPDATE image SET linkse = ? WHERE id = ?", (links,chat))
	conn.commit()
	
	photo = open(f"Аниме/{link}","rb")
	try:
		await bot.edit_message_media(media=types.InputMedia(type='photo', media=photo, caption = f"Если картинка не по теме аниме то вы всегда можете сообщить об этом\n/report_image `{((photo.name).split('/')[-1])}`",parse_mode="MarkDown"), chat_id=call.message.chat.id, message_id=call.message.message_id,reply_markup = await image_next())
	except MessageNotModified:
		pass
	await asyncio.sleep(1)

async def slide_image(call: types.CallbackQuery):
	chat = call.message.chat.id
	try:
		for i in range(10):
			
			anime=os.listdir("Аниме")
			photo = open(f"Аниме/{random.choice(anime)}", 'rb')
			await bot.edit_message_media(media=types.InputMedia(type='photo', media=photo, caption = f"Если картинка не по теме аниме то вы всегда можете сообщить об этом\n/report_image `{((photo.name).split('/')[-1])}`",parse_mode="MarkDown"), chat_id=call.message.chat.id, message_id=call.message.message_id)
			photo.close()
			await asyncio.sleep(5)
	except ValueError as e:
		await bot.send_message(chat, f"Прошу прощения, что то пошло не так, надеюсь этого больше не повторится, \n{e}")
		return
	except MessageToEditNotFound as e:
		await bot.send_message(chat,f"Возможно сообщение было удалено\n{e}")
		return
	except BadRequest as e:
		await bot.send_message(chat,f"Возможно вы нажали на кнопку слайда несколько раз, поэтомy бот не успевает менять картинку\n{e}")
		return
	else:
		anime=os.listdir("Аниме")
		photo = open(f"Аниме/{random.choice(anime)}", 'rb')
		await bot.edit_message_media(media=types.InputMedia(type='photo', media=photo, caption = f"Если картинка не по теме аниме то вы всегда можете сообщить об этом\n/report_image `{((photo.name).split('/')[-1])}`",parse_mode="MarkDown"), chat_id=call.message.chat.id, message_id=call.message.message_id,reply_markup = await image_next())
		photo.close()

async def random_images(call: types.CallbackQuery):
	adds = ["если фото не соответсвует теме 'Аниме' то можете пожаловатся на неë"]
	media = []
	for phot in range(9):
		anime=os.listdir("Аниме")
		photo = open(f"Аниме/{random.choice(anime)}", 'rb')
		media.append(types.InputMediaPhoto(photo))
		adds.append(f"{phot+1})/report_image `{((photo.name).split('/')[-1])}`")
	
	anime=os.listdir("Аниме")
	photo = open(f"Аниме/{random.choice(anime)}", 'rb')
	adds.append(f"10)/report_image `{((photo.name).split('/')[-1])}`")
	media.append(types.InputMediaPhoto(photo, caption="\n".join(adds),parse_mode="MarkDown", reply_markup=await image_next()))
	try:
		await bot.send_media_group(call.message.chat.id, media=media)
	except RetryAfter:
		pass