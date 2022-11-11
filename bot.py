# bot.py
import os
import random
from dotenv import load_dotenv

# 1
from discord.ext import commands
import discord
from models import Bracket, Gamer

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()

# 2
bot = commands.Bot(command_prefix='!',intents=intents)

default_players = ['curry', 'eric', 'ian', 'stephen']
current_bracket = Bracket(default_players)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='bracket', help='New bracket, if no names are provided will use Curry Eric Ian Stephen, otherwise provide four names')
async def bracket(ctx, player1=None, player2=None, player3=None, player4=None):
    if player1 is None:
        players = default_players
    else:
        players = [player1, player2, player3, player4]

    bracket = Bracket(players)
    current_bracket = bracket
    await ctx.send(bracket)

@bot.command(name='runitback', help='reshuffle the last bracket')
async def run_it_back(ctx):
    current_bracket.shuffle()
    await ctx.send(current_bracket)


# def get_gaming_channel():
#     for c in bot.get_all_channels():
#         if c.name == 'Gaming':
#             return c.id

# def get_gamers():
#     channel = bot.get_channel(get_gaming_channel())
#     print(f'channel were looking for gamers in: {channel}')
#     members = channel.members


bot.run(TOKEN)
