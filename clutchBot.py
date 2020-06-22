import discord
import asyncio
from discord.ext import commands
import random
from mcstatus import MinecraftServer

bot = commands.Bot(command_prefix='<', case_insensitive=True)

client = discord.Client()
bot.remove_command('help')
rankname = 'Member'
smp = MinecraftServer("mc.clutchgaming.xyz", 25583)
modded = MinecraftServer("mod.clutchgaming.xyz", 25569)
hypixel = MinecraftServer("mc.hypixel.net", 25565)

@bot.event
async def on_ready():
    print('Successfully booted Clutchbot')
    await bot.change_presence(activity=discord.Game(name='1+1=3!'))
    #await dq_ping()

# Helper function to append suggestion to suggestion file
async def suggestadd(sug):
    with open('suggestions.txt', 'a') as f:
        f.write(sug + '\n')
        f.close()
    return

# Suggestion command to handle suggestions for vibes from players
@bot.command()
async def vibesug(ctx, arg):
    await suggestadd(arg)
    await ctx.send('Suggestion has been noted!')

@bot.command()
async def role(ctx, arg):
    author = ctx.message.author
    if arg in ("mc", "MC", "minecraft", "Minecraft"):
        await author.add_roles(discord.utils.get(author.guild.roles, name="Minecraft"))
        await ctx.send("Minecraft role has been applied!")
        return
    if arg in ("Rust", "rust"):
        await author.add_roles(discord.utils.get(author.guild.roles, name="Rust"))
        await ctx.send("Rust role has been applied!")
    if arg in ("bot", "Bots", "Bot", "bots"):
        await author.add_roles(discord.utils.get(author.guild.roles, name="Bots"))
        await ctx.send("Bot role has been applied!")
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
    role = discord.utils.get(member.guild.roles, name=rankname)
    await member.add_roles(role)
    channel = client.get_channel(666143692159188993)
    await channel.send(str(member) + ' has been autoroled!')

def vibeload():
    with open('vibe.txt') as f:
        lines = [line.rstrip() for line in f]
    return lines

# Help command for commands relating to Vibe Bot
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='Help List',
        description='All commands relevant to Vibe Bot!',
        colour=discord.Colour.dark_magenta()
    )
    embed.set_author(name='Vibe Bot')
    embed.add_field(name='<vibe', value='Checks your vibe!', inline=False)
    embed.add_field(name='<ping', value='Ping to test status of Vibe Bot!', inline=False)
    embed.add_field(name='<fetchbutter', value='Fetches you some butter!', inline=False)
    embed.add_field(name='<role <role>', value='Get a role to get notifications of our updates! Available roles: Minecraft, Rust and Bots', inline=False)
    embed.add_field(name='<vibesug ""', value='Have a vibe suggestion? Run the command *with* quotes! E.g > <vibesug "This bot is gucci gang"',
                    inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def links(ctx):
    embed = discord.Embed(
        title='Links',
        description='All links relevant to ClutchGaming!',
        colour=discord.Colour.purple()
    )
    embed.set_author(name='Vibe Bot')
    embed.add_field(name='Website', value='https://store.clutchgaming.xyz', inline=False)
    embed.add_field(name='Disboard', value='https://disboard.org/server/230087276967886850', inline=False)
    embed.add_field(name='Survival', value='mc.clutchgaming.xyz', inline=False)
    embed.add_field(name='Modded', value='mod.clutchgaming.xyz', inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def iwannadateyou(ctx):
    await ctx.send('Wanna date? Here is my number: (605)-475-6968')

@bot.command()
async def vibe(ctx):
    await ctx.send(random.choice(lines))

@bot.command()
async def fetchbutter(ctx):
    await ctx.send(':butter:')

@bot.command()
async def help(ctx):
    await ctx.send('Just hold your horses, I am still in experimental mode!')

@bot.command()
async def ping(ctx):
    embed = discord.Embed(
        title='ClutchGaming',
        description='Health and Status of our Servers!',
        colour=discord.Colour.green()
    )
    embed.set_author(name='Vibe Bot')
    embed.add_field(name='Survival', value='Ping = {0}'.format(smp.status().latency), inline=False)
    embed.add_field(name='Modded', value='Ping = {0}'.format(modded.status().latency), inline=False)
    embed.add_field(name='Hypixel', value='Ping = {0}'.format(hypixel.status().latency), inline=False)

"""
@bot.command()
async def ping(ctx):
    role = discord.utils.get(ctx.guild.roles, name='Admin')
    if role in ctx.author.roles:
        await ctx.send('Pong!')
    else:
        await ctx.send('You need the ' + role.name + 'role!')"""

lines = vibeload()
print(lines)
bot.run('MzM1NjM3NjQ5MDMxMTY4MDAw.Xl3yMw.R2OTGdH49JDgMSTaKmmTs6vGW2w')