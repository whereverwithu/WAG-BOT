import discord
import datetime

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!안녕'):
            await message.channel.send('안녕하세요. {0.author.mention}'.format(message))

        if message.content.startswith('!규칙'):
            await message.channel.send('{0.author.mention}님 #규칙 을 이용해주세요. 지키지 않을시 경고를 받습니다.'.format(message))

        if message.content.startswith('!명령어'):
            await message.channel.send('{0.author.mention}님 여기 명령어 목록 입니다.'.format(message))
            await message.channel.send('!규칙'.format(message))
            await message.channel.send('!안녕'.format(message))
            await message.channel.send('!정보'.format(message))

        if message.content.startswith('!정보'):
            date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
            embed = discord.Embed(color=0x00ff00)
            embed.add_field(name="이름", value=message.author.name, inline=True)
            embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
            embed.add_field(name="아이디   ", value=message.author.id, inline=True)
            embed.set_thumbnail(url=message.author.avatar_url)
            await message.channel.send(message.channel, embed=embed)



client = MyClient()
client.run('NTY3NzIwNjg3MjQ3MTYzMzky.XLXpKQ.QOGeYWw3xyeqAO3s8TwhjBGcw0U')
