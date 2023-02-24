from database.database_queries.sqlite_config import *
from config.config import types, bot
async def start(message: types):
	user = message.from_user.username
	ud = message.from_user.id
	name = message.from_user.first_name
	await list_start(ud)
	await append_database(ud)
	await image_users(ud)

	await bot.send_message(message.chat.id, f"Привет {name} теперь ты мой новый друг!\nЧто бы узнать мои команды -> /help")
	await bot.send_message(1328019298, f"пользователь с ником {name} нажал в боте /start\n@{user}\n{ud}")