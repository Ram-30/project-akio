from nextcord.ext import commands
from nextcord.ext import tasks
from nextcord import Client, Interaction, SlashOption
import aiohttp
import config
import keep_alive
import os
import nextcord
import asyncio
import psutil
from googletrans import Translator
import json 

intents = nextcord.Intents.default()
intents.members = True
        
bot = commands.Bot(
    command_prefix=">",
    case_insensitive=True,
    intents=intents
    )

bot.remove_command("help")


@tasks.loop(seconds=30)
async def status_change():
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=(f"{len(bot.users)} members | {len(bot.guilds)} servers")))     
    await asyncio.sleep(30)
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening,name=("/help")))

@bot.event 
async def on_ready():
    print(f'Logged in as:\n{bot.user}')

@bot.event
async def on_message(message):
    if bot.user in message.mentions:
        return await message.channel.send(f"Hello I am Akio :wave: You can use my commands through slash commands.")

    elif message.content.startswith(">") and message.author.bot:
        embed = nextcord.Embed(
            title="Hello there, Trying to use commands?",
            description="""
            Akio was recently migrated to slash commands!
            All commands will only work via slash commands!

            Cannot see/use slash commands?
            Make sure to reinvite the bot by [clicking here](https://discord.com/oauth2/authorize?client_id=732119152885497867&permissions=8&scope=applications.commands%20bot)

            Need help? Join the support server by [clicking here](https://discord.gg/TbhN3ye9cC)]""",
            color=nextcord.Color.blurple())

        embed.set_footer(text="Akio development team", icon_url= bot.user.avatar.url)
        return await  message.channel.send(embed=embed)
    await bot.process_commands(message) 

for filename in os.listdir('./cogs'):
         if filename.endswith('.py') and not filename.startswith("_"):
            try:
                bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded {filename[:-3]}')
            except Exception as e:
                print(f'Faield to load {filename[:-3]} due to {e}')

bot.developers = config.developers
bot.owner_ids = config.owners
bot.topgg_token = config.topgg_token

