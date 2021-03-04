from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='！')
token = os.environ['DISCORD_BOT_TOKEN']


@client.event
async def on_ready():

　CHANNEL_ID = 816632415165349921 # 任意のチャンネルID(int)

# 任意のチャンネルで挨拶する非同期関数を定義
async def greet():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('おはよう！')

# bot起動時に実行されるイベントハンドラを定義
@client.event
async def on_ready():
    await greet() # 挨拶する非同期関数
   

bot.run(token)
