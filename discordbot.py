from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def　on_voice_state_update(member,before,):
if len（before.Channele.members） ＝＝ ０：
 await ctx.send('成功')
 
@bot.command()
async def ping(ctx):
    await ctx.send('ロング')

bot.run(token)