@bot.slash_command(name="help", description="View the help page")
async def help(interaction , args=SlashOption(name="args", description="Provide a module/command name",required=False)):
  help_embed = nextcord.Embed(title="Akio help command", color = 0x69EBE4)
  command_names_list = [x.name for x in bot.commands_slash]


    # If there are no arguments, just list the commands:
  if not args:
    help_embed= nextcord.Embed(description=(f"[Invite me](https://discord.com/api/oauth2/authorize?client_id=732119152885497867&permissions=8&scope=bot) | [Support Server](https://discord.gg/5yeY36GnGS) | [Upvote](https://top.gg/bot/732119152885497867/vote)\nAll the modules of the bot are listed below"), color = 0x69EBE4)
    #help_embed.add_field(name="<:music:847767269899370538> Music",value=f"Type **`>help music`**")
    help_embed.add_field(name=" <:mod:847767322156335135> Moderation Commands",value=f"Type **`>help mod`**")
    help_embed.add_field(name=" <:fun:847767372400295946> Fun commands",value=f"Type **`>help fun`**")
    #help_embed.add_field(name="💰 Economy Commands",value="Type **`>eco`**")
    help_embed.add_field(name=" <:utility:847767398508789791> Utility commands",value=f"Type **`>help utility`**")
    help_embed.add_field(name="<:Snow_info:847853879542022144> Bot information",value=f"Type **`>help info`**")
      
    help_embed.add_field(name="Details",value=f"Type `>help <command name>` for more details about a command.",inline=False)
    help_embed.add_field(name="\u200b" ,value="[Invite me](https://discord.com/api/oauth2/authorize?client_id=732119152885497867&permissions=8&scope=bot) | [Support Server](https://discord.gg/5yeY36GnGS) | [Upvote](https://top.gg/bot/732119152885497867/vote)")
    
    help_embed.set_footer(text="Akio® | Made by NotGizzy#9481",icon_url="https://media.discordapp.net/attachments/869491746067865611/887991450170687518/20210916_144928.png")
    help_embed.set_thumbnail(url="https://media.discordapp.net/attachments/867648204279513088/887994311218724874/20210916_091654.png")
    await interaction.response.send_message(embed=help_embed)
 
  
  elif args == "utility":
    help_embed.add_field(name="<:Snow_info:847853879542022144> ServerInfo",value ="`Get information about the server`")
    help_embed.add_field (name="<:question_mark:848121100387090443> Whois",value ="`Get information about a mentioned user`")
    help_embed.add_field(name="<:ascii:848121059521200128> Ascii",value ="`Make ascii art`")
    help_embed.add_field(name="<:av:848121080245518357> Avatar",value ="`Get mentioned users avatar`")
    help_embed.add_field(name=" <:magnify_glass:858332516775624704> bigemoji",value ="`Make a emoji bigger`")
    
    help_embed.add_field(name="<:logs:847775658805166080> Define",value ="`Get definition of mentioned word from urban dictionary`")
    #help_embed.add_field(name="<:afk:848121032962736149> Afk",value ="`Set afk status`")
    help_embed.add_field(name="<:emoji_2:851707692295913486> Channel Topic",value ="`Get channel topic of current or mentioned channel`")
    help_embed.add_field(name="<:role_info:851705678447771678> Inrole",value ="`Get the list of users in a role`")
    help_embed.add_field(name="<:embed_add:858614012190785546> embed",value="Interactive embed Creator")
    help_embed.add_field(name="<:magnify_glass:858332516775624704> Role",value ="`Get Information about a role`")
    help_embed.set_footer(text=f"Type `>help <command name>` for more details about a command.")
    await interaction.response.send_message(embed=help_embed)
  
  elif args == "fun":
    help_embed.add_field(name="<:hugie:847962984243265568> Hug",value ="`Give a user virtual hug`")
    help_embed.add_field(name="<:pat:847963024391536660> Pat",value ="`Give a user virtual pat`")
    help_embed.add_field(name="<:kiss_fun:848497004749651998> Kiss",value="`Give a user a virtual kiss`")
    help_embed.add_field(name="<:slaps:847962777590693919> Slap",value ="`Virtually slap a user`")
    help_embed.add_field(name="<:heart_cyan:847962945543340053> Ship",value ="`Ship users together`")
    help_embed.add_field(name="<:F_letter:847962864174104597> f",value ="`Pay your respects`")
    help_embed.add_field(name="<:REVERSE:847962793725788212> Reverse",value ="`Reverse your message`")
    help_embed.add_field(name="<:8ball_fun:848487045575737355> 8ball",value="`Get a 8bal prediction`")
    help_embed.add_field(name="<:nitro:888351590426222642> Nitro",value="`Free nitro?`")
    help_embed.add_field(name="<:reddit:847962820929781821> Reddit",value ="`Get a random image from specified subreddit`")
    help_embed.add_field(name="<:pin_important:847962841574408212> Choose",value ="`Make the bot choose between options`")

    help_embed.add_field(name="<:youtube:849646074158383164> Youtube",value ="`Make a YouTube comment`")
    help_embed.add_field(name="<:twitter:849646014860230686> Tweet",value ="`Tweet something`")
    help_embed.add_field(name="<:trigger:849645876313718854> Trigger",value ="`Trigger someone`")
    help_embed.add_field(name="<:magic_stick:849645547371233280> Magik",value ="`Magik someone's avatar`")
    help_embed.add_field(name="<:av:848121080245518357> clyde",value ="`Make clyde bot say something`")
    help_embed.add_field(name="<:versus:849646037861531668> vs",value ="`Who will win?`")
    help_embed.add_field(name="<:gae:849647492081385473> gay",value ="`apply gay flag on a user's avatar`")
    help_embed.add_field(name="<:trophy_congrats:849645897020080168> Achievement",value ="`Get a achievement`")
    
    help_embed.add_field(name="<:cat_blue:849645508493443175> Cat",value ="`Get a cat image`")

    help_embed.add_field(name="<:dog_blue:849645528387158066> Dog",value ="`Get a Dog image`")

    help_embed.add_field(name="<:captcha:849645490605654018> Captcha",value ="`Get Your PFP In Captcha`")

    help_embed.add_field(name="<:pp_ruler:858631042427256832> PP Size",value ="`Know Your or others PP Size`")

    help_embed.add_field(name="<:simpin:858631060555431937> Simp",value ="`Check Simp Rate`")

    help_embed.add_field(name="<:person_say:858630989012926464> Say",value ="`Make Bot Say Something`")


    help_embed.set_footer(text=f"Type `>help <command name>` for more details about a command.")
    await interaction.response.send_message(embed=help_embed)
    
  elif args == "mod":
    help_embed.add_field(name="<:nickname:848436062845927435> Nickname",value ="`Change nick of a user`")
    help_embed.add_field(name="<:muted:848436041656434708> Mute",value ="`Mute a user`")
    help_embed.add_field(name="<:umuted:848436114917425162> Unmute",value ="`unmute a muted user`")
    help_embed.add_field(name="<:kick:848436025608372274> kick",value ="`Kick the mentioned user`")
    help_embed.add_field(name="<:unban:848436139983765524> Ban",value ="`Ban the mentioned user`")
    help_embed.add_field(name="<:force_ban:848436002183446548> Forceban",value ="`Ban a user not in the server`")
    #help_embed.add_field(name="<:volume_cyan:847976059600109628> Volume",value ="`Change the volume of the player`")
    help_embed.add_field(name="<:ban:848435959917707304> Unban",value ="`Unban a user`")
    help_embed.add_field(name="<:give_role:848435982546370580> Giverole",value ="`Add a role to user`")
    help_embed.add_field(name="<:remove_role:848436089088901141> takerole",value ="`Remove a role from user`")
    
    help_embed.set_footer(text=f"Type `>help <command name>` for more details about a command.")
    await interaction.response.send_message(embed=help_embed)
  
  elif args == "info":
    #help_embed.add_field(name="<:xs_prefix:848442391018864650> setprefix",value ="`Change the bot prefix for this server`")
    help_embed.add_field(name="<a:loading:847421396984135680> Stats",value ="`Get bot's current stats`")
    help_embed.add_field(name="<:whats_new:848443104591347742> new",value ="`Get the most recent changelog `")
    help_embed.add_field(name="<:contributers:848442304390103050> Contributors",value ="`Get the list of users that contributed in bot development`")
    help_embed.add_field(name="<:support:847767237883592724> Support",value ="`Join the support server`")
    help_embed.add_field(name="<:upvote_xs:848850824197439509> Upvote ",value ="`Upvote the bot`")
    help_embed.add_field(name="<:invite:848442326027730964> Invite",value ="`Get the bots invite link`")
    help_embed.add_field(name="<:announce:847767286685499433> Report",value ="`Report a bug or give feedback to developers`")
 
    
    help_embed.set_footer(text=f"Type `>help <command name>` for more details about a command.")
    await interaction.response.send_message(embed=help_embed)
  
  
  
    # If the argument is a command, get the help text from that command:
  elif args in command_names_list:
    help_embed.add_field(name="Guide",value="```\n<> = Required arguments\n() = Optional arguments\nDo not include brackets\n```",inline = False)
    
    help_embed.add_field(
    name="Description",
    value=f"```{bot.get_command(args).help}```",inline=False)
    
    if bot.get_command(args).aliases:
      help_embed.add_field(
      name="Aliases",
      value=f"```{bot.get_command(args).aliases}```")
    help_embed.add_field(
    name="Usage",
    value=f"```>{bot.get_command(args).usage}```")
    await interaction.response.send_message(embed=help_embed,emerphal=True)

 
    
 
  
                    
    # If someone is just trolling:
  else:
    help_embed.add_field(
    name="No command found",
    value=f"I dont have a command/module named {args}!")
    await interaction.response.send_message(embed=help_embed,emerphal=True)



  
