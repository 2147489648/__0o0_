import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(795641935540912179)
            while not self.bot.is_closed():
                await self.channel.send("Hi! I'm operating now!")
                await asyncio.sleep(1800)
        
        self.bg_task = self.bot.loop.create_task(interval())

    @commands.command()
    async def set_channel(self, ctx, ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Channel:{self.channel.mention}')

def setup(bot):
    bot.add_cog(Task(bot))