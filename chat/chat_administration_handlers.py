from config.config import bot, types
from filter.admin_filter import admin_cmd
from chat.mute_time_filter import mute_time
from time import time
from aiogram.utils.exceptions import UserIsAnAdministratorOfTheChat, CantRestrictSelf,CantRestrictChatOwner,BadRequest


async def chat_link(message:types):
	if await admin_cmd(message):
	    chat = await bot.get_chat(message.chat.id)
	    await bot.send_message(message.chat.id, chat.invite_link)

async def remove_channels(message:types):
	if message.reply_to_message.sender_chat and await admin_cmd(message):
		await bot.ban_chat_sender_chat(message.chat.id,message.reply_to_message.sender_chat.id)
		await bot.send_message(message.chat.id,"этот пользователь больше не может писать от лица своих каналов")
	else:
		await bot.send_message(message.chat.id,"это сообщение не от лица канала")

async def un_ban_user(message:types):
	if not await admin_cmd(message):
	    return None
	me = await bot.get_me()
	users = message.text
	try:
			if int(message.reply_to_message.from_user.id) != int(me.id):
				msg = message.reply_to_message
				await bot.unban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
				if msg.from_user.last_name:
					await bot.send_message(message.chat.id, f"пользователь {msg.from_user.first_name} {msg.from_user.last_name} разбанен")
				else:
					await bot.send_message(message.chat.id, f"пользователь {msg.from_user.first_name} разбанен")
	except BadRequest as e:
		await bot.send_message(message.chat.id,f"Пользователь не забанен в данном чате")

async def ban_user(message:types):
	if not await admin_cmd(message):
	    return None
	replied_user = message.reply_to_message.from_user.id
	try:
		await bot.kick_chat_member(chat_id=message.chat.id, user_id=replied_user)
		await bot.send_message(message.chat.id, f"пользователь забанен что бы его вернуть напишите\nвернуть {replied_user}")
	except UserIsAnAdministratorOfTheChat as e:
		await bot.send_message(message.chat.id, "Нельзя банить админов")
	except CantRestrictSelf as e:
		await bot.send_message(message.chat.id,"Простите, но себя забанить не могу")
	except CantRestrictChatOwner as e:
			await bot.send_message(message.chat.id,"Не хочу идти против создателя чата")

async def un_mute_user(message: types):
	if not await admin_cmd(message):
	    return None
	await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
	permissions = types.ChatPermissions(can_send_messages=True,
        can_send_media_messages=True,
        can_send_audios=True,
        can_send_documents=True,
        can_send_photos=True,
        can_send_videos=True,
        can_send_video_notes=True,
        can_send_voice_notes=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_change_info=True,
        can_invite_users=True,
        can_pin_messages=True,
        can_manage_topics=True,
        join_to_send_messages=True
            ))
	if message.reply_to_message.from_user.last_name:
		await bot.send_message(message.chat.id,f"Пользователь {message.reply_to_message.from_user.first_name} {message.reply_to_message.from_user.last_name} размучен")
	else:
		await bot.send_message(message.chat.id,f"Пользователь {message.reply_to_message.from_user.first_name} размучен")

async def mute_user(message: types):
	if not await admin_cmd(message):
	    return None
	tim,inv = await mute_time(message)
	
	if tim is None and inv is None:
		return
	times=message.text.split()[1]
	try:
		await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date=time()+tim, permissions = types.ChatPermissions(can_send_messages=False))
		if message.reply_to_message.from_user.last_name:
			await bot.send_message(message.chat.id,f"Пользователь {message.reply_to_message.from_user.first_name} {message.reply_to_message.from_user.last_name} замучен на {times} {inv}")
		else:
			await bot.send_message(message.chat.id,f"Пользователь {message.reply_to_message.from_user.first_name} замучен на {times} {inv}")
	except UserIsAnAdministratorOfTheChat as e:
		await bot.send_message(message.chat.id, "Нельзя мутить админов")
	except CantRestrictSelf as e:
		await bot.send_message(message.chat.id,"Простите, но себя замутить не могу")
	except CantRestrictChatOwner as e:
		await bot.send_message(message.chat.id,"Не хочу идти против создателя чата")

async def user_id(message:types):
    try:
        await message.reply(f"id:{message.reply_to_message.from_user.id}")
    except:
        pass