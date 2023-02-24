from config.config import *
from inline_handler.inline_mode_filter import *
import requests
from bs4 import BeautifulSoup as BS

async def anime_inline_handler(inline_query: types.InlineQuery):
    item = []
    id = 1
    if inline_query.query.split(' ')[0].capitalize() in genre.keys():
        names = genre[inline_query.query.capitalize().split(' ')[0]]
    else:
        years = inline_query.query.split(' ')[0]
    try:
        list = inline_query.query.split(' ')[1]
    except IndexError:
    	list = 1
    if inline_query.query and argse(inline_query.query):
	    if inline_query.query.split(' ')[0].capitalize() in genre.keys():
	        
	        r = requests.get(f"https://animebuff.ru/anime/filter?genre%5B%5D={names.capitalize()}&page={list}")
	        html = BS(r.content,"html.parser")
	        items = html.select(".anime-item__name")
	        coun = html.select(".anime-item__genre")
	        series = html.select(".anime-item__series")
	        img = html.select(".anime-item__image")
	        reting = html.select(".rating-green")
	        if (len(items)):
	            for (r,i),(s,(a,h)) in zip(zip(reting,items),zip(coun,zip(series,img))):
	            	input_content = types.InputTextMessageContent(f"{i.text}\n{s.text.split(',')[0]}\n{a.text}\n{r.text}")
	            	imag = h["src"]
	            	item.append(types.InlineQueryResultArticle(id=id,
	            	title=i.text,
	            	thumb_url=f"https://animebuff.ru{imag}",
	             input_message_content=input_content))
	            	id = id + 1
	
	    elif inline_query.query.split(' ')[0].isdigit():
	        if 2000 <= int(inline_query.query.split(' ')[0]) and int(inline_query.query.split(' ')[0]) < 2024:
	            r = requests.get(f"https://animebuff.ru/anime/year/{years}?page={list}")
	            html = BS(r.content,"html.parser")
	            items = html.select(".anime-item__name")
	            coun = html.select(".anime-item__genre")
	            series = html.select(".anime-item__series")
	            img = html.select(".anime-item__image")
	            reting = html.select(".rating-green")
	            if (len(items)):
	                for (r,i),(s,(a,h))in zip(zip(reting,items),zip(coun,zip(series,img))):
	                	input_content = types.InputTextMessageContent(f"{i.text}\n{s.text}\n{a.text}\n{r.text}")
	                	imag = h["src"]
	                	item.append(types.InlineQueryResultArticle(id=id,
	                	title=i.text,
	                	thumb_url=f"https://animebuff.ru{imag}",
	                	input_message_content=input_content))
	                	id = id + 1

    elif none_args(inline_query.query):
        r = requests.get(f"https://animebuff.ru/anime?page={inline_query.query}")
        html = BS(r.content,"html.parser")
        items = html.select(".anime-item__name")
        coun = html.select(".anime-item__genre")
        series = html.select(".anime-item__series")
        img = html.select(".anime-item__image")
        reting = html.select(".rating-green")
        if (len(items)):
            for (r,i),(s,(a,h))in zip(zip(reting,items),zip(coun,zip(series,img))):
            	input_content = types.InputTextMessageContent(f"{i.text}\n{s.text}\n{a.text}\n{r.text}")
            	imag = h["src"]
            	item.append(types.InlineQueryResultArticle(id=id,
            	title=i.text,
            	thumb_url=f"https://animebuff.ru{imag}",
             input_message_content=input_content))
            	id = id + 1
    elif inline_query.query.split(' ')[0].capitalize() == "Видео":
        r = requests.get(f"https://animebuff.ru/videos?page={list}")
        html = BS(r.content,"html.parser")
        items = html.select(".video__item-name")
        img = html.select(".video__item-img")
        if (len(items)):
            for i,h in zip(items,img):
                images = str(h).split("src=")[1].split('"')[1]
                h = str(h).split("src=")[1].split('"')[1].split("/")[4]
                imag = f"https://youtu.be/{h}.jpg"
                input_content = types.InputTextMessageContent(f"<b>{i.text}</b>\nhttps://youtu.be/{h}",
            parse_mode="HTML")
                item.append(types.InlineQueryResultArticle(
        id=id,
        title=i.text,
        description=f"https://youtu.be/{h}",
        url=f"https://youtu.be/{h}",
        hide_url=False,
        thumb_url=images,
        input_message_content=input_content))
                id = id + 1
    else:
        name = inline_query.query.split(' ')[0]
        r = requests.get(f"https://animebuff.ru/search?q={name}&page={list}")
        html = BS(r.content,"html.parser")
        items = html.select(".anime-item__name")
        coun = html.select(".anime-item__genre")
        series = html.select(".anime-item__series")
        img = html.select(".anime-item__image")
        reting = html.select(".rating-green")
        if (len(items)):
            for (r,i),(s,(a,h))in zip(zip(reting,items),zip(coun,zip(series,img))):
            	input_content = types.InputTextMessageContent(f"{i.text}\n{s.text}\n{a.text}\n{r.text}")
            	imag = h["src"]
            	item.append(types.InlineQueryResultArticle(id=id,
            	title=i.text,
            	thumb_url=f"https://animebuff.ru{imag}",
             input_message_content=input_content))
            	id = id + 1
    await bot.answer_inline_query(inline_query.id, results=[*item], cache_time=60)