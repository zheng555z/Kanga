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
async def 圖片(ctx):
    #pic = discord.File(jdata['pic']) 傳送單一圖片
    #await ctx.send(file=pic)
    random_pic=random.choices(jdata['pic']) #隨機傳送圖片
    pic = discord.File(random_pic)
    await ctx.send(file= pic)




@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')

bot.run(jdata['TOKEN'])