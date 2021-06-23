import discord
import traceback
import os
import asyncio
from discord.ext import commands
import random
from mcstatus import MinecraftServer
import sqlite3

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='<', intents=intents)
bot.remove_command("help")

count = 0
client = discord.Client()
bot_name = 'Anti-Gabe Bot'
smp = MinecraftServer("192.168.1.13", 25571)
modded = MinecraftServer("192.168.1.13", 25570)

curate_list = 'nsfw, gifs, words'
con = sqlite3.connect('counter.db')
cur = con.cursor()


@bot.event
async def on_ready():
    #if db not in db.get_tables():
    #    db.add_table('counter', column1='INT')
    print('Successfully booted ' + bot_name)
    await bot.change_presence(activity=discord.Game(name='1+1=3!'))
    #await dq_ping()


@bot.command()
async def options(ctx):
    embed = discord.Embed(
        title='Vibe Curation',
        description='Curate your vibe list to your likings!',
        colour=discord.Colour.purple()
    )
    embed.set_author(name=bot_name)
    embed.add_field(name='Words', value='All vibes in worded format', inline=False)
    embed.add_field(name='Gifs', value='All vibes in gif format', inline=False)
    embed.add_field(name='NSFW', value='Non-graphic language and adult-humor', inline=False)
    embed.add_field(name='Memes', value='Memes Galore!', inline=False)
    await ctx.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
    if hasattr(ctx.command, 'on_error'):
        return
    if isinstance(error, commands.CommandNotFound):
        return


@bot.command()
@commands.has_role('Admin')
async def restart_mod(ctx):
    os.system('tmux send -t 0:modded.1 stop ENTER')
    await asyncio.sleep(10)
    os.system('tmux send -t 0:modded.1 C-c')
    os.system('tmux send -t 0:modded.1 ./start.sh ENTER')
    await ctx.send("Sent restart command to modded server!")


@bot.command()
async def role(ctx, arg):
    author = ctx.message.author
    if arg.lower() == "amongus":
        await author.add_roles(discord.utils.get(author.guild.roles, name="Among Us"))
        await ctx.send("Among Us role has been applied!")
        return
    if arg.lower() == "rust":
        await author.add_roles(discord.utils.get(author.guild.roles, name="Rust"))
        await ctx.send("Rust role has been applied!")
        return
    if arg.lower() == "bots":
        await author.add_roles(discord.utils.get(author.guild.roles, name="Bots"))
        await ctx.send("Bot role has been applied!")
        return
    else:
        await ctx.send("Role request not recognized!")

"""
#@tasks.loop(hours=24)
async def dq_ping():
    channel = bot.get_channel(230087276967886850)
    while(True):
        print("Loop ran successfully")
        await channel.send('<@400286398575280158>, your vibe has been checked! <:patrickpingthrow:643614030933786636>')
        await asyncio.sleep(86400)
"""


@bot.event
async def on_member_join(member):
    await bot.get_channel(347239762798837761).send("Welcome {0.mention} to ClutchGaming, we hope you enjoy your time here!".format(member))
    await member.add_roles(discord.utils.get(member.guild.roles, name="Member"))


@bot.event
async def on_member_remove(member):
    await bot.get_channel(347239762798837761).send("Goodbye {0} {1}".format(member, bot.get_emoji(644734494502420490)))


@bot.command()
async def links(ctx):
    embed = discord.Embed(
        title='Links',
        description='All links relevant to ClutchGaming!',
        colour=discord.Colour.purple()
    )
    embed.set_author(name=bot_name)
    embed.add_field(name='Discord', value='https://discord.gg/BzFpan8', inline=False)
    embed.add_field(name='Website', value='https://store.clutchgaming.xyz', inline=False)
    embed.add_field(name='Survival', value='mc.clutchgaming.xyz', inline=False)
    embed.add_field(name='Modded', value='mod.clutchgaming.xyz', inline=False)
    await ctx.send(embed=embed)


# Help command for commands relating to Vibe Bot
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='Help List',
        description='All commands relevant to Vibe Bot!',
        colour=discord.Colour.dark_magenta()
    )
    embed.set_author(name=bot_name)
    embed.add_field(name='<vibe', value='Checks your vibe!', inline=False)
    embed.add_field(name='<ping', value='Ping to test status of Vibe Bot!', inline=False)
    embed.add_field(name='<fetchbutter', value='Fetches you some butter!', inline=False)
    embed.add_field(name='<role <role>', value='Get a role to get notifications of our updates! Available roles: Minecraft, Rust and Bots', inline=False)
    embed.add_field(name='<vibesug msg', value='Have a vibe suggestion? Run the command with your suggestion afterwards! E.g > <vibesug This bot is gucci gang', inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    #await ctx.send("test")
    embed = discord.Embed(
        title='ClutchGaming',
        description='Health and Status of our Servers!',
        colour=discord.Colour.green()
    )
    embed.set_author(name=bot_name)
    embed.add_field(name='Survival', value='Ping = {0} ms'.format(smp.ping()), inline=False)
    embed.add_field(name='Modded', value='Ping = {0} ms'.format(modded.ping()), inline=False)
    #embed.add_field(name='Hypixel', value='Ping = {0}'.format(hypixel.ping()), inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def iwannadateyou(ctx):
    await ctx.send('Wanna date? Here is my number: (605)-475-6968')


# For testing purposes, specifically pertaining to database modifications
@bot.command()
async def database_commands(ctx):
    if ctx.message.author.id == 169554013837066241:
        cur.execute("UPDATE vibecount SET count = count+1")
        cur.execute("SELECT count FROM vibecount")
        print(cur.fetchone()[0])
        con.commit()
        await ctx.send("Cmd run gut")
        return
    await ctx.send("No sir, yer neer to be murr")


@bot.command()
async def fetchbutter(ctx):
    await ctx.send(':butter:')


bot.run('')
