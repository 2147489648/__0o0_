import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    @commands.command()
    async def image(self, ctx):
        pic = discord.File(jdata['PIC'])
        await ctx.send(file=pic)

    @commands.command()
    async def roll(self, ctx):
        n = random.randint(0,100)
        await ctx.send(n)

def setup(bot):
    bot.add_cog(React(bot))