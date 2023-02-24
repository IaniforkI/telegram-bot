from config.config import admin, bot

def admin_bot(id,cmd):
 if id in admin and cmd[:5] == ".exec":
  return True
 else:
  return False

async def admin_cmd(message):
    if int(message.from_user.id) in admin:
        return True
    else:
        adm = await bot.get_chat_administrators(message.chat.id)
        for i in adm:
            if int(i.user.id) == message.from_user.id:
                return True
        else:
            return False