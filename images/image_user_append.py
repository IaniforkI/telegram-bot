from database.database_queries.sqlite_config import *
async def image_users(id,image = "None"):
	fo = c.execute('SELECT * FROM favourites WHERE id =?', (id,))
	if fo.fetchone() is None:
		c.execute("INSERT INTO favourites VALUES (?, ?)", (id, image))
		conn.commit()