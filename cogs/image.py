import io
import os

import discord
from discord.ext import commands
import alexflipnote
import asyncio
from discord_slash.utils.manage_commands import create_option

from discord_components import DiscordComponents, Button
from discord_slash import cog_ext, SlashContext



# a token is required for the following methods: colour, colour_image, colour_image_gradient,
# birb, dogs, sadcat, cats, coffee

class Image(commands.Cog):
    def __init__(self, bot):
      self.bot = bot

    @commands.command(usage="captcha")
    async def captcha(self, ctx):
        avatar = ctx.author.avatar_url_as(size=1024, format=None, static_format='png')
        r = await self.bot.session.get(f"https://nekobot.xyz/api/imagegen?type=captcha&url={avatar}&username=Orange")
            res = await r.json()
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="Captcha Verification",

            )
            embed.set_image(url=res["message"])

            await ctx.send(embed=embed)

               

    # - TODO: Check to see if this API is still alive

    @commands.command(usage="cat")
    async def cat(self, ctx):
        r = await self.bot.session.get('https://some-random-api.ml/img/cat')
        res = await r.json()
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="Meow 🐈"
        )
        embed.set_image(url=res['link'])

        await ctx.send(embed=embed)

    @commands.command(usage="dog")
    async def dog(self, ctx):
        r = await self.bot.session.get('https://dog.ceo/api/breeds/image/random')
        res = await r.json()
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="Woof 🐕"
        )
        embed.set_image(url=res['message'])
        await ctx.send(embed=embed)

             
    @cog_ext.cog_slash(name="gay", description="Gay-ify a user's avatar",options=[create_option(name="user", description="Mention a user",option_type=6,required=False)])
    async def gay(self,ctx, user = None):
      if not user:
        user = ctx.author
      embed = discord.Embed(title = f"{user.name}",color=ctx.author.color)  # this is a example, everything is optional.
      embed.set_image(url = "attachment://gay.png")  # attaching file image to embed.
    # Wrapper
      try:
        image = await self.bot.alex_api.filter(13, user.avatar_url) # get Image object
        image_bytes = await image.read()  # get io.BytesIO object
     # Sending
        file = discord.File(image_bytes, "gay.png")  # pass io.BytesIO object to discord.File with a filename.
        await ctx.send(embed = embed, file = file)  # send both the embed and file, the file will attach to the embed.
      except:
        await ctx.send("Oh no i couldn't process the image. please try again later")

    @cog_ext.cog_slash(name="achievement", description="Get a achievement",options=[create_option(name="text", description="Mention the text for the achievement",option_type=3 ,required=True)])
    async def achievement(self,ctx,*,text: str, icon = None ):
      embed = discord.Embed(title = f"{ctx.author} unlocked a new achievement",color=ctx.author.color)  # this is a example, everything is optional.
      embed.set_image(url = "attachment://gay.png")  # attaching file image to embed.
    # Wrapper
      image = await self.bot.alex_api.achievement(text, icon = 46)
      image_bytes = await image.read()  # get io.BytesIO object
     # Sending
      file = discord.File(image_bytes, "gay.png")  # pass io.BytesIO object to discord.File with a filename.
      await ctx.send(embed = embed, file = file)  # send both the 
    
         

    @commands.command(usage="Tweet <username> <text>")
    async def tweet(self, ctx, username: str, *, text: str):
        r = await self.bot.session.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={text}")
        res = await r.json()
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="New Tweet"
        )
        embed.set_image(url=res["message"])

        await ctx.send(embed=embed)

             

    @tweet.error
    async def tweet_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:broken_circle:847776660174274580> Invalid Argument",
                description="• Please supply in a valid option! Example: `>tweet <username> <text>`"
            )

            await ctx.send(embed=embed)
          
    @cog_ext.cog_slash(name="clyde", description="Make clyde bot say something",options=[create_option(name="text", description="Mention the text for clyde bot to say",option_type=3 ,required=True)])
    async def clyde(self, ctx, *, text):
        r = await self.bot.session.get(f"https://nekobot.xyz/api/imagegen?type=clyde&text={text}")
        res = await r.json()
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="Clyde Bot sent a message"
        )
        embed.set_image(url=res['message'])

        await ctx.send(embed=embed)

                

    @clyde.error
    async def clyde_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:broken_circle:847776660174274580> Invalid Argument",
                description="• Please supply in a vaild option! Example: `>clyde <text>`"
            )

            await ctx.send(embed=embed)

    @commands.command(usage="vs <@user> <@user>")
    async def vs(self, ctx, member1: discord.Member, member2: discord.Member):
        member1 = member1.avatar_url_as(size=1024, format=None, static_format='png')
        member2 = member2.avatar_url_as(size=1024, format=None, static_format='png')
        r = await self.bot.session.get(f"https://nekobot.xyz/api/imagegen?type=whowouldwin&user1={member1}&user2={member2}")
        res = await r.json()
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="Who Would Win"
        )
        embed.set_image(url=res["message"])

        await ctx.send(embed=embed)

               

    @vs.error
    async def vs_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:broken_circle:847776660174274580> Invalid Member",
                description="• Please mention two valid members Example: `>vs @user1 @user2`"
            )

            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.error_color,
                title="→ Invalid Argument",
                description="• Please supply in a vaild option Example: `>vs @user1 @user2`"
            )

            await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="magik", description="Magik a user's avatar",options=[create_option(name="user", description="Mention a user",option_type=6,required=False)])
    async def magik(self, ctx, user = None, intensity: int = 5):
        member = user or ctx.author
        avatar = member.avatar_url_as(size=1024, format=None, static_format='png')
      

        message = await ctx.send(f"<:slowmode_time:862601700807933952> **Processing the image please wait!**")
        try:
            r = await self.bot.session.get(f"https://nekobot.xyz/api/imagegen?type=magik&image={avatar}&intensity={intensity}")
            res = await r.json()
            embed = discord.Embed(color=self.bot.embed_color,title="→ Magik")
            embed.set_image(url=res["message"])

            await ctx.send(embed=embed)
            await message.delete()
        except:
          await ctx.reply("I couldn't process that image, Please try again later.\nContact bot support if issue persists")

    @cog_ext.cog_slash(name="deepfry", description="deepfry a user's avatar",options=[create_option(name="user", description="Mention a user",option_type=6,required=False)])
    async def deepfry(self, ctx, user = None):
        member = user or ctx.author
        avatar = member.avatar_url_as(size=1024, format=None, static_format='png')
        

        message = await ctx.send(f"<:slowmode_time:862601700807933952>  **Processing the image please wait!**")
        try:
            r = await self.bot.session.get(f"https://nekobot.xyz/api/imagegen?type=deepfry&image={avatar}")
            res = await r.json()
            embed = discord.Embed(color=self.bot.embed_color,title="→ deepfry")
            embed.set_image(url=res["message"])

            await ctx.send(embed=embed)
            await message.delete()
        except:
          await ctx.reply("I couldn't process that image, Please try again later.\nContact bot support if issue persists")
       

    


    @cog_ext.cog_slash(name="mind", description="Change my mind meme",options=[create_option(name="text", description="Mention the text",option_type=3 ,required=True)])
    async def mind(self, ctx, text):
        r = await self.bot.session.get(f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}")
        res = await r.json()
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="Change My Mind"
        )
        embed.set_image(url=res["message"])

        await ctx.send(embed=embed)

              
    

    @cog_ext.cog_slash(name="youtube", description="Make a youtube comment",options=[create_option(name="comment", description="Mention the text for the comment",option_type=3 ,required=True)])
    async def youtube(self, ctx, *, comment):
        picture = ctx.author.avatar_url_as(size=1024, format=None, static_format='png')
        r = await self.bot.session.get(f"https://some-random-api.ml/canvas/youtube-comment?avatar={picture}&username={ctx.author.name}&comment={comment}")
        res = io.BytesIO(await r.read())
        youtube_file = discord.File(res, filename=f"youtube.jpg")
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="Youtube comment"
        )
        embed.set_image(url="attachment://youtube.jpg")

        await ctx.send(embed=embed, file=youtube_file)

         

    @youtube.error
    async def youtube_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:broken_circle:847776660174274580> Invalid Argument",
                description="• Please supply in a vaild option Example: `>youtube <comment>`"
            )

            await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="trigger", description="Trigger a user's avatar",options=[create_option(name="user", description="Mention a user",option_type=6,required=False)]) 
    async def trigger(self, ctx , user  = None):
        if not user:
          user = ctx.author
          
        picture =  user.avatar_url_as(size=1024, format=None, static_format='png')
        r = await self.bot.session.get(f"https://some-random-api.ml/canvas/triggered?avatar={picture}")
        res = io.BytesIO(await r.read())
        triggered_file = discord.File(res, filename=f"triggered.gif")
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="Triggered",
        )
        embed.set_image(url="attachment://triggered.gif")

        await ctx.send(embed=embed, file=triggered_file)

               


def setup(bot):
    bot.add_cog(Image(bot))
    print("Image manipulation module Ready to be loaded")