import nextcord
from nextcord.ext import commands
import json
import requests
import aiohttp
from aiohttp import ClientSession
from logging_files.events_logging import logger
from nextcord import Client, Embed, Color , Interaction
from nextcord import slash_command, SlashOption
import os
import asyncio
import random


class system(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
      bot.embed_color = 0x69EBE4
      bot.error_color = 0xED4245

    

   
      
       

    @nextcord.slash_command(name="votecheck", description="Check if a user has voted")
    @commands.is_owner()
    async def votecheck(self, int : Interaction, user=SlashOption(name="user", description="Mention a user to check", required=True)):

      voted = await self.bot.session.get(f"https://top.gg/api/bots/732119152885497867/check?userId={user.id}",headers={"Authorization": os.environ["topgg_token"]})
      voted = await voted.json()["voted"]
      if voted == 1:
        await int.response.send_message(f"{user.name} have voted")
      else:
        await int.response.send_message(f"{user.name} hasn't voted")
      
    @nextcord.slash_command(name="leave", description="leave a server")
    @commands.is_owner()
    async def leave(self, int : Interaction, guild=SlashOption(name="guild", description="Mention a guildid", required=True)):
      g = self.bot.get_guild(guild)
      await g.leave()
      await int.response.send_message(f"left {g.name}")


    
    @nextcord.slash_command(name="ping", description="Bot latency ping")
    async def ping(self, int: Interaction):
        PingEmbed = nextcord.Embed(color=nextcord.Color.green(), title='Pong! 🏓', description=(f'{round(self.bot.latency * 1000)} ms'))
        await int.response.send_message(embed=PingEmbed)

    @nextcord.slash_command(name="contributors", description="Get a list of akio development contributors")
    async def contributors(self,int:Interaction):
      """Get the list of users that helped in development of xarvis"""
      e = nextcord.Embed(title="Contributors to Akio bot",color= self.bot.embed_color)
      e.add_field(name="Developers",value="`NotGizzy#9481`")
      #e.add_field(name="Art",value="`Arjun#7777`")
      e.add_field(name="Contributors",value="Spidey#7777\nDevils King#3000\n𝐕𝐚𝐧𝐪𝐮𝐢𝐬𝐡#0001\nCyrus Kensaro#8008`")
      await int.response.send_message(embed=e)
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
      c = self.bot.get_channel(859283068358492220)
      e2 = nextcord.Embed(title=f"🚨__NEW SERVER JOINED__🚨" , description=f"\nOwned by: {guild.owner}\nMember count: {guild.member_count}\nServer Name: {guild.name}\nServer id:",color=nextcord.Color.blurple())
      await c.send(f"{guild.id}",embed=e2)
      e = nextcord.Embed(title="🚨⚠️ **__ALERT__** 🚨⚠️", description="Bot may have joined a fake/test server" , color = nextcord.Color.red())
      e.add_field(name="Server Details",value=f"Owned by: {guild.owner}\nMember count: {guild.member_count}\nServer Name: {guild.name}\nServer id:{guild.id}")
        
      if guild.member_count <= 10:
        await c.send("<@333147019378032640>",embed=e)
        await random.choice(guild.text_channels).send("Hello There! Akio is moderated and is made to leave any test server! We would advise you to use the support server to test the bot\nFor more support type `>support` ")

      elif "Test" in guild.name:
        await c.send("<@333147019378032640>",embed=e)
        await random.choice(guild.text_channels).send("Hello There! Akio is moderated and is made to leave any test server! We would advise you to use the support server to test the bot\nFor more support type `>support` ")

      welcome_channel = guild.system_channel

      embed = nextcord.Embed(
      color=self.bot.embed_color,
      title="Thanks for inviting me!",description="• Please use `>help` for more information on the bot.")
      embed.set_footer(text="Akio® Unlimited Possibilities", icon_url=self.bot.user.avatar)

      logger.info(f"New guild| Joined Guild: {guild.name} | ID: {guild.id}")

      if welcome_channel is not None:
        await welcome_channel.send(embed=embed)
      else:
        pass


def setup(bot):
    bot.add_cog(system(bot)) 
    print("No errors is system cog")
    r = requests.head(url="https://discord.com/api/v1")
    try:
     print(f"Bot is Rate limited {int(r.headers['Retry-After']) / 60} minutes left")
    except:
      print("No rate limit")