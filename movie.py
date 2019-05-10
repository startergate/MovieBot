# -*- coding: utf-8 -*-
import discord
import requests
from bs4 import BeautifulSoup
import datetime

app = discord.Client()

token = 'NTc1MzE4NzczNDEwNTYyMDQ4.XNLdUw.rWFO7h2N_nrtsrq1dyMzhZ9ZJAE'


@app.event
async def on_ready():
    print("로그인 정보>")
    print(app.user.name)
    print(app.user.id)
    print("=============")
    await app.change_presence(game=discord.Game(name="도움말을 받으려면 m!help ", type=1))


@app.event
async def on_message(message):
    messageInitalized = datetime.datetime.now()
    if message.author.bot:
        return
    msg = message.content.split(' ')
    if msg[0] == 'm!boxoffice':
        if messageInitalized.day > 1:
            boxofficeTime = messageInitalized.replace(day=messageInitalized.day-1)
        else
            
        boxoffice = requests.get('http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=04fc9903c58f171ed0aad4c20a565880&targetDt=20190509')
        em = discord.Embed(title='한국의 박스오피스에요!', description='')
        for movie in boxoffice['boxOfficeResult']['dailyBoxOfficeList']:
            print(movie)

app.run(token)
