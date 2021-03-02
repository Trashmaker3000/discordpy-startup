  
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_voice_state_update(member, before, after):
    if not before.channel and after.channel:
        set_mention_name = after.channel.name
        role = discord.utils.get(member.guild.roles, name=set_mention_name)
        await member.add_roles(role)
    elif before.channel and not after.channel:
        remove_mention_name = before.channel.name
        role = discord.utils.get(member.guild.roles, name=remove_mention_name)
        await member.remove_roles(role)

bot.run(token)
