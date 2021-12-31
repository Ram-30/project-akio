	import asyncio
	import discord
	import random
	from discord.ext import commands
	from cogs import DL
	import urllib
	from utils import permissions
	import requests
	import json
	import typing
	import aiohttp
	import discord_slash
	from discord_slash.utils.manage_commands import create_option

	from discord_components import DiscordComponents, Button
	from discord_slash import cog_ext, SlashContext


	class utils(commands.Cog):
		def __init__(self, bot):
			self.bot = bot

		@cog_ext.cog_slash(name="bigemote", description="Get the bigger version of a emote",options=[create_option(name="emoji", description="Type the emote",option_type=3 ,required=True)])
		async def bigemote(self, ctx, emoji):
			"""Make a certain emote bigger"""
			try:
				if emoji[0] == '<':
					name = emoji.split(':')[1]
					emoji_name = emoji.split(':')[2][:-1]
					anim = emoji.split(':')[0]
					if anim == '<a':
						url = f'https://cdn.discordapp.com/emojis/{emoji_name}.gif'
					else:
						url = f'https://cdn.discordapp.com/emojis/{emoji_name}.png'
					try:
						await ctx.send(url)
					except Exception as e:
						print(e)
						resp = await self.bot.session.get(url) as
						if resp.status not in (200, 204):
							return await ctx.send('```Error: Emote not found.```')
						img = await resp.read()

						kwargs = {'parent_width': 1024, 'parent_height': 1024}
						convert = False
						task = functools.partial(bigEmote.generate, img, convert,
												**kwargs)
						task = self.bot.loop.run_in_executor(None, task)
						try:
							img = await asyncio.wait_for(task, timeout=15)
						except asyncio.TimeoutError:
							await ctx.send(
								"```Error: Timed Out. Try again in a few seconds")
							return
						await ctx.send(
							file=discord.File(img, filename=name + '.png'))

			except Exception as e:
				await ctx.send(f"```Error, couldn't send emote. Please tell my bot master\n{e}```")
		
		
		@commands.command(pass_context=True, no_pm=True)
		async def ascii(self, ctx, *, text: str = None):
			"""Beautify some text (font list at http://artii.herokuapp.com/fonts_list)."""

			if text == None:
				await ctx.channel.send(
					'Usage: `ascii [font (optional)] [text]`\n(font list at http://artii.herokuapp.com/fonts_list)'
				)
				return

			# Get list of fonts
			fonturl = "http://artii.herokuapp.com/fonts_list"
			response = await DL.async_text(fonturl)
			fonts = response.split()

			font = None
			# Split text by space - and see if the first word is a font
			parts = text.split()
			if len(parts) > 1:
				# We have enough entries for a font
				if parts[0] in fonts:
					# We got a font!
					font = parts[0]
					text = ' '.join(parts[1:])

			url = "http://artii.herokuapp.com/make?{}".format(
				urllib.parse.urlencode({'text': text}))
			if font:
				url += '&font={}'.format(font)
			response = await DL.async_text(url)
			await ctx.channel.send("```Markup\n{}```".format(response))

		@commands.command(usage="embed (channel)")
		@commands.has_permissions(manage_messages=True)
		async def embed(self, ctx, channel: discord.TextChannel = None):
			"""Interactive Embed maker"""
			if channel == None:
				channel = ctx.channel

			def check(message):
				return message.author == ctx.author and message.channel == ctx.channel

			await ctx.send('Type the title below')

			title = await self.bot.wait_for('message', check=check)

			await ctx.send('Type the description below')

			desc = await self.bot.wait_for('message', check=check)

			#await ctx.send('Tyoe the color Hexcode , for random color type `Skip`')

			#color = await self.bot.wait_for('message', check=check)

			embed = discord.Embed(title=title.content,
								description=desc.content,
								color=0x72d345)
			#else:
			#embed = discord.Embed(title=title.content, description=desc.content, color=colorctx.send('Type the Footer , type `skip` to skip')
			footer = await self.bot.wait_for('message', check=check)

			if footer.content.lower() == "skip":
				await channel.send(embed=embed)
			else:
				embed.set_footer(text=footer.content)
				await channel.send(embed=embed)

		@cog_ext.cog_slash(name="whois", description="Get information about a member",options=[create_option(name="member", description="Mention the user",option_type=6,required=True)])
		
		async def whois(self, ctx, member = None):
			"""Get information about the mentioned user"""
			if not member:
				member = ctx.message.author  # set member as the author
			roles = [role for role in member.roles[1:]]
			embed = discord.Embed(color=ctx.author.color, title=f" {member}'s info")
			embed.set_thumbnail(url=member.avatar_url)
			embed.set_footer(text=f"{member.name}")
			embed.add_field(name="<:id:847775640743837697> User's name:",
							value=member.name)
			embed.add_field(name="<:cc_card:847854492879552522> User's ID:",
							value=member.id)
		#	embed.add_field(name="<:online_status:847786717176135690> **Status:**"  value=str(member.status).replace  "dnd", "Do Not Disturb") ,inline=True)
			embed.add_field(
				name="<:calender:847791916279267339> Account created on:",
				value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
			embed.add_field(
				name="<:stats:847776840311242832> Joined Server On:",
				value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
			embed.add_field(name="<:hypesquad:847776416396607488> Roles:",
							value=" ".join([role.mention for role in roles]))
			embed.add_field(name="Highest Role:", value=member.top_role.mention)
			perm_string = ', '.join([
				str(p[0]).replace("_", " ").title()
				for p in member.guild_permissions if p[1]
			])
			embed.add_field(name="Guild permissions", value=perm_string, inline=False)
			if member.id == ctx.guild.owner_id:
				embed.add_field(name='<:mod:847767322156335135> Acknowledgements',
								value='Server Owner')
			elif member.id in permissions.owners:
				embed.add_field(name='<:mod:847767322156335135> Acknowledgements',
								value='Akio Bot Developer')
			elif member.id == 848878186439639050:
				embed.add_field(name='<:mod:847767322156335135> Acknowledgements',
								value='It is Me!')

			elif member.guild_permissions.administrator:
				embed.add_field(name='<:mod:847767322156335135> Acknowledgements',
								value='Server Administrator')
			elif member.guild_permissions.manage_guild:
				embed.add_field(name=' <:mod:847767322156335135> Acknowledgements',
								value='Server Manager')
			elif member.id in permissions.cont:
				embed.add_field(name='<:mod:847767322156335135> Acknowledgements',   value='Akio Bot Contributor')

			await ctx.send(embed=embed)

		@cog_ext.cog_slash(name="serverinfo", description="Get information about the server")
		
		@commands.guild_only()
		async def serverinfo(self, ctx):
			""" Check info about current server """
			if ctx.invoked_subcommand is None:
				findbots = sum(1 for member in ctx.guild.members if member.bot)
			embed = discord.Embed(colour=ctx.author.color)
			if ctx.guild.icon:
				embed.set_thumbnail(url=ctx.guild.icon_url)
			if ctx.guild.banner:
				embed.set_image(url=ctx.guild.banner_url_as(format="png"))

			embed.add_field(name="<:id:847775640743837697> Server Name",
							value=ctx.guild.name,
							inline=False)
			embed.add_field(name="<:stats:847776840311242832> Server ID",
							value=ctx.guild.id,
							inline=False)
			embed.add_field(name="<:mod:847767322156335135> Owner",
							value=ctx.guild.owner,
							inline=False)
			embed.add_field(name="<:globe_lines:848575865524191232> Server Region",
							value=ctx.guild.region,
							inline=False)
			embed.add_field(name="<:calender:847791916279267339> Date of creation",
							value=ctx.guild.created_at,
							inline=False)
			embed.add_field(name="<:contributers:848442304390103050> Members",
							value=ctx.guild.member_count,
							inline=False)
			await ctx.send(embed=embed)

		@cog_ext.cog_slash(name="avatar", description="Get a user's avatar",options=[create_option(name="user", description="Mention the user",option_type=6,required=False)])
		@commands.guild_only()
		async def avatar(self, ctx, *, user: discord.Member = None):
			""" Get the avatar of you or someone else """
			user = user or ctx.author
			embed = discord.Embed(
				title=(f"{user.name}'s Avatar"),
				description=(
					f"[Click here if the image doesn't load]({user.avatar_url})"),
				color=ctx.author.color)
			embed.set_image(url=user.avatar_url)
			await ctx.send(embed=embed)

		@cog_ext.cog_slash(name="define", description="Get defination of a word from ud",options=[create_option(name="term", description="Mention the term",option_type= 3,required=True)])
		
		async def define(self, ctx, index: typing.Optional[int] = 0, *, term: str):
			"""Look up definition of a word on urban dictionary"""
			try:
				resp = await self.bot.session.get("https://api.urbandictionary.com/v0/define",params={"term": term})
				result = await r.json()
			data = result["list"][index]
			defin = data["definition"]
			
			if "2." in defin:
				defin == ["definition"].splisplit("2.")
				defin = defin[0]
			elif len(defin) > 250:
				defin = defin[:250]
			example = data["example"]
			if "2." in defin:
				example = data["example"].split("2.")
				example = example[0]
			elif len(example) > 250:
				example = example[:250]
			
			urban_embed = discord.Embed(title="Result for {0}".format(term),url=data["permalink"],colour=ctx.author.color)
			urban_embed.add_field(name="Definition", value=defin, inline=False)
			urban_embed.add_field(name="Example",value=example or "N/A",inline=False)
			urban_embed.set_footer(text="Author: " + data["author"])
			await ctx.send(embed=urban_embed)
			return  # Halts further action
			except:
			return await ctx.reply("> Couldn't find that word")
	
	
	
		@cog_ext.cog_slash(name="inrole", description="Get list of users in a role",options=[create_option(name="role", description="Mention the role",option_type=8 ,required=True)])
		async def inrole(self, ctx, *, role: discord.Role):
			'''Get list of users in a role'''
			embed = discord.Embed(title=f"{role.name} ({len(role.members)} users)",
								description=("\n".join(map(str, role.members))),
								color=role.color)
			await ctx.send(embed=embed)

		@inrole.error
		async def inrole_error(self, ctx, error):
			if isinstance(error, commands.BadArgument):
				embed = discord.Embed(
					color=self.bot.error_color,
					title="<:warn:847767343395373097> Invalid Argument!",
					description=
					"• Please provide a valid role! \nExample: `xs!inrole <role>`")
				await ctx.send(embed=embed)

		@cog_ext.cog_slash(name="topic", description="Get channel topic of a channel",options=[create_option(name="args", description="Mention a channel",option_type=7 ,required=False)])
		async def topic(self, ctx, args=None):
			'''Send the channel topic of current channel or Mentioned channel'''
			m = args    
			embed = discord.Embed(title="Channel topic", description=(f"{m.topic}"), color=0x9ef0f4)
			if m.topic == None:
				await ctx.send(f"**{m.name} has no topic**")
			else:
				await ctx.send(embed=embed)
				await ctx.message.delete()

		@commands.command(usage="role <rolename/id>")
		async def role(self, ctx, *, msg):
			"""Get info about a role"""
			if not msg:
				return await ctx.send(
					"`Invalid argument` Please provide a rolename or roleid")
			guild = ctx.message.guild
			guild_roles = ctx.message.guild.roles
			for role in guild_roles:
				if msg.lower() == role.name.lower() or msg == role.id:
					all_users = [str(x) for x in role.members]
					all_users.sort()
					all_users = ', '.join(all_users)
					em = discord.Embed(title='Role Info', color=role.color)
					em.add_field(name='Name', value=role.name)
					em.add_field(name='ID', value=role.id, inline=False)
					em.add_field(name='Users in this role',
								value=str(len(role.members)))
					em.add_field(name='Role color hex value',
								value=str(role.color))
					em.add_field(name='Role color RGB value',
								value=role.color.to_rgb())
					em.add_field(name='Mentionable', value=role.mentionable)
					em.add_field(name='Created at',
								value=role.created_at.__format__('%x at %X'))
					em.set_thumbnail(url='http://www.colorhexa.com/{}.png'.format(
						str(role.color).strip("#")))
					if len(role.members) == 0:
						em.add_field(name='All users',
									value=all_users,
									inline=False)
					return await ctx.send(embed=em)
			

	
		
	def setup(bot):
		bot.add_cog(utils(bot))
		print("Utility module Ready to be loaded")
