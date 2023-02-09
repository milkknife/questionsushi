#!/usr/bin/env python3
''' read QS_CHANNEL && export QS_CHANNEL
    read -s QS_TOKEN && export QS_TOKEN
    pypy3 questionsushi.py
'''
from os import environ
from sys import stdout
from random import choices
from logging import StreamHandler
from discord import Intents
from discord.ext import commands, tasks
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

@bot.command()
async def ping(ctx):
    await ctx.send(f'response: {round(bot.latency, 1)}ms')

@bot.event
async def on_ready():
    AskQuestion.start()

@tasks.loop(seconds=30)
async def AskQuestion():
    channel = bot.get_channel(environ['QS_CHANNEL'])
    await channel.send(choices(qdb)[0])

# todo: add choosable answers
bot.run(environ['QS_TOKEN'], log_handler=StreamHandler(stdout))
