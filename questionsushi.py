#!/usr/bin/env python3
''' read -s DISCORD_BOT_TOKEN && export DISCORD_BOT_TOKEN
    pypy3 questionsushi.py
'''
from os import environ
from sys import stdout
from random import choices
from logging import StreamHandler
from discord import Intents
from discord.ext import commands
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents)

with open('db.yml') as f:
    qdb = load(f, Loader=Loader)

@bot.command(name='question') # todo: add more parameters, send message like chron
async def getq(ctx): # todo: wait one minute, then announce the answer
    await ctx.send(choices(qdb)[0]) # todo: state language

bot.run(environ['DISCORD_BOT_TOKEN'], log_handler=StreamHandler(stdout))
