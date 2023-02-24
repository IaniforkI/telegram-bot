import os
from config.config import *
from database.database_queries.sqlite_config import *
from aiogram.utils.exceptions import MessageTextIsEmpty, MessageToDeleteNotFound, MessageCantBeDeleted

async def random_10_images(message: types):
	adds = ["если фото не соответсвует теме 'Аниме' то можете пожаловатся на неë"]
	media = []
	for phot in range(9):
		anime=os.listdir("Аниме")
		photo = open(f"Аниме/{random.choice(anime)}", 'rb')
		media.append(types.InputMediaPhoto(photo))
		adds.append(f"{phot+1})/report `{((photo.name).split('/')[-1])}`")
	
	anime=os.listdir("Аниме")
	photo = open(f"Аниме/{random.choice(anime)}", 'rb')
	adds.append(f"10)/report `{((photo.name).split('/')[-1])}`")
	media.append(types.InputMediaPhoto(photo, caption="\n".join(adds),parse_mode="MarkDown"))
	await bot.send_media_group(message.chat.id, media=media)

async def anime_name(message: types):
	anime=os.listdir("Аниме")
	if len(message.text.split()) == 2:
		if (message.text).split()[1] in anime:
			await bot.send_photo(message.chat.id,photo=open(f"Аниме/{(message.text).split()[1]}", 'rb'), caption=f'/report `{message.text.split()[1]}`',parse_mode="MarkDown")
		else:
			await bot.send_message(message.chat.id,"Простите но картинки с названием: {(message.text).split()[1]} нету😞")

async def favourites(message: types):
	anime=os.listdir("Аниме")
	if len(message.text.split()) == 2:
		image_name = (message.text).split()[1]
		id = message.from_user.id
		fo = c.execute('SELECT * FROM favourites WHERE id =?', (id,))
		if fo.fetchone() is None:
			if (message.text).split()[1] in anime:
				c.execute("INSERT INTO favourites VALUES (?, ?)", (id, image_name))
				conn.commit()
				await bot.send_message(message.chat.id,f"картинка `{image_name}` добавлена в избранное",parse_mode="MarkDown")
			else:
				c.execute("INSERT INTO favourites VALUES (?, ?)", (id, "None"))
				conn.commit()
				await bot.send_message(message.chat.id,f"картинки с названием {image_name} нету(")
		else:
			use_id = """SELECT * from favourites"""
			c.execute(use_id)
			re = c.fetchall()
			for ud in re:
				if id == ud[0]:
					if ud[1] != "None":
						imag = (ud[1]).split(",")
						image = ud[1] + "," + image_name
					else:
						imag = "None"
						image = image_name
			if (message.text).split()[1] in anime:
				if image_name not in imag:
					c.execute("UPDATE favourites SET image=? WHERE id = ?", (image,id))
					conn.commit()
					await bot.send_message(message.chat.id,f"картинка `{image_name}` добавлена в избранное",parse_mode="MarkDown")
				else:
					await bot.send_message(message.chat.id,f"картинкa с названием `{image_name}` у вас уже в избранном(")
			else:
				await bot.send_message(message.chat.id,f"картинки с названием {image_name} нету(")

async def remove_favourites(message: types):
	if len((message.text).split()) != 2:
		await bot.send_message(message.chat.id,"и что же уберать?")
	else:
		id = message.from_user.id
		use_id = """SELECT * from favourites"""
		c.execute(use_id)
		re = c.fetchall()
		for ud in re:
			if id == ud[0]:
				imag = ud[1]
				if imag == "" or imag == "None":
					await bot.send_message(message.chat.id,"А у вас там пусто(")
				else:
				 imag = (ud[1]).split(",")
				 try:
				  imag.remove((message.text).split()[1])
				 except ValueError:
				  await bot.send_message(message.chat.id, "такого фото нет")
				 else:
				  c.execute("UPDATE favourites SET image=? WHERE id = ?", (",".join(imag),id))
				  conn.commit()
				  await bot.send_message(message.chat.id,"фото убрано из избранного")

