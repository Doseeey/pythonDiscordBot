import discord
from discord.ext import commands
import asyncio

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''Console logs, errors etc.'''

    @commands.Cog.listener()
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        print(("DELETED -- {}: {}".format(message.author.name,message.content)))

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("Haha nie mozesz wypierdalaj")
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Nie moge Mokebe, mam chłopaka")
            await asyncio.sleep(2)
            await ctx.send("**jak to 40**")

        raise error

def setup(bot):
    bot.add_cog(Events(bot))
