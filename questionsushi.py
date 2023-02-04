#!/usr/bin/env python3
''' read -s DISCORD_BOT_TOKEN && export DISCORD_BOT_TOKEN
    pypy3 questionsushi.py
'''
from os import environ
from sys import stdout
from random import choice
from logging import StreamHandler
from discord import Intents
from discord.ext import commands

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

# sample questions, switch this with db file
qdb = ('what is a class decorator?',
       'what does `yield` do?')

@bot.command(name='say', description='says something')
async def ping(ctx, abc): # sample command
    try:
        await ctx.send(abc)
        0/0 # experimenting with exception handling
    except: # todo: handle invalid input
        await ctx.send('nuh uh uh')

@bot.command(name='question') # todo: add more parameters, send message like chron
async def getq(ctx, lang): # todo: wait one minute, then announce the answer
    await ctx.send(f'{lang}: {choice(qdb)}') # todo: state language

bot.run(environ['DISCORD_BOT_TOKEN'], log_handler=StreamHandler(stdout))
