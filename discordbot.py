from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

CHANNEL_ID = 816632415165349921

@client.event
async def on_message(message):
    if message.author.bot: # メッセージ送信者がBotだった場合は無視する
        return

    if message.channel.id != CHANNEL_ID: # チャンネルが違う場合は無視する
        return

    if message.content == '!bot':#「XX」と発言したら
        await message.channel.send('```BOT discordバージョン起動中です。```')#「XX」が返る処理

bot.run(token)
