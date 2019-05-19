# -*- coding: utf-8 -*-
import discord
import requests
from bs4 import BeautifulSoup
import datetime
import json

app = discord.Client()

token = 'ㅅㅂ'


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
        boxofficeTime = messageInitalized - datetime.timedelta(days=1)
        if len(msg) == 1:
            boxoffice = requests.get('http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=04fc9903c58f171ed0aad4c20a565880&targetDt={}'.format(boxofficeTime.strftime('%Y%m%d')))
            boxoffice = boxoffice.json()
            em = discord.Embed(title='한국의 박스오피스에요!', description='')
            for movie in boxoffice['boxOfficeResult']['dailyBoxOfficeList']:
                rankchange = int(movie['rankInten'])
                if movie['rankOldAndNew'] == "OLD":
                    yesterday = "어제 {}위".format(int(movie['rank']) + rankchange)
                else:
                    yesterday = "신규!"
                if rankchange < 0:
                    rankmove = "어제 {}위 하락".format(-rankchange)
                elif int(movie['rankInten']) > 0:
                    rankmove = "어제 {}위 상승".format(rankchange)
                else:
                    rankmove = "박스오피스 순위 변동 없음"
                em.add_field(name="{}위 | {}".format(movie['rank'], movie['movieNm']),
                            value="{} | {}\n오늘 {}명 관람함".format(yesterday, rankmove, format(int(movie['audiCnt']), ',')),
                            inline=False)

            await app.send_message(message.channel, embed=em)
            return
        if len(msg) == 2:
            if msg[1].lower() in ['us', 'usa']:
                boxoffice = requests.get('https://www.boxofficemojo.com/daily/chart/?view=1day&sortdate={}'.format(boxofficeTime.strftime('%Y-%m-%d')))
                boxoffice = BeautifulSoup(boxoffice.text, 'html.parser')

                movies = boxoffice.select('#body > center > center > table > tbody > tr:nth-child(2) > td > table > tbody > tr')
                isStarted = False
                for movie in movies:
                    if not isStarted:
                        isStarted = True
                        continue
                    movie = movie.find('td')
                    



app.run(token)
