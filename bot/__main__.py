from bot import bot, TOKEN
from bot.cogs.basic import BasicCog
from bot.cogs.dog import DogCog

# Add cogs (blueprints) to bot and run
bot.add_cog(BasicCog(bot))
bot.add_cog(DogCog(bot))
bot.run(TOKEN)
