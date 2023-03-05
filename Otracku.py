import os
import discord
import time
from dotenv import load_dotenv
from discord.ui import Select,View
from discord.ext import commands
import asyncio
from AnilistPython import Anilist
anilist=Anilist()
load_dotenv()
TOKEN = os.getenv('MTAzNDQzODkzODk1OTU0NDMyMg.GISW0X.IPnQ1vlkji7ylEivz3K5-YCMOIHgg8ti98nths')
intents = discord.Intents()
intents.emojis = True
intents.messages = True
intents.presences = True
intents.message_content = True
client = commands.Bot(command_prefix=".",intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name='you guys waste your time on Anime and Manga'))
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)

@client.command()
async def info(ctx):
    help=discord.Embed(title='Instruction Manual for Otracku', description='List of commands you can use and what they are for.')
    help.add_field(name="info",value='Gives a list of all commands',inline=False)
    help.add_field(name='setr',value='Sets a reminder for all the episodes of the show given as parameter until it stops airing. Different Seasons are treated as different shows. Do no give spaces between the words of name of the show',inline=False)
    help.add_field(name='anisyn',value="Gives Synopsis of an anime. That's pretty much it",inline=False)
    help.add_field(name='mansyn',value='Gives Synopsis of a manga.',inline=False)
    help.set_thumbnail(url=client.user.avatar)
    await ctx.send(embed=help)

@client.command()
async def setr(ctx,ded=""):
    a=anilist.get_anime(ded)
    # print(a)
    while(a['airing_status']=='RELEASING'):
        ok=a['next_airing_ep']['timeUntilAiring']
        await asyncio.sleep(ok)
        await ctx.send(f'{ctx.author.mention} {ded} has a new Episode')
    await ctx.send(f'{ded} has ended. See you next when the next season airs')

@client.command()
async def anisyn(ctx,ded=""):
    a=anilist.get_anime(ded)
    n=a['name_romaji']
    d=a['desc']
    syn=discord.Embed(title=f'{n}',description=f'{d}')
    syn.set_thumbnail(url=a['cover_image'])
    await ctx.send(embed=syn)

@client.command()
async def mansyn(ctx,ded=""):
    a=anilist.get_manga(ded)
    n=a['name_romaji']
    d=a['desc']
    syn=discord.Embed(title=f'{n}',description=f'{d}')
    syn.set_thumbnail(url=a['cover_image'])
    await ctx.send(embed=syn)

client.run('MTAzNDQzODkzODk1OTU0NDMyMg.GISW0X.IPnQ1vlkji7ylEivz3K5-YCMOIHgg8ti98nths')
