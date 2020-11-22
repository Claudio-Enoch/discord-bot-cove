from discord.ext import commands

from bot import ADMIN_ID
from bot.utils import dog_ai


class DogCog(commands.Cog):
    def __init__(self, _bot):
        self.bot = _bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # await self.bot.process_commands(message)
        if message.author == self.bot.user:
            return

        # Respond with random dog activity
        response = dog_ai.get_response(message=message.content)
        await message.channel.send(response)

        # Forward DMs from dog to Admin
        admin = self.bot.get_user(ADMIN_ID)
        dm_from_not_admin = not message.guild and message.author != admin
        if admin and dm_from_not_admin:
            dm = f"{message.author.display_name}: {message.content}"  # {message.embeds[0]}
            admin_dm = admin.dm_channel or await admin.create_dm()
            await admin_dm.send(f"{dm}\n\tRESPONSE: {response}")
