from nextcord import Embed, Color
from nextcord.ext import commands

from nextcord import slash_command, SlashOption

import json

class AFK(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author.bot:
            return

        with open("afk.json", "r") as file:
            afk = json.load(file)

        if str(msg.guild.id) not in afk:
            return

        if len(msg.mentions) > 0:
            user = msg.mentions[0]

        if user.id in afk[str(msg.guild.id)]["to-mention-ids"]:
            msgs = Embed(
                title=f"{user.name} is AFk",
                description=f"**{afk[str(msg.guild.id)][str(user.id)]}**",
                color=Color.blurple()
            )

            dm = Embed(
                title="Afk Notification alert",
                description=(f"{msg.author} mentioned you in {msg.channel.mention}\nReason you were afk:\n{afk[str(msg.guild.id)][str(user.id)]}"),
                color = msg.author.color)

            await user.send(embed=dm)
            await msg.reply(embed=msgs,mention_author=False)

        if msg.author.id in afk[str(msg.guild.id)]["to-mention-ids"]:
            index = afk[str(msg.guild.id)]["to-mention-ids"].index(msg.author.id)
            del afk[str(msg.guild.id)]["to-mention-ids"][index]

            afk[str(msg.guild.id)].pop(str(msg.author.id))

            with open("afk.json", "w") as dumps:
                json.dump(afk, dumps, indent = 4)

            await msg.channel.send(f"Welcome back {msg.author.mention}, I removed your AFK.",delete_after=5)

    @slash_command(name="afk",description="Let other know you are afk when you get pinged")
    async def afk(self, interaction : Interaction, message=SlashOption(name="input", description="This message shows when someone pings you")):
        with open("afk.json", "r") as file:
            afk = json.load(file)

        if not str(ctx.guild.id) in afk:
            afk[str(ctx.guild.id)] = {}

        if not str(ctx.author.id) in afk[str(ctx.guild.id)]:
            afk[str(ctx.guild.id)][str(ctx.author.id)] = {}

        if not "to-mention-ids" in afk[str(ctx.guild.id)]:
            afk[str(ctx.guild.id)]["to-mention-ids"] = []

        if not ctx.author.id in afk[str(ctx.guild.id)]["to-mention-ids"]:
            afk[str(ctx.guild.id)][str(ctx.author.id)] = message
            afk[str(ctx.guild.id)]["to-mention-ids"].append(ctx.author.id)

            with open("afk.json", "w") as dumps:
                json.dump(afk, dumps, indent = 4)

            await ctx.send(f"{ctx.author.mention}, I have set your AFK with reason : *_{message}_*",hidden=True)
        
        else:
            return

def setup(bot):
    bot.add_cog(AFK(bot))
