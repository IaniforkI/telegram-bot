from config.config import types, bot
async def help_image(message: types):
	await bot.send_message(message.chat.id,"/random:выведет 10 рандом аниме картинок\n/image:можно будет смотреть рандомные аниме картинки\n/name {name}: можно получить картинку зная еë название\n/favourites {name}:добавить картинку в избранное\n/my_favourites:выведет все {name} изображений из избранного\n/my_favourites_image:Выведет все изображения из избранного\n/remove_favourites {name}:уберет изображение из избранного\n/clear_favourites:полностью отчистит избранное")