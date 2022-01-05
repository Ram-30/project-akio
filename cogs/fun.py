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
t cog_ext, SlashContext

class fun(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
    
    @nextcord.slash_command(name="Nitro", description="Free nitro?")
    async def nitro(self,ctx):
      m = random.randint(5,48)
      e = discord.Embed(title="A WILD GIFT APPEARS!", description=f"**NITRO**\nExpires in {m} hours")
      e.set_thumbnail(url="https://media.discordapp.net/attachments/848432518700990514/859659655570522112/images_10_1.jpeg")
      m = await ctx.channel.send(embed=e,components = [Button(label = "                       Accept                      ",style=3)])
      await ctx.send("Click the claim button to claim the gift")
      try:
        interaction = await self.bot.wait_for("button_click", check = lambda i: i.component.label.startswith("                       Accept                      "))
        await interaction.respond(content = "https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825")
        await m.edit(components=[Button(style=2, label="                    Claimed                       ", disabled=True)])
      except:
        return

    @nextcord.slash_command(name="kiss", description="kiss a user")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kiss(self, int : Interaction, user=SlashOption(name="user", description="Mention a user to kiss", required=True):

        
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
    async def blush(self, int: Interaction, user = SlashOption(name="user", description="Mention a user to kiss", required=True)):
       
          lick_api = 'https://waifu.pics/api/sfw/blush'
          parameter = dict()
          resp = requests.get(url=lick_api, params=parameter)
          data = resp.json()
          waifu_embed = nextcord.Embed(title='Blushy', url=data['url'], color=int.user.color, description = f'**{int.user}** is blushing')
          waifu_embed.set_image(url=data['url'])
          waifu_embed.set_footer(text='Requested by %s' % int.user, icon_url=int.user.avatar)
          await int.response.send_message(embed=waifu_embed)  
        elif user.id == int.author.id:
          await ctx.send("You blushed at yourself :flushed: , mention a user next time ")
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

    @cog_ext.cog_slash(name="Cry")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cry(self, ctx):
          """cry?"""
          lick_api = 'https://waifu.pics/api/sfw/cry'
          parameter = dict()
          resp = requests.get(url=lick_api, params=parameter)
          data = resp.json()
          waifu_embed = discord.Embed(title='Waaaaaaaaaaa', url=data['url'], color=ctx.author.color, description = f'**{ctx.author}** cries')
          waifu_embed.set_image(url=data['url'])
          waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
          await ctx.send(embed=waifu_embed) 
     
    @cog_ext.cog_slash(name="Poke", description="Poke a user",options=[create_option(name="user", description="Mention the user you want to poke",option_type=6,required=True)]) 
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def poke(self, ctx, user = None):
        """poke a user"""
        if not user:  # if member is no mentioned
            await ctx.send("You forgot to mention a user to poke")
        elif UserWarning == ctx.author:
          await ctx.send("You poked yourself. Mention a user next time ")
        elif user.id == 732119152885497867:
          await ctx.send("*Im a bot , you can't cant poke me*")
    
        else:
          
          lick_api = 'https://waifu.pics/api/sfw/poke'
          parameter = dict()
          resp = requests.get(url=lick_api, params=parameter)
          data = resp.json()
          waifu_embed = discord.Embed(title='Pokey poke', url=data['url'], color=ctx.author.color, description = f'**{ctx.author}** poked  **{user.name}**')
          waifu_embed.set_image(url=data['url'])
          waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
          await ctx.send(embed=waifu_embed) 
          
    @cog_ext.cog_slash(name="cuddle", description="Virtually cuddle with a user",options=[create_option(name="user", description="Mention the user you want to cuddle with",option_type=6,required=True)])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cuddle(self, ctx, user = None):
        """cuddle with a user"""
        if not user:  # if member is no mentioned
            await ctx.send("You can't cuddle the air. Mention a user next time")
        elif user == ctx.author:
          await ctx.send("You can't cuddle yourself , can you?")
        else:
          
          lick_api = 'https://waifu.pics/api/sfw/cuddle'
          parameter = dict()
          resp = requests.get(url=lick_api, params=parameter)
          data = resp.json()
          waifu_embed = discord.Embed(title='Cuddles UwU', url=data['url'], color=ctx.author.color, description = f'**{ctx.author}** cuddled with **{user.name}**')
          waifu_embed.set_image(url=data['url'])
          waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
          await ctx.send(f"{user.mention}",embed=waifu_embed)  

    @cog_ext.cog_slash(name="bonk", description="Virtually bonk a user",options=[create_option(name="user", description="Mention the user you want to bonk",option_type=6,required=True)])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bonk(self, ctx, user):
        """Bonk a user"""
        if user == ctx.author:
          await ctx.send("Why do you wanna bonk yourself 😐")
        elif user.id == 732119152885497867:
          await ctx.send("*bonks* Get bonked for tryna bonk me")
        else:
          lick_api = 'https://waifu.pics/api/sfw/bonk'
          parameter = dict()
          resp = requests.get(url=lick_api, params=parameter) 
          data = resp.json()
          waifu_embed = discord.Embed(title='Bonkkk', url=data['url'], color=ctx.author.color, description = f'**{ctx.author}** bonked **{user.name}**')
          waifu_embed.set_image(url=data['url'])
          waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
          await ctx.send(f"{user.mention}",embed=waifu_embed)  

    @cog_ext.cog_slash(name="ship", description="Ship 2 users together",options=[create_option(name="user1", description="Mention a user ",option_type=6,required=True),create_option(name="user2", description="Mention the other user ",option_type=6,required=False)])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ship(self, ctx, user1, user2 = None):
      """Ship 2 users , if one user provided ships the command executer with mentioned user"""
    
      if user2 is None:
        user2 = ctx.author

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

      em = discord.Embed(color=ctx.author.color)
      em.title = "%s ❤ %s" % (user1.name, user2.name,)
      em.description = f"**Love %**\n" f"`{counter_}` **{score}%**\n\n{finalName}"

      await ctx.send(embed=em)
      
    @ship.error
    async def ship_error(self, ctx, error):
      if isinstance(error, commands.BadArgument):
          embed = discord.Embed(
          color=self.bot.error_color,
          title=" <:broken_circle:847776660174274580> Invalid Arguments",
          description=f"• Invalid arguments were given\n> Correct usage: `>{ctx.command.usage}`")
          await ctx.reply(embed=embed,mention_author=False)
          ctx.command.reset_cooldown(ctx)
      elif isinstance(error, commands.MissingRequiredArgument):
          embed = discord.Embed(
          color=self.bot.error_color,
          title=" <:broken_circle:847776660174274580> Missing Arguments",
          description=f"• Incorrect command usage\nUsage Example: `>ship @user @user2`")
          await ctx.reply(embed=embed,mention_author=False)
          ctx.command.reset_cooldown(ctx)
        
    @cog_ext.cog_slash(name="simp", description="Know the simp rate of a user",options=[create_option(name="user", description="Mention the user whose simp rate you want ",option_type=6,required=False)])
    async def simp(self, ctx,user  = None):
        """Get The Simp rate of mentioned User"""
        if not user:  # if member is no mentioned 
            user = ctx.author 
        s = random.randint(1,100)
        embed = discord.Embed(title = "Simp rate machine", description = f"{user.name} is {s}% simp", colour = ctx.author.color)
        await ctx.send (embed = embed)

    @cog_ext.cog_slash(name="pp", description="Get the pp size of a user",options=[create_option(name="user", description="Mention a user whose pp size you want to know",option_type=6,required=False)])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pp(self, ctx ,user = None):
        """What Is PP Size Of User"""
        if not user:  # if member is no mentioned
            user = ctx.author
        PP = ['8','8D','8==D','8===D','8====D','8======D','8=======D','8========D','8===========D','8===============D']
         
        embed = discord.Embed(title = 'PP Size Machine', description = f"**{user.name}'s pp is this big\n ** {random.choice(PP)}",colour =0xF10000)
        if user.id == 333147019378032640:
          em = discord.Embed(title = 'How dare you', description = f"**{user.name} has the biggest and ||juiciest|| pp",colour =0xF10000)
          await ctx.send(embed=em)
        elif user.id == self.bot.user.id:
          em2 = discord.Embed(title = 'PP Size Machine', description = f"**I dont have a pp** I am a bot ;)",colour =0xF10000)
          await ctx.send(embed=em2)
        else:


          await ctx.send(embed = embed)

    @cog_ext.cog_slash(name="slap", description="Virtually slap a user",options=[create_option(name="user", description="Mention the user to slap",option_type=6,required=True)])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def slap(self, ctx, user = None):
      """Virtual Slap the mentioned user"""
      
      if user == ctx.author:
        await ctx.send("Do you need a hug? Mention someone other than you to slap")
      else:
        slap_api = 'https://waifu.pics/api/sfw/slap'
        parameter = dict()
        resp = requests.get(url=slap_api, params=parameter)
        data = resp.json()
        slap_embed = discord.Embed(title='Get slapped!', url=data['url'], color=ctx.author.color, description = f'**{ctx.author}** slapped **{user.name}**')
        slap_embed.set_image(url=data['url'])
        slap_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(f"{user.mention}",embed=slap_embed) 
        
    @cog_ext.cog_slash(name="pat", description="Virtually pat a user",options=[create_option(name="user", description="Mention the user you want to pat",option_type=6,required=True)])
    @commands.cooldown(1,  5, commands.BucketType.user)
    async def pat(self, ctx, user  = None) :
        '''Virtually pat the mentioned user'''
        pat_api = 'https://nekos.life/api/v2/img/pat'
        parameter = dict()
        resp = requests.get(url=pat_api, params=parameter)
        data = resp.json()
        pat_embed = discord.Embed(title='Pat', url=data['url'], color=ctx.author.color, description = f'**{ctx.author}** Patted **{user.name}**')
        pat_embed.set_image(url=data['url'])
        pat_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=pat_embed)
    

    @cog_ext.cog_slash(name="say", description="Make me say something",options=[create_option(name="message", description="Write the text you want me to say",option_type=3 ,required=True)])
    async def say(self,ctx,message: commands.clean_content):
      """Make the bot say something"""
      await ctx.send(f"{message}")
      
    @commands.command(aliases=["flip", "coin"],usage="flip")
    async def coinflip(self, ctx):
        """Flip a coin """
        coinsides = ["Heads", "Tails"]
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")

    @cog_ext.cog_slash(name="pressf", description="Pay your respects",options=[create_option(name="text", description="The thing you are paying respect for",option_type=3 ,required=False)])
    async def pressf(self, ctx, *, text: commands.clean_content = None):
        """ Press F to pay respect (text optional) """
        hearts = ["❤", "💛", "💚", "💙", "💜"]
        reason = f"for **{text}** " if text else ""
        await ctx.send(f"**{ctx.author.name}** has paid their respect {reason}{random.choice(hearts)}")
        
    
    @commands.command(usage="reverse <text>")
    async def reverse(self, ctx, *, text: str=None):
        """ !poow ,ffuts esreveR
        Everything you type after reverse will of course, be reversed
        """
        if not text:
          return await ctx.send("You didn't provide a text to reverse")
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f"🔁 {t_rev}")
        
    @cog_ext.cog_slash(name="choose", description="Make me choose between two options",options=[create_option(name="choice1", description="Frist choice",option_type=3,required=True),create_option(name="choice2", description="The second choice",option_type=3,required=True)])
    async def choose(self, ctx, *, choice1 , choice2 ):

      """Choose randomly from the options you give. xs!choose this, that"""
      choices = [choice1 , choice2 ]
      await ctx.send(f'{ctx.author.name} : `{choice1}` or `{choice2}`\nI choose: `{random.choice(choices)}`')

    
    @cog_ext.cog_slash(name="hug", description="Virtually hug a user",options=[create_option(name="user", description="Mention the user you want to hug",option_type=6,required=True)])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hug(self, ctx,  user  = None):
      """virtually hug the mentioned user"""
      if user == ctx.author:
        await ctx.channel.send("You hugged yourself. Mention a user other than you to hug next time")
      else:
        hug_api = 'http://api.nekos.fun:8080/api/hug'
        parameter = dict()
        resp = requests.get(url=hug_api, params=parameter)
        data = resp.json()
        h_embed = discord.Embed(title='Huggie 🤗', url=data['image'], color=ctx.author.color, description = f'{ctx.author.mention} gave a hug to  {user.mention}')
        h_embed.set_image(url=data['image'])
        h_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(f"{user.mention}",embed=h_embed)
 
        
    @cog_ext.cog_slash(name="reddit", description="get images from subreddit",options=[create_option(name="subreddit", description="Enter the subreddit name (replace space with _)",option_type=3 ,required=True)])
    async def reddit(self,ctx, subreddit=None):
      if subreddit == None:
        await ctx.send("You need to specify subreddit `ex: Discord_irl`")
      else:
        r = requests.get(url=f"https://meme-api.herokuapp.com/gimme/{subreddit}")
        rd = r.json()
        postlink = rd['postLink']
        sub = rd['subreddit']
        title = rd['title']
        url= rd['url']
        nsfw = rd['nsfw']
        spoiler = rd['spoiler']
        
        if nsfw == True:
            await ctx.send("This post is marked as NSFW,I cannot post it")
        else:
            if spoiler == True:
                await ctx.send("This post is marked as spoiler, are you sure you still want to view this? Respond with `y` or `n`")
                try:
                    response = await self.bot.wait_for('message', check=lambda m: m.author.id == ctx.author.id and m.channel.id == ctx.channel.id, timeout=10)
                    
                    if response.content.lower().startswith("y"):
                        embed = discord.Embed(color=ctx.author.color, description=f"[{title}]({postlink})")
                        embed.set_image(url=url)
                        embed.set_footer(text=f"r/{sub}")
                        await ctx.send(embed=embed)
                    elif response.content.lower().startswith("n"):
                        await ctx.send("cancelled")
                    else:
                        await ctx.send("cancelled")
                except asyncio.TimeoutError:
                    await ctx.send("timeout")
            else:
                embed = discord.Embed(color=ctx.author.color, description=f"[{title}]({postlink})")
                embed.set_image(url=url)
                embed.set_footer(text=f"r/{sub}")
                await ctx.send(embed=embed)
        
    @cog_ext.cog_slash(name="8ball", description="Ask 8ball a question",options=[create_option(name="question", description="Write the question you want to ask",option_type=3 ,required=True)])
    async def eightball(self, ctx, *, question: clean_content):
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
            emb = (discord.Embed(title="Question: {}".format(question), colour=0x3be801, description=prediction))
        elif choiceType == "(Non-committal)":
            prediction = random.choice(["Reply hazy try again ", 
                                        "Ask again later ", 
                                        "Better not tell you now ", 
                                        "Cannot predict now ", 
                                        "Concentrate and ask again "])
            emb = (discord.Embed(title="Question: {}".format(question), colour=0xff6600, description=prediction))
        elif choiceType == "(Negative)":
            prediction = random.choice(["Don't count on it ", 
                                        "My reply is no ", 
                                        "My sources say no ", 
                                        "Outlook not so good ", 
                                        "Very doubtful "])
            emb = (discord.Embed(title="Question: {}".format(question), colour=0xE80303, description=prediction))
        emb.set_author(name='Magic 8 ball', icon_url='https://media.discordapp.net/attachments/847018182426230794/848488495466938378/8ball_fun.png')
        await ctx.send(embed=emb)        
                 
                
     
      
def setup (bot):
  bot.add_cog(fun(bot))
  print("Fun module Ready to be loaded")
