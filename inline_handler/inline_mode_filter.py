genre = {'Безумие':'34',
'Боевые искусства':'32',
'Вампиры':'23',
'Военное':'2',
'Гарем':'35',
'Гурман':'41',
'Демоны':'27',
'Детектив':'9',
'Детское':'39',
'Дзёсей':'28',
'Драма':'5',
'Игры':'17',
'Исторический':'13',
'Комедия':'4',
'Космос':'16',
'Магия':'6',
'Машины':'38',
'Меха':'24',
'Музыка':'33',
'Пародия':'14',
'Повседневность':'19',
'Полиция':'30',
'Приключения':'3',
'Психологическое':'31',
'Работа':'42',
'Романтика':'22',
'Самураи':'15',
'Сверхъестественное':'21',
'Сёдзё':'25',
'Сёдзё-ай':'40',
'Сёнен':'8',
'Сёнен-ай':'37',
'Спорт':'26',
'Супер сила':'10',
'Сэйнэн':'18',
'Триллер':'11',
'Ужасы':'29',
'Фантастика':'12',
'Фэнтези':'7',
'Школа':'20',
'Экшен':'1',
'Этти':'36'
}

def argse(args):
	if len(args.split()) == 1:
		if args.isdigit():
			if int(args) >= 2000:
				return True
			else:
				return False
		else:
			if args.capitalize() in genre.keys():
				return True
			else:
				return False
	else:
		if args.split('\n')[0].capitalize() in genre.keys():
			return True
		else:
			if args.split("\n")[0].isdigit():
				if 2000 <= int(args.split("\n")[0]) and int(args.split("\n")[0]) <= 2022:
					return True
				else:
					return False
			return False

def none_args(args):
	if args.isdigit():
		if int(args) < 1500:
			return True
		else:
			return False
	else:
		if args == "":
			return True
		else:
			return False