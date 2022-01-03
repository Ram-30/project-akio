from nextcord import Embed, Color, Intents
import config

import os
import asyncio
from googletrans import Translator

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=">", case_insensitive=True, intents=intents)
bot.remove_command("help")  

@tasks.loop(seconds=30)
async def status_change():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=(f"{len(bot.users)} members | {len(bot.guilds)} servers")))     
    await asyncio.sleep(30)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=(">help")))

@bot.event 
async def on_ready():
    print(f'Logged in as {bot.user} in {len(bot.guilds)} guilds with total {len(bot.users)} users.')

@bot.event
async def on_message(message):
    if bot.user in message.mentions:
        return await message.channel.send(f"Hello I am Akio :wave: You can use my commands through slash commands.")

    elif message.content.startswith(">") and message.author.bot:
        embed = Embed(
            title="Hello there, Trying to use commands?",
            description="""
            Akio was recently migrated to slash commands!
            All commands **Excluding nsfw commands** will only work via slash commands!

            Cannot see/use slash commands?
            Make sure to reinvite the bot by [clicking here](https://discord.com/oauth2/authorize?client_id=732119152885497867&permissions=8&scope=applications.commands%20bot)

            Need help? Join the support server by [clicking here](https://discord.gg/TbhN3ye9cC)]""",
            color=Color.blurple())

        embed.set_footer(text="Akio development team", icon_url= bot.user.avatar.url)
        return await ctx.send(embed=embed)
    await bot.process_commands(message)

async def startup():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and not filename.startswith("_"):
            try:
                bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded {filename[:-3]}')
            except Exception as e:
                print(f'Faield to load {filename[:-3]} due to {e}')

    bot.load_extension("jishaku")

    status_change.before_loop(bot.wait_until_ready)
    status_change.start()

    bot.developers = config.developers
    bot.owner_ids = config.owners
    bot.topgg_token = config.topgg_token
    bot.translator = Translator()

    async with aiohttp.CilentSession as session:
        bot.session = session
        bot.run(config.token)

asyncio.run(startup())