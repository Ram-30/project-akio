import discord
from discord.ext import commands

import json

class Snipe(commands.Cog):
  '''Cog for snipe command'''
  def __init__(self, bot):
    
    self.bot = bot
    
      
  @commands.Cog.listener()
  async def on_message_delete(self, msg):

    if msg.author.bot:

      return
    
    file = open("snipe.json", "r")
    
    snipe = json.load(file)
    
    if not str(msg.guild.id) in snipe:
      
      snipe[str(msg.guild.id)] = {}
   
    if not "user-id" in snipe[str(msg.guild.id)]:
      
      snipe[str(msg.guild.id)]["user-id"] = {}
      
    if not "deleted-message" in snipe[str(msg.guild.id)]:
      
      snipe[str(msg.guild.id)]["deleted-message"] = {}
      
    snipe[str(msg.guild.id)]["user-id"] = msg.author.id
    
    snipe[str(msg.guild.id)]["deleted-message"] = msg.content
    
    dumps = open("snipe.json", "w")
    
    json.dump(snipe, dumps, indent = 4)
    
def setup(bot):
  
  bot.add_cog(Snipe(bot))