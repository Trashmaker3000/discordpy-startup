from discord.ext import commands
import os
import traceback

@client.event
async def on_ready():
    channel = client.get＿channel(819855834896531466)
    await channel.send("起動しました")

bot.run(token)
