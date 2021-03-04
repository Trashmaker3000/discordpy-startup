from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='！')
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_ready():

　ch_name = "一般"
 
  for channel in client.get_all_channels():
        if channel.name == ch_name:
            await channel.send("起動しました")
   

bot.run(token)
