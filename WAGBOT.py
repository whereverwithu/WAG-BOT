import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='We Are Gamers!', type=1))


@client.event
async def on_message(message):
    if message.content.startswith("!규칙"):
        await client.send_message(message.channel, "#규칙 에서 규칙을 확인하실 수 있습니다! 규칙이 바뀌면 #공지 에서 공지가 되니 확인해주세요!")

        
access_token = os.environ["BOT_TOKEN"]        
client.run('access_token')
