import discord
from discord.ext import commands


class BasicCog(commands.Cog):
    def __init__(self, _bot):
        self.bot = _bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("I am running as:", self.bot.user.name)
        print("With the ID:", self.bot.user.id)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        admin = self.bot.get_user(105864389252382720)
        await admin.dm_channel.send(f"{member.display_name} has JOINED the Cove")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        admin = self.bot.get_user(105864389252382720)
        await admin.dm_channel.send(f"{member.display_name} has been REMOVED from Cove")

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if n := after.nick:
            if (n.lower().count("claud") > 0) or (n.lower().count("ciaud") > 0):
                if last := before.nick:
                    await after.edit(nick=last)
                else:
                    await after.edit(nick="woof!")

    @commands.command()
    async def add(self, ctx, left: int, right: int):
        """Adds two numbers together."""
        await ctx.send(left + right)

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
        await channel.connect()