async def clear_favourites(message: types):
	id = message.from_user.id
	c.execute("UPDATE favourites SET image=? WHERE id = ?", ("None",id))
	conn.commit()
	await bot.send_message(message.chat.id,"все фото убраны из избранного")

async def my_favourites(message: types):
		use_id = """SELECT * from favourites"""
		id = message.from_user.id
		c.execute(use_id)
		re = c.fetchall()
		for ud in re:
			if id == ud[0]:
				imag = ud[1]
				if imag != "None":
					try:
						await bot.send_message(message.chat.id,'\n'.join(imag.split(',')))
					except MessageTextIsEmpty:
						await bot.send_message(message.chat.id,"Пусто")
				else:
					await bot.send_message(message.chat.id,"у вас в избранном пусто")

async def my_favourites_image(message: types):
		media = []
		id = message.from_user.id
		use_id = """SELECT * from favourites"""
		c.execute(use_id)
		re = c.fetchall()
		for ud in re:
			if id == ud[0]:
				image = ud[1]
				if image == "" or image == "None":
					c.execute("UPDATE favourites SET image=? WHERE id = ?", ("None",id))
					conn.commit()
					await bot.send_message(message.chat.id,"у вас пусто(")
					return
				image = (image).split(",")
				a = len(image)//10
				if len(image) >=10:
					for i in range(a):
						for photos in image[:10]:
							photo = open(f"Аниме/{photos}","rb")
							media.append(types.InputMediaPhoto(photo))
							image.remove(photos)
						await bot.send_media_group(message.chat.id, media=media)
						media.clear()
				a = len(image)
				if a < 10:
					for photos in image[:a]:
						print(photos)
						photo = open(f"Аниме/{photos}","rb")
						media.append(types.InputMediaPhoto(photo))
						image.remove(photos)
					await bot.send_media_group(message.chat.id, media=media)
					media.clear()

async def report_image(message: types):
	user = {
	"name":message.from_user.first_name,
	"id":message.from_user.id,
	"link":f"tg://user?id={message.from_user.id}"
		}
	anime=os.listdir("Аниме")
	if (message.text).split()[1] in anime:
		await bot.send_photo(message.chat.id,photo=open(f"Аниме/{(message.text).split()[1]}", 'rb'), caption=f'{user["name"]}\n{user["id"]}\n{user["link"]}')
	else:
		await bot.send_message(message.chat.id, "фальш репорты не прокатят🙂☺")

async def image(message: types):
	id = message.chat.id
	fo = c.execute('SELECT * FROM image WHERE id =?', (id,))
	if fo.fetchone() is None:
		c.execute("INSERT INTO image VALUES (?, ?, ?, ?, ?)", (id, "None", "None", "None", "None"))
		conn.commit()
		
	use_id = """SELECT * from image"""
	c.execute(use_id)
	re = c.fetchall()
	for i in re:
		if i[0] == str(id):
			messag = i[4]
	if messag != "None":
		try:
			await bot.delete_message(chat_id=id,message_id = messag)
		except MessageToDeleteNotFound as e:
			pass
		except MessageCantBeDeleted:
			pass
	
	anime=os.listdir("Аниме")
	photo = open(f"Аниме/{random.choice(anime)}", 'rb')
	msg = await bot.send_photo(message.chat.id,photo=photo, caption=f"Привет,👆эта картинка меняется\n/help-Узнать об всех возможностях бота\nЕсли картинка не по аниме,вы можете сообщить о ней\n/report_image `{photo.name.split('/')[-1]}`", reply_markup=await image_next(),parse_mode="MarkDown")
	c.execute("UPDATE image SET link = ?, links = ?, msg = ? WHERE id = ?", ((photo.name).split("/")[-1], "None", msg.message_id, id))
	conn.commit()
	await asyncio.sleep(1)