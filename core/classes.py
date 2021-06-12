from discord.ext import commands
from discord.ext.commands import bot

class Cog_Extension(commands.cog):
    def __init__(self,bot):
        self.bot = bot