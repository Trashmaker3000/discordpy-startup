from discord.ext import commands
import os
import traceback

bot = commands.Bot
token = os.environ['DISCORD_BOT_TOKEN']

bot.run(token)
