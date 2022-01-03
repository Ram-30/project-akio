import nextcord
from nextcord.ext import commands
import json
import requests
import aiohttp
from aiohttp import ClientSession
from logging_files.owner_logging import logger
from logging_files.events_logging import logger
import disputils
from disputils import BotEmbedPaginator ,BotConfirmation
import os
import asyncio
import random


class system(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
      bot.embed_color = 0x69EBE4
      bot.error_color = 0xED4245

    @commands.Cog.listener()
    async def on_ready(self):
      print("System Cog Ready")

    @commands.Cog.listener()
    async def on_member_join(self,member):
      if member.guild.id == 848048628592279574:
        e = discord.Embed(title="Welcome to Akio Official Server", description=f"Hello {member.mention} Welcome to Akio Support Server\n<a:blue_star_op:848546162352586832> Make sure to read <#848432508542124032>\n<a:blue_star_op:848546162352586832> Go to  <#848432516432265276> for support\n<a:blue_star_op:848546162352586832> Talk with community in <#848432512137297930>",color=self.bot.embed_color)
        e.set_thumbnail(url=member.avatar_url)
        e.set_footer(text="Akio Development Team",icon_url="https://media.discordapp.net/attachments/869491746067865611/887991450170687518/20210916_144928.png")
        m= self.bot.get_channel(848432507699724298)
        await m.send(embed=e)
      
       

    @commands.command()
    @commands.is_owner()
    async def votecheck(self,ctx,user: discord.Member):
      voted = await self.bot.session.get(f"https://top.gg/api/bots/732119152885497867/check?userId={user.id}",headers={"Authorization": os.environ["topgg_token"]})
      voted = await voted.json()["voted"]
      if voted == 1:
        await ctx.send(f"{user.name} have voted")
      else:
        await ctx.send(f"{user.name} hasn't voted")
      
    @commands.command()
    @commands.is_owner()
    async def leave(self, ctx,guild:int):
      g = self.bot.get_guild(guild)
      await g.leave()
      await ctx.send(f"left {g.name}")


    @commands.command()
    @commands.is_owner()
    async def servers(self, ctx):
      activeservers = self.bot.guilds
      for guild in activeservers:
        await ctx.send(f"{guild.name} - {guild.member_count} - {guild.owner} ({guild.id})")

    @commands.command()
    @commands.is_owner()
    async def reply(self,ctx,user:discord.user,*,message):
      #m = self.bot.fetch_user(uid)
      try:
        await user.send(message)
        await ctx.send("Sent successfully")
      except Exception as e:
        await ctx.send(e)
       

 
    @commands.command(aliases=["restart"],hidden=True)
    @commands.is_owner()
    async def reboot(self,ctx):
      extensions = ['cogs.DL' , 'cogs.fun' , 'cogs.image' , 'cogs.moderation' , 'cogs.utils' ]
      try:
        m = await ctx.send("<a:warn:738717144518361149> Restarting bot!", delete_after=10)
        for extension in extensions:
          self.bot.unload_extension(extension)
          #await ctx.send(f"<a:loader:837561814765010944> reloading {extension}",delete_after=1)
        
          self.bot.load_extension(extension)
          #await ctx.send(f"loaded {extension}")
          await self.bot.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.listening,name=(f"Rebooting")))
      
        m = await ctx.send(" <a:loading:847421396984135680>  reloading cogs")
        
        await asyncio.sleep(5)
        await m.edit(content=" <a:loading:847421396984135680>  Loading json and database")
        await asyncio.sleep(4)
        await m.edit(content="Reboot completed")
        await asyncio.sleep(3)
        await m.edit(content="Logging in.")
        await asyncio.sleep(1)
        await m.edit(content="Logging in..")
        await asyncio.sleep(1)
        await m.edit(content="Logging in...")
        await asyncio.sleep(2)
        await m.edit(content="**__Logged in as__**:\n{0.user.name}\n{0.user.id}".format(self.bot))
        await asyncio.sleep(2)
        await m.edit(content=f'Current bot latency: {round(self.bot.latency * 1000)} ms')
        await self.bot.change_presence(status=discord.Status.online,activity=discord.Activity(type=discord.ActivityType.watching,name=(f"{len(self.bot.users)} members | {len(self.bot.guilds)} servers")))
      except Exception as e:
        await ctx.send(f"<a:deny:780077466161119273> error rebooting\n\n`{e}`") 
        await m.edit(content="<a:deny:780077466161119273> Reboot failure")
      
                 
          
       

    @nextcord.slash_command(name="ping", description="Bot latency ping")
    async def ping(self, ctx, interaction: Interaction):
        PingEmbed = discord.Embed(color=discord.Color.green(), title='Pong! 🏓', description=(f'{round(self.bot.latency * 1000)} ms'))
        await interaction.send_message(embed=PingEmbed)
     
        
  
    @commands.command()
    @commands.is_owner()
    async def test_join(self, ctx, member: discord.Member):
      await self.on_member_join(member)
    
     
      
    @commands.command(usage="new")
   # @commands.is_owner()
    async def new(self,ctx):
      e = discord.Embed(title="ChangeLog",description="**__New commands__**\n\n__0.4.2__\n• Added `bonk` , `cry` , `cuddle` , `blush` ,`poke` commands\n• Afk command is back\n• Moderation and Error improvements\n• Added a command **`>mind`** : Change my mind image gen\n\n__Previous changes (0.3.1)__\nEmbed:`Create a Embed`\n• Bug fixes\n• Cleaned the backend mess",color = self.bot.embed_color)
      await ctx.send(embed=e)
      
    @commands.command(usage="report <message> (image/gif of error)")
    @commands.bot_has_permissions(create_instant_invite=True)
    async def report(self,ctx,*,message):
      """Report or send feedback to the developers via this command\nYou can provide a image or gif too about the error to help us out"""
  
      confirmation = BotConfirmation(ctx, 0x012345)  
      channel = self.bot.get_channel(848448665646399488)
      author = ctx.author
      link= await ctx.channel.create_invite(max_age = 0)
      embed1 = discord.Embed(title="Bot Support", description=(f"**Your report has been sent for review** \n \n__Your Report__: \n \n{message} \n \n***Note: Abuse of this feature will lead to a permanent ban from the bot***"),color=discord.Color.green())
      embed1.set_footer(text="Please be patient We will contact You soon")
      if ctx.message.attachments:
        url = ctx.message.attachments[0].url
        embed1.set_image(url=url)
      await confirmation.confirm(f"Are you sure You wanna send this report to the Developers?\nMessage: `{message}`. \n\n <:warn:847767343395373097> Note: I must have Permission to create invite to send report") 
      if confirmation.confirmed:
        await  confirmation.update("Confirmed", color=0x55ff55)
        try:
          await author.send("**MESSAGE SENT**")
          await author.send(embed=embed1)
          embed = discord.Embed(title="bug/feedback report", description=f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id}) Has sent a report \n \n__Message:__ \n \n**{message}** \n \n__Server Invite__ \n{link}",color= discord.Color.blurple())
          if ctx.message.attachments:
            embed.add_field(name="Screenshot provided",value="\u200b")
            embed.set_image(url=url)
          await channel.send(embed=embed)
          
        except:
          await ctx.send("<:warn:847767343395373097> Report not sent.")
      
      else: 
        await  confirmation.update("Process cancelled", hide_author=True, color=0xff5555)
        
    @report.error
    async def report_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
          embed = discord.Embed(
          color=self.bot.error_color,
          title="<:warn:847767343395373097> Invalid Arguments provided",
          description="• Please supply a valid message!\nExample: `report <message>`" )
          await ctx.send(embed=embed)
      elif isinstance(error, commands.BotMissingPermissions):
          embed = discord.Embed(
          color=self.bot.error_color,
          title="<:warn:847767343395373097> Bot is Missing Permissions!",
          description="• Please give me the `create_invite` permissions to use this command!")
          await ctx.send(embed=embed)
  
    
    @cog_ext.cog_slash(name="support", description="Get akio's support server link")
    async def support(self,ctx):
      """Get Akio Support server link"""
      e = discord.Embed(title="<:Snow_info:847853879542022144> Akio Support Server", description="Click the button below to join the [Support server](https://discord.gg/5yeY36GnGS)",color=self.bot.embed_color)
      #emoji = self.bot.get_emoji(847767304707768390)
    
      await ctx.send("Support server link : https://discord.gg/yqgQbV5TMv",hidden=True)
    
    @cog_ext.cog_slash(name="upvote", description="Get the link to upvote Akio")
    async def upvote(self,ctx):
      """Get upvote link"""
      e = discord.Embed(title="<:Snow_info:847853879542022144> Upvote Akio",color=self.bot.embed_color)
      emoji = self.bot.get_emoji(847767304707768390)
      await ctx.channel.send(embed=e,components=[Button(style=5,emoji=emoji ,label="Upvote",url="https://top.gg/bot/732119152885497867/vote")])
      await ctx.send("Click the upvote button to get redirected to topgg")
 
   
    @commands.command(usage="invite")
    async def invite(self,ctx):
      e = discord.Embed(title="<:Snow_info:847853879542022144> Invite Akio", description="Click the button below to **[invite Akio](             https://discord.com/api/oauth2/authorize?client_id=732119152885497867&permissions=8&scope=bot)**",color=self.bot.embed_color)
      emoji = self.bot.get_emoji(847767304707768390)
    
      await ctx.send(embed=e,components=[Button(style=5,emoji=emoji ,label="Admin Invite (Recommended)",url="https://discord.com/oauth2/authorize?client_id=732119152885497867&permissions=8&scope=applications.commands%20bot"),Button(style=5,emoji=emoji ,label="Basic Invite",url="https://discord.com/api/oauth2/authorize?client_id=732119152885497867&permissions=418761783&scope=applications.commands%20bot")])
    
      #await ctx.send("The bot is not available to public yet. Please stay tuned")

    @cog_ext.cog_slash(name="contributors", description="Get a list of akio development contributors")
    async def contributors(self,ctx):
      """Get the list of users that helped in development of xarvis"""
      e = discord.Embed(title="Contributors to Akio bot",color= self.bot.embed_color)
      e.add_field(name="Developers",value="`NotGizzy#9481`")
      #e.add_field(name="Art",value="`Arjun#7777`")
      e.add_field(name="Contributors",value="Spidey#7777\nDevils King#3000\n𝐕𝐚𝐧𝐪𝐮𝐢𝐬𝐡#0001\nCyrus Kensaro#8008`")
      await ctx.send(embed=e)

    @commands.command(usage="status <dnd/online/idle>")
    @commands.is_owner()
    async def status(self, ctx, online_status):
      if str(online_status).lower() == "dnd":
        await self.bot.change_presence(status=discord.Status.dnd)
      elif str(online_status).lower() == "idle":
        await self.bot.change_presence(status=discord.Status.idle)
      elif str(online_status).lower() == "offline":
        await self.bot.change_presence(status=discord.Status.offline)
      else:
        await self.bot.change_presence(status=discord.Status.online)

      embed = discord.Embed(
      color=self.bot.embed_color,
      title="<:enter:847767304707768390> Status Changed!",
      description=f"• My status has been updated to: `{online_status.lower()}`")

      await ctx.send(embed=embed)

      logger.info(f"Owner | Sent Status: {ctx.author} | Online Status: {online_status}")

    @status.error
    async def change_status_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
        color=self.bot.embed_color,
        title="→ Invalid Arguments provided",
        description="• Please supply a valid option! Example: `status <online status>`"
            )
        await ctx.send(embed=embed)

    @commands.is_owner()
    @commands.command()
    async def name(self, ctx, name):
      """Update the bot username"""
      await self.bot.user.edit(username=name)

      embed = discord.Embed(
      color=self.bot.embed_color,
      title="→ Bot Name Changed!",
      description=f"• My name has been updated to: `{name}`"
        )

      await ctx.send(embed=embed)

      logger.info(f"Owner | Sent Name: {ctx.author} | Name: {name}")

    @name.error
    async def name_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
          embed = discord.Embed(
          color=self.bot.embed_color,
          title="→ Invalid Argument!",
          description="• Please put a valid option! Example: `l!name <name>`"
            )
          await ctx.send(embed=embed)
      elif isinstance(error, commands.CommandError):
          embed = discord.Embed(
          color=self.bot.embed_color,
          title="→ Unknown Error Has Occurred ",
          description=f"```python"
                      f"{error}"
                      f"```"
            )
          await ctx.send(embed=embed)

   
      #logger.info(f"Owner | Sent guilds: {ctx.author}")

    @commands.is_owner()
    @commands.command()
    async def get_invite(self, ctx):
      """Get server invite"""
      guild = self.bot.get_guild(id)

      for channel in guild.text_channels:
        picked = random.choice(channel)
        channels = self.bot.get_channel(picked)
      

      embed = discord.Embed(
      color=self.bot.embed_color,
      title=f"→ Invite From Guild",
      description=f"• Invite: {await channels.create_invite(max_uses=1)}"
        )

      await ctx.author.send(embed=embed)

      logger.info(f"Owner | Sent Get Invite: {ctx.author}")


    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
      """Shutdown/logout the bot"""
      embed = discord.Embed(
      color=self.bot.embed_color,
      title="→ Shutdown",
      description="• Performing a shutdown on the bot... ( :wave: )")

      await ctx.send(embed=embed)
      await self.bot.logout()

      logger.info(f"Owner | Sent Shutdown: {ctx.author}")




    @commands.Cog.listener()
    async def on_guild_join(self, guild):
      c = self.bot.get_channel(859283068358492220)
      e2 = discord.Embed(title=f"🚨__NEW SERVER JOINED__🚨" , description=f"\nOwned by: {guild.owner}\nMember count: {guild.member_count}\nServer Name: {guild.name}\nServer id:",color=discord.Color.blurple())
      await c.send(f"{guild.id}",embed=e2)
      e = discord.Embed(title="🚨⚠️ **__ALERT__** 🚨⚠️", description="Bot may have joined a fake/test server" , color = discord.Color.red())
      e.add_field(name="Server Details",value=f"Owned by: {guild.owner}\nMember count: {guild.member_count}\nServer Name: {guild.name}\nServer id:{guild.id}")
        
      if guild.member_count <= 10:
        await c.send("<@333147019378032640>",embed=e)
        await random.choice(guild.text_channels).send("Hello There! Akio is moderated and is made to leave any test server! We would advise you to use the support server to test the bot\nFor more support type `>support` ")

      elif "Test" in guild.name:
        await c.send("<@333147019378032640>",embed=e)
        await random.choice(guild.text_channels).send("Hello There! Akio is moderated and is made to leave any test server! We would advise you to use the support server to test the bot\nFor more support type `>support` ")

      welcome_channel = guild.system_channel

      embed = discord.Embed(
      color=self.bot.embed_color,
      title="Thanks for inviting me!",description="• Please use `>help` for more information on the bot.")
      embed.set_footer(text="Akio® Unlimited Possibilities", icon_url=self.bot.user.avatar_url)
      

      if welcome_channel is not None:
        await welcome_channel.send(embed=embed)
      else:
        pass

        logger.info(f"Events | Joined Guild: {guild.name} | ID: {guild.id}")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
      logger.info(f"Events | Left Guild: {guild.name} | ID: {guild.id}")

    @cog_ext.cog_slash(name="snipe", description="Get The most recently deleted message in the sevrer")
    async def snipe(self, ctx):
      file = open("snipe.json", "r")
    
      snipe = json.load(file)
    
      if not str(ctx.guild.id) in snipe:
      
        return await ctx.send("You quick-scoped the air , There's nothing to snipe!",hidden=True)   
      user = snipe[str(ctx.guild.id)]["user-id"]
    
      msg = snipe[str(ctx.guild.id)]["deleted-message"]
    
      fetched_user = await self.bot.fetch_user(int(user))
    
      embed = discord.Embed()
    
      embed.set_author(name=f"Message deleted by {fetched_user}", icon_url = fetched_user.avatar_url)
    
      embed.color = discord.Color.blurple()
    
      embed.description = msg
    
      #embed.timestamp = ctx.message.created_at
    
      await ctx.send(embed = embed)



def setup(bot):
    bot.add_cog(system(bot))
