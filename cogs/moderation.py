import traceback

import discord
from discord.ext import commands

from logging_files.moderation_logging import logger

from discord_components import *
import discord_slash
from discord_slash.utils.manage_commands import create_option

from discord_components import DiscordComponents, Button
from discord_slash import cog_ext, SlashContext


class Moderation(commands.Cog):

    def __init__(self, bot):
      self.bot = bot
      
      bot.embed_color = 0x69EBE4
      bot.error_color = 0xED4245
    
    
      
      
      
    @cog_ext.cog_slash(name="mute", description="mute a user in the server",options=[create_option(name="member", description="Mention the user you want to mute",option_type=6,required=True)])
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(manage_roles=True)
    
    async def mute(self, ctx, member: discord.Member, *, reason: str = None):
      """Mute the mentioned user from chat and vc"""
      muted_role = next((g for g in ctx.guild.roles if g.name == "Muted"), None)
      if not muted_role:
        return await ctx.send("I cannot find the role **Muted**? Make sures its existing",hidden=True)
      if ctx.guild.me.top_role < member.top_role:
        embed = discord.Embed(
        color=self.bot.error_color,
        title="<:broken_circle:847776660174274580> Unsuccessful Operation",
        description="• The target user has higher permissions/role than me")
        await ctx.send(embed=embed,hidden=True)
      elif ctx.author.top_role <= member.top_role and ctx.author.id != ctx.guild.owner.id:
        embed = discord.Embed(
        color=self.bot.error_color,
        title="<:broken_circle:847776660174274580> Unsuccessful Operation",
        description="• The target user has higher permissions than you or equal permissions as you",hidden=True)
         
        await ctx.send(embed=embed)
      elif muted_role in member.roles:
        await ctx.send(f"{member.name} is already muted",hidden=True)
      elif ctx.guild.me.top_role > member.top_role:
        
        await member.add_roles(muted_role)
        embed = discord.Embed(
        color=self.bot.embed_color,
        title="<:muted:848436041656434708> Action Successful", description=f"• {member.mention} has been **Muted**")
        await ctx.send(embed=embed)
        
    @mute.error
    async def mute_error(self, ctx, error):
      if isinstance(error, commands.BadArgument):
          embed = discord.Embed(
          color=self.bot.error_color,
          title="<:warn:847767343395373097> Invalid Member",
          description="• Please supply a valid member \nExample: `>mute @user`")
          await ctx.send(embed=embed)
      elif isinstance(error, commands.MissingRequiredArgument):
          embed = discord.Embed(
          color=self.bot.error_color,
          title="<:warn:847767343395373097> Invalid Arguments provided",
          description="• Please supply a valid argument\nExample: `>mute @user`"
            )
          await ctx.send(embed=embed)
      elif isinstance(error, commands.MissingPermissions):
          embed = discord.Embed(
          color=self.bot.error_color,
          title="<:warn:847767343395373097> You are Missing Permissions",description=f"• You do not have the `{error.missing_perms[0]}` permission to run this command!")
          await ctx.send(embed=embed)
      elif isinstance(error, commands.BotMissingPermissions):
          embed = discord.Embed(
          color=self.bot.error_color,
          title="<:warn:847767343395373097> Bot is Missing Permissions!",
          description=f"• I'm missing **`{error.missing_perms[0]}`** permission to use this command")
          await ctx.send(embed=embed)

    
    
    @cog_ext.cog_slash(name="unmute", description="Unmute a muted user",options=[create_option(name="member", description="Mention a user to unmute",option_type=6,required=True)])
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(manage_roles=True)
    
    async def unmute(self,ctx, *, member: discord.Member , reason: str = None):
      '''Unmute a user'''
      muted_role = next((g for g in ctx.guild.roles if g.name == "Muted"), None)
      if member == ctx.author and muted_role in ctx.author.roles:
        await ctx.reply("You cannot unmute yourself.",hidden=True)
      else:
        await member.remove_roles(muted_role)
        embed = discord.Embed(
        color=self.bot.embed_color,
        title="<:umuted:848436114917425162> Action Successful",
        description=f"• {member.mention} has been **Unmuted** 🔈")
        await ctx.send(embed=embed)
         
    
  

    @cog_ext.cog_slash(name="giverole", description="Add a role to a user",options=[create_option(name="role", description="Mention the role",option_type=8,required=True),create_option(name="member", description="Mention the member",option_type=6,required=True)])
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def giverole(self, ctx, role: discord.Role, member: discord.Member,):
      """Assgin a role to user"""
      if ctx.guild.me.top_role < member.top_role:
        embed = discord.Embed(
        color=self.bot.embed_color,
        title="<:broken_circle:847776660174274580> Unsuccessful Operation",
        description="• The user has higher permissions/role than me")
        await ctx.send(embed=embed,hidden =True)
      elif ctx.author.top_role <= member.top_role and ctx.author.id != ctx.guild.owner.id:
          embed = discord.Embed(
          color=self.bot.embed_color,
          title="<:broken_circle:847776660174274580> Unsuccessful Operation",
          description="• The user has higher permissions or equal permissions than you" )
          await ctx.send(embed=embed, hidden=True)
      elif ctx.guild.me.top_role > member.top_role:
          await member.add_roles(role)
          embed = discord.Embed(
          color=self.bot.embed_color,
          title="<:give_role:848435982546370580> Action Success",
          description=f"• {member.mention} Has been given the role `{role}`")

          await ctx.send(embed=embed)

          logger.info(f"Moderation | Sent Addrole: {ctx.author} | Role added: {role} | To: {member}")
      else:
        traceback.print_exc()

    @giverole.error
    async def giverole_error(self, ctx, error):
      if isinstance(error, commands.BadArgument):
          embed = discord.Embed(
          color=self.bot.error_color,
          title="<:warn:847767343395373097> Invalid Role / Member!",
          description="• Please Supply a valid role / member! \nExample: `>addrole <role ID / @role> @user`")
          await ctx.send(embed=embed)
      elif isinstance(error, commands.MissingRequiredArgument):
          embed = discord.Embed(
          color=self.bot.error_color,
          title="<:warn:847767343395373097> Invalid Arguments provided",
          description="• Please supply a valid option!\nExample: `>addrole <Role ID / Rolename> @user`"
            )
          await ctx.send(embed=embed)
      elif isinstance(error, commands.MissingPermissions):
          embed = discord.Embed(
          color=self.bot.error_color,
          title="<:warn:847767343395373097> Missing Permissions",description="• You do not have the required permission(s) to run this command!")
          await ctx.send(embed=embed)
      elif isinstance(error, commands.BotMissingPermissions):
          embed = discord.Embed(
          color=self.bot.error_color,
          title="<:warn:847767343395373097> Bot is Missing Permissions",
          description=f"• I'm missing **`{error.missing_perms[0]}`** permission to use this command")
          await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="ban", description="Ban a user from the server",options=[create_option(name="member", description="Mention the user to ban",option_type=6,required=True)])
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason provided"):
      """Ban the mentioned user"""
      if ctx.guild.me.top_role < member.top_role:
        embed = discord.Embed(
        color=self.bot.error_color,
        title="<:broken_circle:847776660174274580> Unsuccessful Operation",
        description="• The target user has higher permissions/role than me",hidden=True)
        await ctx.send(embed=embed)
      elif ctx.author.top_role <= member.top_role and ctx.author.id != ctx.guild.owner.id:
        embed = discord.Embed(
        color=self.bot.error_color,
        title="<:broken_circle:847776660174274580> Unsuccessful Operation",
        description="• The target user has higher permissions than you or equal permissions as you",hidden=True
            )
        await ctx.send(embed=embed)
      elif ctx.guild.me.top_role > member.top_role:
        embed = discord.Embed(
        color=self.bot.embed_color,
        title="<:unban:848436139983765524> Action successful",
        description=f"• {member.mention} has been **Banned!** Bye bye! :wave:")

        sender = ctx.author
        await member.ban(reason=reason)

        await ctx.send(embed=embed)
        try:

          embed2 = discord.Embed(
          color=self.bot.embed_color,
          title=f"{member} You Have Been Banned!")
          embed2.add_field(name=f"• Moderator", value=f"{sender}")
          embed2.add_field(name="• Reason", value=f"{reason}")
          embed2.set_footer(text=f"Banned from: {ctx.guild}")

          await member.send(embed=embed2)
        except:
          return
 
        logger.info(f"Moderation | Sent Ban: {ctx.author} | Banned: {member} | Reason: {reason}")
      else:
        traceback.print_exc()

    @ban.error
    async def ban_error(self, ctx, error):
      if isinstance(error, commands.BadArgument):
        embed = discord.Embed(
        color=self.bot.error_color,
        title="<:warn:847767343395373097> Invalid Member",
        description="• Please mention a valid member Example: `>ban @user / userid [reason]`"
            )
        await ctx.send(embed=embed)
      elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
        color=self.bot.error_color,
        title="<:warn:847767343395373097> Invalid Argument",
        description="• Please supply a valid option! Example: `>ban @user / userid [reason]`")
        await ctx.send(embed=embed)
      elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
        color=self.bot.error_color,
        title="<:warn:847767343395373097> Missing Permissions",
        description="• You do not have the needed permissions to run this command!")
        await ctx.send(embed=embed)
      elif isinstance(error, commands.BotMissingPermissions):
        embed = discord.Embed(
        color=self.bot.error_color,
        title="<:warn:847767343395373097> Bot is Missing Permissions",
        description=f"I'm missing **`{error.missing_perms[0]}`** permission to use this command")
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="nickname", description="Change a user's nickname",options=[create_option(name="member", description="Mention the user",option_type=6,required=True),create_option(name="nick", description="New nickname",option_type=3, required=True)])
    @commands.has_permissions(manage_nicknames=True)
    @commands.bot_has_permissions(manage_nicknames=True)
    async def nickname(self, ctx, member: discord.Member, *, nickname):
      """Change the mentioned user's nickname"""
      if ctx.guild.me.top_role < member.top_role:
        embed = discord.Embed(
        color=self.bot.error_color,
        title="<:broken_circle:847776660174274580> Unsuccessful Operation",
        description="• The target user has higher permissions than me!"
            )
        await ctx.send(embed=embed)
      elif ctx.author.top_role <= member.top_role and ctx.author.id != ctx.guild.owner.id:
        embed = discord.Embed(
        color=self.bot.error_color,
        title="<:broken_circle:847776660174274580> Unsuccessful operation",
        description="• The target user has higher permissions than you or equal permissions as you"
            )
        await ctx.send(embed=embed)
      elif ctx.guild.me.top_role > member.top_role:
        embed = discord.Embed(
        color=self.bot.ember_color,
        title="<:nickname:848436062845927435> Action Successful",
        description=f"• {member.name}'s Nickname has been **Changed!**"
            )

        await member.edit(nick=nickname)
        await ctx.send(embed=embed)

        logger.info(f"Moderation | Sent Change Nickname: {ctx.author} | Nickname: {nickname} | To: {member}")
      else:
        traceback.print_exc()

    @nickname.error
    async def nickname_error(self, ctx, error):
      if isinstance(error, commands.BadArgument):
        embed = discord.Embed(
        color=self.bot.error_color,
        title="<:warn:847767343395373097> Invalid Member",
        description="• Please mention a valid member Example: `>nickname @user / userid <nickname>`")
        await ctx.send(embed=embed)
      elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
        color=self.bot.error_color,
        title="<:warn:847767343395373097> Invalid Arguments provided",
        description="• Please supply a valid option Example: `>nickname @user / userid name`")
        await ctx.send(embed=embed)
      elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
        color=self.bot.error_color,
        title="<:warn:847767343395373097>You are Missing Permissions",
        description="• You do not have permissions to run this command"
            )
        await ctx.send(embed=embed)
      elif isinstance(error, commands.BotMissingPermissions):
        embed = discord.Embed(
        color=self.bot.error_color,
        title="<:warn:847767343395373097> Bot Missing Permissions!",
        description=f"• I'm missing **`{error.missing_perms[0]}`** permission to use this command"
            )
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="forceban", description="Ban a user not currently in server",options=[create_option(name="id", description="Mention the userid",option_type=3,required=True)])
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def forceban(self, ctx, *, id: int):
      """Ban a user who is not in the server"""
      await ctx.guild.ban(discord.Object(id))
      embed = discord.Embed(
      color=self.bot.embed_color,
      title="<:force_ban:848436002183446548> Action Successful",
      description=f"<@{id}> → has been **Forcefully banned!** Bye bye! :wave:")

      await ctx.send(embed=embed)

      logger.info(f"Moderation | Sent Force Ban: {ctx.author} | Force Banned: {id}")

    @forceban.error
    async def forceban_error(self, ctx, error):
      if isinstance(error, commands.BadArgument):
        embed = discord.Embed(
        color=self.bot.error_color,
        title="<:warn:847767343395373097> Invalid ID!",
        description="• Please use a valid Discord ID! Example: `>forceban <ID>`")
        await ctx.send(embed=embed)
      elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
        color=self.bot.error_color,
        title="<:warn:847767343395373097> Invalid Argument!",
        description="• Please supply a valid argument! Example: `>forceban <ID>`")
        await ctx.send(embed=embed)
      elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
        color=self.bot.embed_color,
        title="<:warn:847767343395373097> Missing Permissions",
        description="• You do not have permissions to run this command!")
        await ctx.send(embed=embed)
      elif isinstance(error, commands.BotMissingPermissions):
        embed = discord.Embed(
        color=self.bot.embed_color,
        title="<:warn:847767343395373097> Bot is Missing Permissions!",
        description=f"• I'm missing **`{error.missing_perms[0]}`** permission to use this command"
            )
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="kick", description="Kick a user from the server",options=[create_option(name="member", description="Mention the user to kick",option_type=6,required=True)])
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason provided"):
        """Kick the mentioned user from the server"""
        if ctx.guild.me.top_role < member.top_role:
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:broken_circle:847776660174274580> Unsuccessful Operation",
                description="• The user has higher permissions than me"
            )
            await ctx.send(embed=embed)
        elif ctx.author.top_role <= member.top_role and ctx.author.id != ctx.guild.owner.id:
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:broken_circle:847776660174274580> Unsuccessful Operation",
                description="• The user has higher permissions than you or equal permissions as you",hidden=True
            )
            await ctx.send(embed=embed)
        elif ctx.guild.me.top_role > member.top_role:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="<:kick:848436025608372274> Action Successful",
                description=f"• {member.mention} has been **kicked!** Bye bye! :wave:"
            )
            sender = ctx.author
            await member.kick(reason=reason)

            await ctx.send(embed=embed)
          

            embed2 = discord.Embed(
                color=self.bot.embed_color,
                title=f"{member} → You have been kicked!"
            )
            embed2.add_field(name=f"• Moderator", value=f"{sender}")
            embed2.add_field(name="• Reason", value=f"{reason}")
            embed2.set_footer(text=f"Kicked from: {ctx.guild}")
            try:
              await member.send(embed=embed2)
            except:
              return 
              
            logger.info(f"Moderation | Sent Kick: {ctx.author} | Kicked: {member} | Reason: {reason}")
        else:
            traceback.print_exc()

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:warn:847767343395373097> Invalid Member!",
                description="• Please mention a valid member! Example: `>kick @user/ userid [reason]`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:warn:847767343395373097> Invalid Argument!",
                description="• Please supply a valid option! Example: `l!kick @user [reason]`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:warn:847767343395373097> You are Missing Permissions",
                description="• You do not have permissions to run this command!"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:warn:847767343395373097> Bot is Missing Permissions!",
                description=f"• I'm missing **`{error.missing_perms[0]}`** permission to use this command"
            )
            await ctx.send(embed=embed)
        else:
            raise error

    @cog_ext.cog_slash(name="purge", description="Purge messages",options=[create_option(name="amount", description="Mention the amount of messages to purge",option_type=4  ,required=True)])
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        """purge the mentioned amount of message from the chat"""
        await ctx.channel.purge(limit=amount+1)

        logger.info(f"Moderation | Sent Purge: {ctx.author} | Purged: {amount} messages")

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:warn:847767343395373097> Invalid Amount",
                description="• Please supply a valid number! Example: `>purge <number>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:warn:847767343395373097> Invalid Argument!",
                description="• Please supply a valid option Example: `>purge <number>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:warn:847767343395373097> Missing Permissions",
                description="• You do not have permissions to run this command!"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:warn:847767343395373097> Bot Missing Permissions!",
                description=f"• I'm missing **`{error.missing_perms[0]}`** permission to use this command"
            )
            await ctx.send(embed=embed)

    @commands.command(aliases=["removerole", "delrole"],usage="removerole <roleid/@role> <user>")
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def takerole(self, ctx, role: discord.Role,*, member: discord.Member,):
        """Remove a role from user"""
        if ctx.guild.me.top_role < member.top_role:
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:broken_circle:847776660174274580> Unsuccessful Operation",
                description="• The target user has higher permissions than me"
            )
            await ctx.send(embed=embed)
        elif ctx.author.top_role <= member.top_role and ctx.author.id != ctx.guild.owner.id:
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:broken_circle:847776660174274580> Unsuccessful",
                description="• The target user has higher permissions than you or equal permissions as you"
            )
            await ctx.send(embed=embed)
        elif ctx.guild.me.top_role > member.top_role:
            await member.remove_roles(role)
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="<:remove_role:848436089088901141> Action Successful",
                description=f"• {member.mention} has been removed from the role `{role}`"
            )

            await ctx.send(embed=embed)

            logger.info(f"Moderation | Sent Remove Role: {ctx.author} | Removed Role: {role} | To: {member}")
        else:
            traceback.print_exc()

    @takerole.error
    async def takerole_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:warn:847767343395373097> Invalid Role / Member!",
                description="• Please supply a valid role / member! Example: `>takerole <role ID / rolename> @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:warn:847767343395373097> Invalid Argument!",
                description="• Please supply a valid option! Example: `>takerole <Role ID / Rolename> @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:warn:847767343395373097> You are Missing Permissions",
                description="• You do not have permissions to run this command!"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:warn:847767343395373097> Bot is Missing Permissions!",
                description=f"• I'm missing **`{error.missing_perms[0]}`** permission to use this command"
            )
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    @commands.bot_has_permissions(manage_nicknames=True)
    async def resetnick(self, ctx, member: discord.Member):
        if ctx.guild.me.top_role < member.top_role:
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:broken_circle:847776660174274580> Unsuccessful Operation",
                description="• The user has higher permissions than me"
            )
            await ctx.send(embed=embed)
        elif ctx.author.top_role <= member.top_role and ctx.author.id != ctx.guild.owner.id:
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:broken_circle:847776660174274580> Unsuccessful Operation",
                description="• The user has higher permissions than you or equal permissions as you"
            )
            await ctx.send(embed=embed)
        elif ctx.guild.me.top_role > member.top_role:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="<:nickname:848436062845927435> Action Successful",
                description=f"• {member.mention}'s Nickname has been **Reset!**"
            )

            await member.edit(nick=None)
            await ctx.send(embed=embed)

            logger.info(f"Moderation | Sent Reset Nickname: {ctx.author} | To: {member}")
        else:
            traceback.print_exc()

    @resetnick.error
    async def resetnick_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:warn:847767343395373097> Invalid Member!",
                description="• Please mention a valid member Example: `>resetnick @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="<:warn:847767343395373097> Invalid Argument!",
                description="• Please supply a valid option Example: `>resetnick @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="<:warn:847767343395373097> You are Missing Permissions!",
                description="• You do not have permissions to run this command!"
            )

            await ctx.send(embed=embed)
          
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="<:warn:847767343395373097> Bot is Missing Permissions!",
                description=f"• I'm missing **`{error.missing_perms[0]}`** permission to use this command"
            )
            await ctx.send(embed=embed)
        else:
            traceback.print_exc()

    @cog_ext.cog_slash(name="unban", description="Unaban a user from the server",options=[create_option(name="id", description="Mention the userid",option_type=4 ,required=True)])
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self, ctx, *, id: int):
        """unban a user from server"""
        await ctx.guild.unban(discord.Object(id))
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="<:unban:848436139983765524> Action Successful",
            description=f"<@{id}> → has been **Unbanned!** Welcome back! :wave:"
        )
        await ctx.send(embed=embed)

        logger.info(f"Moderation | Sent Unban: {ctx.author} | Unbanned: {id}")

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:warn:847767343395373097> Invalid ID!",
                description="• Please use a valid Discord ID! Example: `>unban <ID>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:warn:847767343395373097> Invalid Argument!",
                description="• Please supply a valid Discord ID! Example: `>unban 546812331213062144`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:warn:847767343395373097> You are Missing Permissions",
                description="• You do not have permissions to run this command!"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                color=self.bot.error_color,
                title="<:warn:847767343395373097> Bot Missing Permissions!",
                description=f"• I'm missing **`{error.missing_perms[0]}`** permission to use this command"
            )
            await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Moderation(bot))
    print("Moderation module Ready to be loaded")