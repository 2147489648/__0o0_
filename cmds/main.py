import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class Main(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')
    
    @commands.command()
    async def h(self, ctx):
        embed=discord.Embed(title="Hello everyone!", url="https://jikman.files.wordpress.com/2015/06/rin-best-girl-end.jpg?resize=648%2C363", description="I am __0o0_'s robot. Feel free to find me if you want.", color=0x00b3ff)
        embed.set_author(name="__0o0_", url="https://jikman.files.wordpress.com/2015/06/older-rin-tohsaka.jpg?resize=648%2C366", icon_url="https://jikman.files.wordpress.com/2015/06/older-rin-tohsaka.jpg?resize=648%2C366")
        embed.set_thumbnail(url="https://jikman.files.wordpress.com/2015/06/rin-best-girl-end.jpg?resize=648%2C363")
        embed.add_field(name="[ping", value="Displays bot latency", inline=False)
        embed.add_field(name="[roll", value="Rolls a random number from 0 to 100", inline=False)
        embed.add_field(name="[h", value="Shows a list of commands", inline=False)
        embed.set_footer(text="Created by __0o0_#5740")
        await ctx.send(embed=embed)

    @commands.command()
    async def rewrite(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clear(self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)


def setup(bot):
    bot.add_cog(Main(bot))