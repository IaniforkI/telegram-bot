from config.config import bot

async def mute_time(message):
	text=message.text
	if len(text.split()) == 3:
		times=text.split()[1]
		minutes=text.split()[2]
	else:
		await bot.send_message(message.chat.id,"вы ввели команду в не правильном формате\nмут {число} время\nмут 5 минут")
		return None, None
		
	sek = ["секунд","секунды","секунда","сек"]
	min = ["минут","минута","минуты","мин"]
	chas = ["час","часа","часов","часы"]
	day =["дня","дней","дни","день"]
	mesc = ["месяц","месяца","месица","месяцов",'месицов']
	god = ["год","лет","года"]
	if minutes.lower() in sek:
		await bot.send_message(message.chat.id,"Минимальное время мута 1 минута, максимальное 2 года")
		return None, None
	elif minutes.lower() in min:
		tim = int(times) * 60
		inv = "минут(ы)"
	elif minutes.lower() in chas:
		tim = int(times) * 60 * 60
		inv = "часа(ов)"
	elif minutes.lower() in day:
		tim = int(times) * 60 * 60 * 24
		inv="дня(ей)"
	elif minutes.lower() in mesc:
		tim = int(times) * 60 * 60 * 24 * 31
		inv = "месяца(ев)"
	elif minutes.lower() in god:
		tim = int(times) * 60 * 60 * 24 * 31 * 12
		inv = "год(а)"
	return tim, inv