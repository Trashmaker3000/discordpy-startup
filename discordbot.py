from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def　on_voice_state_update(member,before,):
if len(before.VoiceChannele.members) == 0:
 await guild.create_voice_channel("VC", overwrites=None, category=None, reason=None)
 
@bot.command()
async def ping(ctx):
    await ctx.send('今')
    
bot.run(token)
