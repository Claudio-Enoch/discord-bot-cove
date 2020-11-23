import discord

from discord.ext import commands

from bot import ADMIN_ID
from bot.utils import dog_ai


class DogCog(commands.Cog):
    def __init__(self, _bot):
        self.bot = _bot

    @commands.Cog.listener()
    async def on_message(self, message):

        # await self.bot.process_commands(message)
        if message.author.bot:
            return

        if (self.bot.user in message.mentions) or not message.guild:  # dog mentioned in general chat or DM
            # Respond with dog AI
            response = dog_ai.get_response(message=message.content)
            await message.channel.send(response)

            # Forward dog DMs to Admin
            owner = await self.bot.fetch_user(ADMIN_ID)
            if isinstance(message.channel, discord.DMChannel):
                if not message.guild:
                    await owner.send(f"{message.author.display_name}: {message.content}\n\tRESPONSE: {response}")
