# -*- coding: utf-8 -*-
import discord
import requests
from bs4 import BeautifulSoup

app = discord.Client()

token = 'NTc1MzE4NzczNDEwNTYyMDQ4.XNGQHg.JDn6zzlvdviPs_3lB3bomr3yu24'


@app.event
async def on_ready():
    print("로그인 정보>")
    print(app.user.name)
    print(app.user.id)
    print("=============")
    game = discord.Game(name="도움말을 받으려면 m!help ")
    await app.change_presence(status=discord.Status.idle, activity=game)


@app.event
async def on_message(message):
    if message.author.bot:
        return None
    msg = message.content.split(' ')

app.run(token)
