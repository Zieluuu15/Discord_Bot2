import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello!, {ctx.author.mention}')

@bot.command()
async def hej(ctx, count=5):
    await ctx.send('hej! '  * count)


import random
@bot.command()
async def password(ctx,length=10):
    symbols = '123456789!@#$%^&*-_=+;:.,<>/?`|'
    password = ''
    for i in range(length):
        password += random.choice(symbols)
    await ctx.send(f'Twoje hasło to: {password}')

@bot.command()
async def suma(ctx, a: int, b:int):
    await ctx.send(f'Suma {a} + {b} =  {a+b}')

@bot.command()
async def roz(ctx, a: int, b:int):
    await ctx.send(f'Suma {a} - {b} =  {a-b}')

@bot.command()
async def mno(ctx, a: int, b:int):
    await ctx.send(f'Suma {a} * {b} =  {a*b}')


@bot.command()
async def dziel(ctx, a: int, b:int):
    await ctx.send(f'Suma {a} / {b} =  {a/b}')


import os
print(os.listdir('images'))
@bot.command()
async def animal(ctx):
    animal_name = random.choice(os.listdir('images'))
    with open(f'images/{animal_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


print(os.listdir('plants'))
@bot.command()
async def plant(ctx):
    plant_name = random.choice(os.listdir('plants'))
    with open(f'plants/{plant_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


print(os.listdir('colors'))
@bot.command()
async def color(ctx):
    color_name = random.choice(os.listdir('colors'))
    with open(f'colors/{color_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


print(os.listdir('food'))
@bot.command()
async def food(ctx):
    food_name = random.choice(os.listdir('food'))
    with open(f'food/{food_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


print(os.listdir('things'))
@bot.command()
async def thing(ctx):
    thing_name = random.choice(os.listdir('things'))
    with open(f'things/{thing_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


import requests
def get_image_dog_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def dog(ctx):
    image_url = get_image_dog_url()
    await ctx.send(image_url)

def get_image_duck_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def duck(ctx):
    image_url = get_image_duck_url()
    await ctx.send(image_url)


@bot.command()
async def random_smiles(ctx):
     emojis = [':laughing:',':weary:', ':poop:', ':lying_face:', ':jack_o_lantern:']
     await ctx.send(f'Twoja emotka: {random.choice(emojis)}')
     await ctx.send(emojis)


@bot.command()
async def translate(ctx, slowo):
    slowa = {
        'hello': 'witam',
        'poop': 'pupa',
        'cat': 'kot',
        'apple': 'jabłko'
    }
    for key in slowa.keys():
        if key == slowo:
            await ctx.send(f'Tłumaczenie słowa {slowo} to: {slowa[key]}')
            break

@bot.command()
async def rdd(ctx):
     emojis = [':jack_o_lantern:', ':dress:', ':athletic_shoe:', ':ring:']
     await ctx.send(f'Twoje rękodzieło to: {random.choice(emojis)}')
     await ctx.send(emojis)


@bot.command()
async def ooodpad(ctx, odpad):
    odpady = {
        'plastik': 'worek żółty, rozpad 1000 lat',
        'metal': 'worek żółty, rozpad 100 lat',
        'szkło': 'worek zielony, rozpad 2000 lat',
        'papierek': 'worek niebieski, rozpad 1 rok',
        'odpady zmieszane': 'worek czarny, rozpad od 100 do 1000 lat'

    }
    for key in odpady.keys():
        if key == odpad:
            await ctx.send(f'xxxxxxxx {odpad} to: {odpady[key]}')
            break


'----------------------------------------------------------------------------------------------'

import requests
NEWS_API_KEY = '-------------------------------------'
@bot.command(name='news')
async def news(ctx, *, query='technology'):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}&language=pl&pageSize=5'
    response = requests.get(url)
    if response.status_code != 200:
        await ctx.send('Nie udało się pobrać newsów')
        return
    news_data = response.json()
    articles = news_data['articles']

    if not articles:
        await ctx.send('Nie znaleziono newsów')
        return
    news_message = f'News for {query}:\n'
    for o, article in enumerate(articles, start=1):
        embed = discord.Embed(
            title=f'News o {query}',
            description=news_message,
            url=article['url'],
            color=discord.Color.blue()
        )
        embed.add_field(name='Author', value=article['author'])
        embed.add_field(name='Title', value=article['title'])
        embed.add_field(name='Description', value=article['description'])
        embed.add_field(name='Data publikacji', value=article['publishedAt'])
        embed.add_field(name='Link', value=article['url'])
        embed.add_field(name='Zrodlo', value=article['source']['name'])

        if article['urlToImage']:
            embed.set_image(url=article['urlToImage'])
        await ctx.send(embed=embed)



import aiohttp
api_key = '------------------------------'
@bot.command()
async def pogoda(ctx: commands.Context, *,city:str):
    url = 'http://api.weatherapi.com/v1/current.json'
    params = {
        'key' : api_key,
        'q' : city
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params = params) as res:
            data = await res.json()
            location = data['location']['name']
            temp_c = data['current']['temp_c']
            temp_f = data['current']['temp_f']
            humidity = data['current']['humidity']
            wind_mph = data['current']['wind_mph']
            wind_kph = data['current']['wind_kph']
            condition = data['current']['condition']['text']
            image_url = 'http:' + data['current']['condition']['icon']

            embed = discord.Embed(title=location, color=discord.Color.blue())
            embed.add_field(name='Tempetarure', value=f'{temp_c}C/{temp_f}f')
            embed.add_field(name='Humidity', value=f'{humidity}%')
            embed.add_field(name='Wind', value=f'{wind_mph}mph/{wind_kph}kph')
            embed.add_field(name='Condition', value=condition)
            embed.set_image(url=image_url)
            await ctx.send(embed=embed)



import json
DATA_FILE = 'lessons.json'
def load_data():
    if os.path.exists(DATA_FILE):
        with open (DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
    "Monday": [],
    "Tuesday": [],
    "Wensday": [],
    "Thursday": [],
    "Friday": [],
    "Saturday": [],
    "Sunday": []
    }

def save_date(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def format_schedule(day, lessons):
    if not lessons:
        return f'Brak lekcji w dniu {day}'
    response = f'Lekcje w dniu {day}:\n'
    for i, lesson in enumerate(lesson, 1):
        response +=f"{i}. {lesson['time']} - {lesson['subject']}"
    return response

@bot.command()
async def schedule(ctx, day: str):
    data = load_data()
    day = day.capitalize()
    if day not in data:
        await ctx.send(f'Nieprawidłowy dzień tygodnia: {day}')
        return
    schedule_message = format_schedule(day, data[day])
    await ctx.send(schedule_message)

@bot.command()
async def add(ctx, day: str, time: str, subject: str, room: str):
    data = load_data()
    day = day.capitalize()
    if day not in data:
        await ctx.send(f'Nieprawidłowy dzień tygodnia: {day}')
        return
    data[day].append({'time': time, 'subject': subject, 'room': room})
    save_date(data)
    await ctx.send(f'Dodano lekcję do {day} o {time} - {subject} (Ka6. {room})')


bot.run('--------------------------------------------------')
