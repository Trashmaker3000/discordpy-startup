import discord


with open("token.txt") as F:
  token = F.read()
 
client = discord.client()

@client.event
async def on_ready():
  message.channel.send("起動しました")
  
 client.run(token)
