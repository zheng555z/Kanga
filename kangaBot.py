import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='[')

@bot.event
async def on_raedy():
    print(">> Bot is online <<")

bot.run('ODQ5ODY3NDUyMjUwNzE4MjM5.YLhavg.S23ArrW4i-AocX8L78Tsx4MXoxw')