@bot.slash_command(name="stats", description="Get the bots stats")
async def stats(interaction):
  """Get the current stats of bot"""
  process = psutil.Process(os.getpid())
  embed = nextcord.Embed(title="Bot info",color=0x69EBE4, description=(f"<:Xarvis_dev:847776388484038696> Developers: **NotGizzy#9481**\n\n<:ONLINE:847786717176135690> Live in: **{len(bot.guilds)} **Servers \n\n<a:loading:847421396984135680> Memory usage: **{round(process.memory_info().rss/1024/1024) *1}** mb! \n\n<:desktop_screen:847785552144629821> Cpu usage: **{psutil.cpu_percent()}**% \n\n<:waves:847767252979154944> Ram usage: **{psutil.virtual_memory().percent}**%\n\n<:latency:847781207999905802> Bot latency: **{round(bot.latency * 1000)}** ms\n\n<:Snow_info:847853879542022144> Version\: `0.4.2`"))
  embed.set_footer(text="Akio Copyright 2021®",icon_url=interaction.user.avatar)
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/867648204279513088/887994311218724874/20210916_091654.png")
    
  await interaction.response.send_message(embed=embed)
  

@bot.slash_command(name="load", description="load a cog file")
@commands.is_owner()
async def load(int, extension=SlashOption (name="extension", description="Provide a cog name", required=True)):
   bot.load_extension(f'cogs.{extension}')
   await int.response.send_message(f'Succesfully loaded **{extension}** module')

  
@bot.slash_command(name="unload", description="unload a cog file")
@commands.is_owner()
async def unload(int, extension=SlashOption (name="extension", description="Provide a cog name", required=True)):
   bot.unload_extension(f'cogs.{extension}')
   await int.response.send_message(f'Succesfully unloaded **{extension}** module')

@bot.slash_command(name="reload", description="Reaload a cog file")
@commands.is_owner()
async def reload(interaction, cog: str = SlashOption(name="cog", description="Provide a cog name", required=True)):
  bot.reload_extension(f'cogs.{cog}')
  await interaction.response.send_message(content=f'🔃 Succesfully reloaded **{cog}** module')
  


@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
     msg = 'This command is on cooldown, please try again in {:.2f}s'.format(error.retry_after)
     em = nextcord.Embed(title = "<:slowmode_time:862601700807933952> Cooldown", description = msg ,colour=0x69EBE4 )
     await ctx.send (embed = em)
  
  

    


   
bot.run(config.token)

