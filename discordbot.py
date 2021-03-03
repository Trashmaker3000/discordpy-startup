from discord.ext import commands
import os
import traceback

bot = commas.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    errorsg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.coand()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
