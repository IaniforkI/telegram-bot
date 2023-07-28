from .. import loader, utils
import random
from telethon.tl.functions.users import GetFullUserRequest
import asyncio
@loader.tds
class poiskMod(loader.Module):
	"""by @Vsakoe0 | модуль, который найдёт пидорасов в чате"""
	strings = {'name':'poisk pidorasov'}
	async def поискcmd(self, message):
	    """- найти пидораса"""
	    await message.edit("поиск пидорасов активирован!")
	    await asyncio.sleep(1)
	    await message.edit("поиск пидорасов 🌑 ⬜⬜⬜⬜⬜")
	    await asyncio.sleep(1)
	    await message.edit("поиск пидорасов 🌒 ⬜⬜⬜⬜⬜")
	    await asyncio.sleep(1)
	    await message.edit("поиск пидорасов 🌓 🟩⬜⬜⬜⬜")
	    await asyncio.sleep(1)
	    await message.edit("поиск пидорасов 🌔 🟩⬜⬜⬜⬜")
	    await asyncio.sleep(1)
	    await message.edit("поиск пидорасов 🌕 🟩🟩⬜⬜⬜")
	    await asyncio.sleep(1)
	    await message.edit("поиск пидорасов 🌖 🟩🟩⬜⬜⬜")
	    await asyncio.sleep(1)
	    await message.edit("поиск пидорасов 🌗 🟩🟩🟩⬜⬜")
	    await asyncio.sleep(1)
	    await message.edit("поиск пидорасов 🌘 🟩🟩🟩⬜⬜")
	    await asyncio.sleep(1)
	    await message.edit("поиск пидорасов 🌑 🟩🟩🟩🟩⬜")
	    await asyncio.sleep(1)
	    await message.edit("поиск пидорасов 🌒 🟩🟩🟩🟩⬜")
	    await asyncio.sleep(1)
	    await message.edit("поиск пидорасов 🌓 🟩🟩🟩🟩⬜")
	    await asyncio.sleep(1)
	    await message.edit("поиск пидорасов 🌔 🟩🟩🟩🟩🟩")
	    await asyncio.sleep(1)
	    await message.edit("поиск пидорасов 🌕 🟩🟩🟩🟩🟩")
	    users = []
	    users = await message.client.get_participants(message.chat_id)
	    pidor = await message.client.get_entity(random.choice(users))
	    await message.edit(f'Из {len(users)} людей в этом чате пидором оказался <a href="tg://user?id={pidor.id}">{pidor.first_name}</a>')