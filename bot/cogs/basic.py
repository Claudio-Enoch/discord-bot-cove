import discord
from discord.ext import commands

from bot import ADMIN_ID


class BasicCog(commands.Cog):
    def __init__(self, _bot):
        self.bot = _bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("I am running as:", self.bot.user.name, "\nWith the ID:", self.bot.user.id)
        await self.bot.change_presence(activity=discord.Game(name="with myself"))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        admin = self.bot.get_user(ADMIN_ID)
        if admin:
            await admin.dm_channel.send(f"REPORTING: {member.display_name} has JOINED the Cove")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        admin = self.bot.get_user(ADMIN_ID)
        if admin:
            await admin.dm_channel.send(f"REPORTING: {member.display_name} has been REMOVED from Cove")

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
        await channel.connect()
