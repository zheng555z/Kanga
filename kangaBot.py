import discord
from discord import file
from discord.ext import commands
import json
import random

with open('setting.json',mode='r',encoding='utf8')as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix='.')

@bot.event
async def on_raedy():
    print(">> Bot is online <<")

@bot.command()
async def 圖(ctx):
    #pic = discord.File(jdata['pic']) 傳送單一圖片
    #await ctx.send(file=pic)
    #random_pic=random.choice(jdata['pic']) 隨機傳送圖片(主機內)
    #pic = discord.File(random_pic)
    #await ctx.send(file= pic)
    random_pic=random.choice(jdata['url_pic'])
    await ctx.send(random_pic)


bot.run(jdata['TOKEN'])