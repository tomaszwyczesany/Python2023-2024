#!/usr/bin/python3.6
import random

import discord
from discord.ext import commands
# -- Functions ------
async def zalgo_ify(text):
    ''' Takes some normal text and zalgo-ifies it '''

    # "Combining Diacritical Marks" Unicode block.
    combining_chars = [chr(n) for n in range(768, 878)]

    zalgo_text = ''

    for char in text:
        combining_char = random.choice(combining_chars)
        zalgo_text += f'{char}{combining_char}'

    return zalgo_text
# -- Bot setup ------
bot = commands.Bot(command_prefix='!')
# -- Commands -------
@bot.command()
async def zalgo(ctx):
    message = str(ctx.message.content)

    zalgo_text = await zalgo_ify(message)
    await ctx.send(zalgo_text)
# -- Run bot --------
bot.run('ODMzNzYxNzA2NjI2MTIxNzI4.YH3DGQ.VfwFpy-x9gUAOcI4p_zUchwgRPU')
# Secret token, show no one!