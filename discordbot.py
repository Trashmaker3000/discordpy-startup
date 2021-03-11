from discord.ext import commands
import os
import traceback
import datetime

token = os.environ['DISCORD_BOT_TOKEN']
channel_id = os.environ[CHANNEL_ID]

@client.event
async def on_ready():
    channel = client.get_channel(channel_id)
    dt_now = str(datetime.datetime.now())
    embed = discord.Embed(title="on_ready",description=dt_now)
    await channel.send(embed=embed)
    
bot.run(token)
