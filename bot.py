import discord
from discord.ext import commands
import time
import asyncio
import os

messages = joined = 0
day = 86400

bot = commands.Bot(command_prefix='$')
file = open('token.txt', 'r').readlines()
token = file[0]
'''
Previous console log for bot, it's moved to Activities Cog now.

async def update_stats():
    await bot.wait_until_ready()
    global messages

    while not bot.is_closed():
        try:
            with open('server_stats.txt', 'a') as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}\n")

            messages = 0
            await asyncio.sleep(day)

        except Exception as e:
            print(e)
            await asyncio.sleep(day)
'''

@bot.event
async def on_ready():
    '''Console log when bot is ready to work'''
    print('Logged in as {0.user}'.format(bot))

@bot.command()
@commands.is_owner()
async def reload(ctx, cog):
    '''Reload function to edit your Cogs. Just put your server ID in here or remove if statement to make it work'''
    if ctx.message.guild.id == 635087690240360448:
        try:
            bot.unload_extension(f'cogs.{cog}')
            bot.load_extension(f'cogs.{cog}')
            await ctx.send(f"{cog} module reloaded.")
        except Exception as e:
            raise e
    else:
        pass


async def chng_pr():
    '''Change bot presence'''
    await bot.wait_until_ready()

    status = 'Hello everyone!'
    while not bot.is_closed():
        await bot.change_presence(activity=discord.Game(status))
        await asyncio.sleep(300)


'''Initiate Cogs launch'''
for cog in os.listdir('.\\cogs'):
    if cog.endswith(".py"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            raise e

bot.loop.create_task(chng_pr())
bot.run(token)
