import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

TOKEN = "NTY4NzE0ODAzODI1MjEzNDQw.XL8biw.azg9JwVj2Xl6pqAoXuxrjXiaDh4"


async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print("------")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    user = message.author
    msg = message.content
    print(f"{user} said {msg}")

    await client.process_commands(message)

@client.event
async def on_message_delete(message):
    await message.channel.send("여기에 메시지가 지워졌습니다.")

@client.command() #!안녕을 치면 안녕하세요가 출력
async def 안녕(ctx):
    await ctx.send("안녕하세요!")

@client.command(aliases=["따라하기"]) #내가 보낸 말을 그대로 보냄
async def say(ctx, *, words):
    await ctx.send(words)

@client.command()
async def 위뜨유(ctx):
    embed = discord.Embed(title="위뜨유의 유튜브", desciption="Description", colour=discord.Color.red(), url="https://www.youtube.com/channel/UC4OEaJ7-78b9XXZdPjns8_A?view_as=subscriber")

    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/IR3SH1GToLrOWRQPDabU0RZlv-n1iHQ3kRmdwGbTyJUKAaTxoB6V7j1fOX8Z3suolXi8W7P9S9SI=w220-h220-n-o-rw")

    embed.add_field(name="마우스", value="Logitech G304")
    embed.add_field(name="감도", value="dpi 1000/ingame 8")

    await ctx.send(embed=embed)

@client.command()
async def 엘팍(ctx):
    embed = discord.Embed(title="엘팍이의 유튜브", desciption="Description", colour=discord.Color.red(), url="https://www.youtube.com/channel/UCQMwLUH_C0Qw82cmRQGX7Fw")

    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://yt3.ggpht.com/a-/AAuE7mDpjK2FInWTXbp369re5Mbj0T9sfX4qZBGbXA=s288-mo-c-c0xffffffff-rj-k-no")

    embed.add_field(name="마우스", value="Logitech G403")
    embed.add_field(name="감도", value="dpi 1600/ingame 2.25")

    await ctx.send(embed=embed)


client.run(TOKEN)
