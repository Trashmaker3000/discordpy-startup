import discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_ready():
  message.channel.send("起動しました")
  
 client.run(token)
