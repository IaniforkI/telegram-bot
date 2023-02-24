from config.config import bot, types
async def all_help(message:types):
	await bot.send_message(message.chat.id,text =  """список команд:
	    admin-bot-commands:
	            /BD
	        commands:
	            /help_list
	            /help_chat:(администрирование чата)
	            /help_image:(anime картики)
	            Для поиска аниме тайтлов напишите ```@Gumdles_bot```
	                что бы знать все возможности напишите /help_title""")