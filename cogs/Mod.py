import discord
from discord.ext import commands

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason="No reason"):
        '''Kick someone from server'''
        if member == None:
            await ctx.send("Who you want to kick?")
        else:
            await member.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason="No reason"):
        '''Ban someone from server'''
        if member == None:
            await ctx.send("Who you want to ban?")
        else:
            await member.ban(reason=reason)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def delete(self, ctx, num):
        '''Delete given number of messages above'''
        await ctx.channel.purge(limit=int(num) + 1)


def setup(bot):
    bot.add_cog(Mod(bot))
