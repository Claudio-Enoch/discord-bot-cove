import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
GUILD_ID = os.getenv('GUILD_ID')

# TODO: make dynamic, based on roles
OWNER_IDS = (
    105864389252382720, 319294754401812481, 366778821921472524, 283864159999754240, 283864159999754241,
    517165087518228490)
ADMIN_ID = OWNER_IDS[0]

bot = commands.Bot(command_prefix=".",
                   description="Robot dog",
                   case_insensitive=True,
                   owner_ids=OWNER_IDS,
                   )
