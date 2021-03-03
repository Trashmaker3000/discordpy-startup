from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@client.command()
async def addch(ctx, channel_name):
   thread_category = bot.get_channel(816716125072261120)  # ←botはcommands.Botが入っている変数の名前に置き換えてください。
   await ctx.guild.create_text_channel(channel_name, category=thread_category)
   await ctx.send(f"スレッド[ {channel_name} ]を作成しました！")


bot.run(token)
