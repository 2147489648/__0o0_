import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)



class Plan(Cog_Extension):
    @commands.command()
    async def revise(self, ctx):
        await ctx.send(jdata['REVISE'])
    @commands.command()
    async def score_change(self, ctx, value:int):
        score = score + value
        await ctx.send(score)

def setup(bot):
    bot.add_cog(Plan(bot))