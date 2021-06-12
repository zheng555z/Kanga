import discord
from discord.enums import RelationshipType
from discord.ext import commands
from Kanga.core.classes import Cog_Extension
import random
import json

with open('setting.json',mode='r',encoding='utf8')as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    @commands.command()
    async def 圖(self,ctx):
        random_pic=random.choice(jdata['pic']) #隨機傳送圖片(主機內)
        pic = discord.File(random_pic)
        await ctx.send(file= pic)
    
    @commands.command()
    async def web(self,ctx):
        random_pic=random.choice(jdata['url_pic'])
        await ctx.send(random_pic)

    def setup(bot):
        bot.add_cog(React(bot))