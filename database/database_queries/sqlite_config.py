import sqlite3
conn = sqlite3.connect("database/bot.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS use (id INTEGER)""")

c.execute("""CREATE TABLE IF NOT EXISTS tabl (id INTEGER, aktiv TEXT, список TEXT)""")

c.execute("""CREATE TABLE IF NOT EXISTS image (id INTEGER, link TEXT, links TEXT, linkse TEXT, msg INTEGER)""")

c.execute("""CREATE TABLE IF NOT EXISTS favourites (id INTEGER, image TEXT)""")

async def append_database(id):
			fo = c.execute('SELECT * FROM use WHERE id =?', (id, ))
			if fo.fetchone() is None:
				c.execute("INSERT INTO use VALUES (?)", (id,))
				conn.commit()

async def list_start(id):
			aktiv="False"
			fo = c.execute('SELECT * FROM tabl WHERE id =?', (id, ))
			if fo.fetchone() is None:
				c.execute("INSERT INTO tabl VALUES (?,?,?)", (id,aktiv,None))
				conn.commit()

async def chek_user_database(id):
	tru = "True"
	use_id = """SELECT * from tabl"""
	c.execute(use_id)
	re = c.fetchall()
	for ud in re:
		if id == ud[0]:
			if ud[1] == "False":
				c.execute("UPDATE tabl SET aktiv = ? WHERE id = ?", (tru, id))
				conn.commit()
				return "создано"
			elif ud[1] == "True":
				return "существует"

async def append_list(id,msg):
	use_id = """SELECT * from tabl"""
	c.execute(use_id)
	re = c.fetchall()
	for ud in re:
		if id == ud[0]:
			spisoc = ud[2]
			a = f"{spisoc},{msg}"
			c.execute("UPDATE tabl SET список = ? WHERE id = ?", (a, id))
			conn.commit()
			return "изменено"

async def delete_list(id):
	use_id = """SELECT * from tabl"""
	c.execute(use_id)
	re = c.fetchall()
	for ud in re:
		if id == ud[0]:
			a = None
			c.execute("UPDATE tabl SET список = ? WHERE id = ?", (a, id))
			conn.commit()
			return "отчищено"
			
async def look(id):
	use_id = """SELECT * from tabl"""
	c.execute(use_id)
	re = c.fetchall()
	for ud in re:
		if id == ud[0]:
			spisoc = ud[2]
			return spisoc

async def remove_list(id,msg):
	use_id = """SELECT * from tabl"""
	c.execute(use_id)
	re = c.fetchall()
	for ud in re:
		if id == ud[0]:
			spisoc = ud[2].split(",")
			try:
				spisoc.remove(msg)
			except ValueError as e:
				return "нету"
			k = ",".join(spisoc)
			c.execute("UPDATE tabl SET список = ? WHERE id = ?", (k, id))
			conn.commit()
			return "изменено"

async def image_users(id,image = "None"):
	fo = c.execute('SELECT * FROM favourites WHERE id =?', (id,))
	if fo.fetchone() is None:
		c.execute("INSERT INTO favourites VALUES (?, ?)", (id, image))
		conn.commit()