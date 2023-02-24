from aiogram import executor
from aiogram.dispatcher.filters import Text
from config.config import dp
from images.images_heandlers_messages import *
from chat.chat_administration_handlers import *
from liste.liste_handler_messages import *
from liste.list_handler_buttons import *
from images.images_button_handlers import *
from help_handlers.help_images import help_image
from help_handlers.all_help import all_help
from help_handlers.chat_helping import help_chat
from liste.list_help import help_list
from inline_handler.help_inline import help_title, title
from start.start_handler import start
from inline_handler.anime_inline import anime_inline_handler
from status.my_status_chat import  *

#start handler
dp.register_message_handler(start, commands=["start"])

#help handlers
dp.register_message_handler(all_help, commands="help", commands_prefix='/!.')

dp.register_message_handler(help_chat, commands=["help_chat"], commands_prefix='!/.')

dp.register_message_handler(help_list, commands=["help_list"], commands_prefix='!/.')

dp.register_message_handler(help_title, commands=["help_title"], commands_prefix='!/.')

dp.register_message_handler(title, commands=["title"], commands_prefix='!/.')

#anime images handlers message
dp.register_message_handler(random_10_images, commands=["random"], commands_prefix='!/.')

dp.register_message_handler(anime_name,commands=["name"], commands_prefix='!/.')

dp.register_message_handler(favourites, commands=["favourites"], commands_prefix='!/.')

dp.register_message_handler(image, commands=["image"], commands_prefix='!/.')

dp.register_message_handler(remove_favourites, commands=["remove_favourites"])

dp.register_message_handler(clear_favourites, commands=["clear_favourites"], commands_prefix='!/.')

dp.register_message_handler(my_favourites, commands=["my_favourites"], commands_prefix='!/.')

dp.register_message_handler(my_favourites_image, commands=["my_favourites_image"], commands_prefix='!/.')

dp.register_message_handler(report_image,commands=["report_image"], commands_prefix='!/.')

dp.register_message_handler(help_image, commands=["help_image"], commands_prefix='!/.')
#anime messages handlers inline button
dp.register_callback_query_handler(next_image, lambda c: c.data == 'вперëд')


dp.register_callback_query_handler(back_image, lambda c: c.data == 'Назад')

dp.register_callback_query_handler(slide_image, lambda c: c.data == 'слайд')


dp.register_callback_query_handler(random_images, lambda c: c.data == 'Рандом')

#chat administrators handlers
dp.register_message_handler(chat_link, commands=["chat_link","ссылка чата","чат ссылка","ссылка"], chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP])

dp.register_message_handler(remove_channels,commands= "канал", is_reply=True, chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP], commands_prefix='-')

dp.register_message_handler(un_ban_user, lambda c: c.text.lower() in ["разбан","разбанить","вернуть"], is_reply = True, chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP])

dp.register_message_handler(ban_user, lambda c: c.text.lower() in ["выгнать","бан","забанить"], is_reply = True, chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP])
			
dp.register_message_handler(un_mute_user, lambda c: c.text.lower() in ["unmute","размут","размутить","говори"],is_reply = True, chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP])

dp.register_message_handler(mute_user, lambda c: c.text.lower().split()[0] in ["mute","мут"],is_reply = True, chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP])

dp.register_message_handler(user_id, lambda c: c.text.lower() in ["айди","id"],is_reply = True)

#personal list of each user handlers message
dp.register_message_handler(remove_my_list, lambda c: c.text.lower().split()[0] == "убрать",chat_type=types.ChatType.PRIVATE)

	
dp.register_message_handler(append_my_list, Text(startswith=["добавить","Добавить"]),chat_type=types.ChatType.PRIVATE)

dp.register_message_handler(my_list, Text(startswith=["список","Список"]),chat_type=types.ChatType.PRIVATE)
#personal list of each user handlers inline button
dp.register_callback_query_handler(menu_my_list, lambda c: c.data.split("|")[0] == 'button1')

dp.register_callback_query_handler(clear_my_list, lambda c: c.data == 'button2')

dp.register_callback_query_handler(back_menu_my_list, lambda c: c.data == 'back_spi')

dp.register_callback_query_handler(my_list_status, lambda c: c.data == 'button3')

#chat bot status
dp.register_my_chat_member_handler(my_new_chat_member)

#chat users status
dp.register_chat_member_handler(new_chat_members, lambda c: chats_users(c))

#inline mode handler
dp.register_inline_handler(anime_inline_handler)


if __name__ == "__main__":
	executor.start_polling(dp, allowed_updates=types.AllowedUpdates.all())
