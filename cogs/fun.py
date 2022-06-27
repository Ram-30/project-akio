import random
import nextcord
import secrets
import asyncio
import aiohttp
import json
import requests
from aiohttp import ClientSession
from textwrap import TextWrapper
import os
from nextcord.ext.commands import clean_content
from io import BytesIO
from nextcord.ext import commands

from nextcord import Client, Embed, Color , Interaction
from nextcord import slash_command, SlashOption

class fun(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
      

    @nextcord.slash_command(name="kiss", description="kiss a user")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kiss(self, int : Interaction, user: nextcord.Member =SlashOption(name="user", description="Mention a user to kiss", required=True)):
        
      Kiss_api = 'https://nekos.life/api/v2/img/kiss'
      parameter = dict()
      resp = requests.get(url=Kiss_api, params=parameter)
      data = resp.json()
      k_embed = nextcord.Embed(title='Kissi', url=data['url'],color=int.user.color, description = f'{int.user.mention} kissed  {user.mention}') 
      k_embed.set_image(url=data['url'])
      k_embed.set_footer(text='Requested by %s' % int.user, icon_url=int.user.avatar)
      await int.response.send_message(f"{user.mention}",embed=k_embed)


 
    @nextcord.slash_command(name="blush", description="Blush at someone or just blush")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def blush(self, int: Interaction, user:nextcord.Member = SlashOption(name="user", description="Mention a user to blush at", required=True)):
        if not user:
          
          lick_api = 'https://waifu.pics/api/sfw/blush'
          parameter = dict()
          resp = requests.get(url=lick_api, params=parameter)
          data = resp.json()
          waifu_embed = nextcord.Embed(title='Blushy', url=data['url'], color=int.user.color, description = f'**{int.user}** is blushing')
          waifu_embed.set_image(url=data['url'])
          waifu_embed.set_footer(text='Requested by %s' % int.user, icon_url=int.user.avatar)
          await int.response.send_message(embed=waifu_embed)  
        elif user == int.user:
          await int.response.send_message("You blushed at yourself :flushed: , mention a user next time ")
        else:
          """blush or blush at someone"""
          lick_api = 'https://waifu.pics/api/sfw/blush'
          parameter = dict()
          resp = requests.get(url=lick_api, params=parameter)
          data = resp.json()
          waifu_embed = nextcord.Embed(title='Blushy', url=data['url'], color=int.user.color, description = f'**{int.user} is blushed at {user.name}**')
          waifu_embed.set_image(url=data['url'])
          waifu_embed.set_footer(text='Requested by %s' % int.user, icon_url=int.user.avatar)
          await int.response.send_message(embed=waifu_embed)  

    @nextcord.slash_command(name="cry", description="Cry?")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cry(self, int ):
          """cry?"""
          lick_api = 'https://waifu.pics/api/sfw/cry'
          parameter = dict()
          resp = requests.get(url=lick_api, params=parameter)
          data = resp.json()
          waifu_embed = nextcord.Embed(title='Waaaaaaaaaaa', url=data['url'], color=int.user.color, description = f'**{int.user}** cries')
          waifu_embed.set_image(url=data['url'])
          waifu_embed.set_footer(text='Requested by %s' % int.user, icon_url=int.user.avatar)
          await int.response.send_message(embed=waifu_embed) 
     
    @nextcord.slash_command(name="poke", description="poke a user")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def poke(self, int : Interaction, user: nextcord.Member =SlashOption(name="user", description="Mention a user to poke", required=True)):

        """poke a user"""
        if not user:  # if member is no mentioned
            await int.response.send_message("You forgot to mention a user to poke")
        elif UserWarning == int.user:
          await int.response.send_message("You poked yourself. Mention a user next time ")
        elif user.id == 732119152885497867:
          await int.response.send_message("*Im a bot , you can't cant poke me*")
    
        else:
          
          lick_api = 'https://waifu.pics/api/sfw/poke'
          parameter = dict()
          resp = requests.get(url=lick_api, params=parameter)
          data = resp.json()
          waifu_embed = nextcord.Embed(title='Pokey poke', url=data['url'], color=int.user.color, description = f'**{int.user}** poked  **{user.name}**')
          waifu_embed.set_image(url=data['url'])
          waifu_embed.set_footer(text='Requested by %s' % int.user, icon_url=int.user.avatar)
          await int.response.send_message(embed=waifu_embed) 
          
    @nextcord.slash_command(name="cuddle", description="virtually cuddle with a user")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cuddle(self, int : Interaction, user: nextcord.Member =SlashOption(name="user", description="Mention a user to cuddle with", required=True)):

        """cuddle with a user"""
        if not user:  # if member is no mentioned
            await int.response.send_message("You can't cuddle the air. Mention a user next time")
        elif user == int.user:
          await int.response.send_message("You can't cuddle yourself , can you?")
        else:
          
          lick_api = 'https://waifu.pics/api/sfw/cuddle'
          parameter = dict()
          resp = requests.get(url=lick_api, params=parameter)
          data = resp.json()
          waifu_embed = nextcord.Embed(title='Cuddles UwU', url=data['url'], color=int.user.color, description = f'**{ctx.author}** cuddled with **{user.name}**')
          waifu_embed.set_image(url=data['url'])
          waifu_embed.set_footer(text='Requested by %s' % int.user, icon_url=int.user.avatar)
          await int.response.send_message(f"{user.mention}",embed=waifu_embed)  

    @nextcord.slash_command(name="bonk", description="bonk someone")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bonk(self, int : Interaction, user: nextcord.Member =SlashOption(name="user", description="Mention a user to bonk", required=True)):

        """Bonk a user"""
        if user == int.user:
          await int.response.send_message("Why do you wanna bonk yourself 😐")
        elif user.id == 732119152885497867:
          await int.response.send_message("*bonks* Get bonked for tryna bonk me")
        else:
          lick_api = 'https://waifu.pics/api/sfw/bonk'
          parameter = dict()
          resp = requests.get(url=lick_api, params=parameter) 
          data = resp.json()
          waifu_embed = nextcord.Embed(title='Bonkkk', url=data['url'], color=int.user.color, description = f'**{nextcord.user}** bonked **{user.name}**')
          waifu_embed.set_image(url=data['url'])
          waifu_embed.set_footer(text='Requested by %s' % int.user, icon_url=int.user.avatar)
          await int.response.send_message(f"{user.mention}",embed=waifu_embed)  

    @nextcord.slash_command(name="ship", description="ship 2 users")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ship(self, int : Interaction, user1=SlashOption(name="user", description="Mention a user", required=True),user2=SlashOption(name="user2", description="Mention another user (leave empty for self)", required=False)):  

      """Ship 2 users , if one user provided ships the command executer with mentioned user"""
    
      if user2 is None:
        user2 = int.user

      #await ctx.trigger_typing()
        
      self_length = len(user1.name)
      first_length = round(self_length / 2)
      first_half = user1.name[0:first_length]
      usr_length = len(user2.name)
      second_length = round(usr_length / 2)
      second_half = user2.name[second_length:]
      finalName = first_half + second_half

      score = random.randint(0, 100)
      filled_progbar = round(score / 100 * 10)
      counter_ = '█' * filled_progbar + '‍ ‍' * (10 - filled_progbar)

      em = nextcord.Embed(color=int.user.color)
      em.title = "%s ❤ %s" % (user1.name, user2.name,)
      em.description = f"**Love %**\n" f"`{counter_}` **{score}%**\n\n{finalName}"

      await int.response.send_message(embed=em)
      
    @ship.error
    async def ship_error(self, int, error):
      if isinstance(error, commands.BadArgument):
          embed = nextcord.Embed(
          color=self.bot.error_color,
          title=" <:broken_circle:847776660174274580> Invalid Arguments",
          description=f"• Invalid arguments were given\n> Correct usage: `>{ctx.command.usage}`")
          await ctx.reply(embed=embed,mention_author=False)
          ctx.command.reset_cooldown(ctx)
      elif isinstance(error, commands.MissingRequiredArgument):
          embed = nextcord.Embed(
          color=self.bot.error_color,
          title=" <:broken_circle:847776660174274580> Missing Arguments",
          description=f"• Incorrect command usage\nUsage Example: `>ship @user @user2`")
          await ctx.reply(embed=embed,mention_author=False)
          ctx.command.reset_cooldown(ctx)
        
    @nextcord.slash_command(name="simp", description="get a users simprate")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def simp(self, int : Interaction, user: nextcord.Member =SlashOption(name="user", description="whose simprate you wanna find out", required=False)):

        """Get The Simp rate of mentioned User"""
        if not user:  # if member is no mentioned 
            user = int.user 
        s = random.randint(1,100)
        embed = nextcord.Embed(title = "Simp rate machine", description = f"{user.name} is {s}% simp", colour = int.user.color)
        await int.response.send_message (embed = embed)

    @nextcord.slash_command(name="pp", description="get a users pp size")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pp(self, int : Interaction, user: nextcord.Member =SlashOption(name="user", description="Mention a user", required=False)):

        """What Is PP Size Of User"""
        if not user:  # if member is no mentioned
            user = int.user
        PP = ['8','8D','8==D','8===D','8====D','8======D','8=======D','8========D','8===========D','8===============D']
         
        embed = nextcord.Embed(title = 'PP Size Machine', description = f"**{user.name}'s pp is this big\n ** {random.choice(PP)}",colour =0xF10000)
        if user.id == 333147019378032640:
          em = nextcord.Embed(title = 'How dare you', description = f"**{user.name} has the biggest and ||juiciest|| pp",colour =0xF10000)
          await int.response.send_message(embed=em)
        elif user.id == self.bot.user.id:
          em2 = nextcord.Embed(title = 'PP Size Machine', description = f"**I dont have a pp** I am a bot ;)",colour =0xF10000)
          await int.response.send_message(embed=em2)
        else:


          await int.response.send_message(embed = embed)

    @nextcord.slash_command(name="slap", description="virtually slap with a user")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def slap(self, int : Interaction, user: nextcord.Member =SlashOption(name="user", description="Mention a user to slap", required=True)):

      """Virtual Slap the mentioned user"""
      
      if user == int.user:
        await int.response.send_message("Do you need a hug? Mention someone other than you to slap")
      else:
        slap_api = 'https://waifu.pics/api/sfw/slap'
        parameter = dict()
        resp = requests.get(url=slap_api, params=parameter)
        data = resp.json()
        slap_embed = nextcord.Embed(title='Get slapped!', url=data['url'], color=int.user.color, description = f'**{int.user}** slapped **{user.name}**')
        slap_embed.set_image(url=data['url'])
        slap_embed.set_footer(text='Requested by %s' % int.user, icon_url=int.user.avatar)
        await int.response.send_message(f"{user.mention}",embed=slap_embed) 
        
    @nextcord.slash_command(name="pat", description="virtually cuddle with a user")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pat(self, int : Interaction, user: nextcord.Member =SlashOption(name="user", description="Mention a user to kiss", required=True)):

        '''Virtually pat the mentioned user'''
        pat_api = 'https://nekos.life/api/v2/img/pat'
        parameter = dict()
        resp = requests.get(url=pat_api, params=parameter)
        data = resp.json()
        pat_embed = nextcord.Embed(title='Pat', url=data['url'], color=int.user.color, description = f'**{int.user}** Patted **{user.name}**')
        pat_embed.set_image(url=data['url'])
        pat_embed.set_footer(text='Requested by %s' % int.user, icon_url=int.user.avatar)
        await int.response.send_message(embed=pat_embed)
    

   
    
    @nextcord.slash_command(name="hug", description="virtually hug a user")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hug(self, int : Interaction, user: nextcord.Member =SlashOption(name="user", description="Mention a user to hug", required=True)):

      """virtually hug the mentioned user"""
      if user == int.user:
        await int.respone.send_message("You hugged yourself. Mention a user other than you to hug next time")
      else:
        hug_api = 'http://api.nekos.fun:8080/api/hug'
        parameter = dict()
        resp = requests.get(url=hug_api, params=parameter)
        data = resp.json()
        h_embed = nextcord.Embed(title='Huggie 🤗', url=data['image'], color=int.user.color, description = f'{int.user.mention} gave a hug to  {user.mention}')
        h_embed.set_image(url=data['image'])
        h_embed.set_footer(text='Requested by %s' % int.user, icon_url=int.user.avatar)
        await int.response.send_message(f"{user.mention}",embed=h_embed)
 
        
    
        
    @nextcord.slash_command(name="8ball", description="ask 8ball something")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def eightball(self, int : Interaction, question=SlashOption(name="question", description="type ur question", required=True)):

        """extra generic just the way you like it"""
        choiceType = random.choice(["(Affirmative)", "(Non-committal)", "(Negative)"])
        if choiceType == "(Affirmative)":
            prediction = random.choice(["It is certain ", 
                                        "It is decidedly so ", 
                                        "Without a doubt ", 
                                        "Yes, definitely ", 
                                        "You may rely on it ", 
                                        "As I see it, yes ",
                                        "Most likely ", 
                                        "Outlook good ", 
                                        "Yes ", 
                                        "Signs point to yes "])
            emb = (nextcord.Embed(title="Question: {}".format(question), colour=0x3be801, description=prediction))
        elif choiceType == "(Non-committal)":
            prediction = random.choice(["Reply hazy try again ", 
                                        "Ask again later ", 
                                        "Better not tell you now ", 
                                        "Cannot predict now ", 
                                        "Concentrate and ask again "])
            emb = (nextcord.Embed(title="Question: {}".format(question), colour=0xff6600, description=prediction))
        elif choiceType == "(Negative)":
            prediction = random.choice(["Don't count on it ", 
                                        "My reply is no ", 
                                        "My sources say no ", 
                                        "Outlook not so good ", 
                                        "Very doubtful "])
            emb = (nextcord.Embed(title="Question: {}".format(question), colour=0xE80303, description=prediction))
        emb.set_author(name='Magic 8 ball', icon_url='https://media.discordapp.net/attachments/847018182426230794/848488495466938378/8ball_fun.png')
        await int.response.send_message(embed=emb)        
                 
                
     
      
def setup (bot):
  bot.add_cog(fun(bot))
  print("Fun module Ready to be loaded")
