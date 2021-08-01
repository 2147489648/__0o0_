import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['MAIN_C']))
        pic = discord.File(jdata['PIC'])
        await channel.send(f'{member} joined!')
        await channel.send(file=pic)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['MAIN_C']))
        await channel.send(f'{member} left!')
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == 'owo' and msg.author != self.bot.user:
            await msg.channel.send('owo')

def setup(bot):
    bot.add_cog(Event(bot))