import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
GUILD_ID = os.getenv('GUILD_ID')

bot = commands.Bot(command_prefix=".",
                   description="Robot dog",
                   case_insensitive=True,
                   owner_ids=(105864389252382720, 319294754401812481, 366778821921472524),
                   )

from cogs.basic import BasicCog
from cogs.dog import DogCog

bot.add_cog(BasicCog(bot))
bot.add_cog(DogCog(bot))
bot.run(TOKEN)
