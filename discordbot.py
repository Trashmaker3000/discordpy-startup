from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def　discord.on_voice_state_update(member,before,after):
 if len(after.channel.members) == 1: 
  await create_voice_channel("vc", overwrites=None, category= category, reason=None,)
 elif len(before.channel.members) == 0:
  await delete(,channel, reason=None):
  
   channel = after.channel
    
bot.run(token)
