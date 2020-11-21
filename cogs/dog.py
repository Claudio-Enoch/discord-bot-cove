import asyncio
import random
from discord.ext import commands


class DogCog(commands.Cog):
    def __init__(self, _bot):
        self.bot = _bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # await self.bot.process_commands(message)
        if message.author == self.bot.user:
            return
        # Respond with random dog activity
        dog_texts = ["Dog food! My favorite thing!",
                     "A car ride! My favorite thing!",
                     "A walk in the park! My favorite thing!",
                     "Got rubbed and petted! My favorite thing!",
                     "Milk bones! My favorite thing!",
                     "Played in the yard! My favorite thing!",
                     "Wagged my tail! My favorite thing!",
                     "Dinner! My favorite thing!",
                     "Got to play ball! My favorite thing!",
                     "Wow! Watched TV with the people! My favorite thing!",
                     "Sleeping on the bed! My favorite thing!",
                     ]
        response = random.choice(dog_texts)
        # await message.channel.send(response)

        # Forward messages from dog to Admin
        admin = self.bot.get_user(105864389252382720)
        await admin.dm_channel.send(f"{message.author.display_name}: {message.content}")

        if len(message.content) == 4:  # ToDo: avoid action in dm channel
            await asyncio.sleep(10)
            await message.delete()
