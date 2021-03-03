from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def　on_voice_state_update(member,before,after):
 if len(after.Voicechannel.members) == 0: 
  await create_voice_channel("vc", overwrites=None, category= category, reason=None,)
 elif len(before.Voicechannel.members) == 0:
  await delete(before.Voicechannel, reason=None):
  
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
bot.run(token)
