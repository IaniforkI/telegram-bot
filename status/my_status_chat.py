from config.config import bot, types

async def my_new_chat_member(message:types.ChatMemberUpdated):
	name = message.new_chat_member
	if name.status == "member":
	    await bot.send_message(message.chat.id, "Дайте мне права администратора что бы я мог коректно работать")

async def new_chat_members(message:types.ChatMemberUpdated):
	name = message.new_chat_member
	oname = message.old_chat_member
	
	if name.status == "member" and oname.status == "left":
	    await bot.send_message(message.chat.id,f"Пользователь {name.user.first_name} {name.user.last_name} @{name.user.username} зашел в чат")
	elif name.status == "kicked":
	    await bot.send_message(message.chat.id, f"Пользователя {name.user.first_name} {name.user.last_name} @{name.user.username} кикнули из чата")
	elif name.status == "banned":
	    await bot.send_message(message.chat.id, f"Пользователя {name.user.first_name} {name.user.last_name} @{name.user.username} забанили в чате")
	elif name.status == "left" and oname.status in ["member","administrator","creator", "owner"]:# ["member", 'administranor',"owner"]:
	    await bot.send_message(message.chat.id,f"Пользователь {name.user.first_name} {name.user.last_name} @{name.user.username} покинул чат")
	elif name.status == "left" and oname.status not in ["member","administrator","creator", "owner"]:
	    await bot.send_message(message.chat.id,f"Пользователь {name.user.first_name} {name.user.last_name} @{name.user.username} убран из чёрного списка и может вернутся в чат")