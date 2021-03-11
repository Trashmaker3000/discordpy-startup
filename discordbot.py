from discord.ext import commands
import os
import traceback
import datetime

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
channel_id = 817830113743863828

@client.event
async def on_ready():
    channel = client.get_channel(channel_id)
    dt_now = str(datetime.datetime.now())
    embed = discord.Embed(title="on_ready",description=dt_now)
    await channel.send(embed=embed)
 
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('おはよう')
    
bot.run(token)
