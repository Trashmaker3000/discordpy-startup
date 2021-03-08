from discord.ext import commands
import os
import traceback
import datetime
import random
import time
import sys
import asyncio
import re

client = discord.Client()


#起動メッセージ送信
@client.event
async def on_ready():
    timestamp = str(datetime.datetime.now())
    embed = discord.Embed(title='**on_ready**', description=timestamp)  
    await Admin_Message(embed)
    
#AdminRoomMessage
async def Admin_Message(embed):
    for channel in client.get_all_channels():
       if channel.id == 817830113743863828:
           await channel.send(embed=embed)


#Command
arasi_task = None


@client.event
async def on_message(message):
    global arasi_task
    if "荒" in message.content:
       await message.add_reaction("🎉")
       await message.channel.edit(topic = True)
       for i in range(50):
           arasi_task = asyncio.current_task()
           random_contens = [
               "どりゃあああああああ",
               "ふんっ",
               "せやぁあああああ！！！！！",
               "どむどむどむどむどむどむどむ",
               "ポイズン最強！！！！:sweat_smile:",
               "ポイゾネスもいるんだが:sweat_smile:",
               "インターネットやめるなよ(涙)",
               "https://tenor.com/view/crayon-shin-chan-stretch-cheek-pinch-cheek-anime-gif-16498684",
               "https://tenor.com/view/goku-krillin-stinky-finger-thicc-dragonball-gif-20157072",
               "https://tenor.com/view/i-hate-it-nobita-%E3%81%AE%E3%81%B3%E5%A4%AA-doraemon-%E3%83%89%E3%83%A9%E3%81%88%E3%82%82%E3%82%93-gif-19935205",
               "https://tenor.com/view/akane-chan-gif-11761498"
                ]   
           arasi_content = random.choice(random_contens)
           await message.channel.send(arasi_content)
           await asyncio.sleep(0.3)
           if 45 == i:
             await message.channel.edit(topic = "False")
    elif "うるさい" in message.content:
        arasi_task.cancel()
        await message.channel.edit(topic = "False")
        await message.add_reaction("😅")
    elif "True" == message.channel.topic:
        for reaction in ["🐉", "🌈", "❤", "😙", "🚗", "😎", "👳‍♂️", "🥟", "🚑", "🐠", "🏉", "🍓", "😁", "💂‍♂️", "✍", "🍤", "🛹", "🐲", "💋", "🎃",]:
            await message.add_reaction(reaction)
     
        
        
client.run()  
