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

        if message.content.startswith('!테스터'):
             await message.channel.send('{0.author.mention}님 테스터에 관한 내용입니다.'.format(message))
             await message.channel.send('1. 클랜에 들어오신지 **__3주__**가 되셔야합니다.'.format(message))
             await message.channel.send('2. 채팅을 치시면 레벨이 존재하는데 **__최소 3레벨__**을 달성하셔야합니다.'.format(message))
             await message.channel.send('3. **__활발하게 활동__**을 하셔야 합격할 확률이 높습니다.'.format(message))

        if message.content.startswith('!정보'):
            date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
            embed = discord.Embed(color=0x00ff00)
            embed.add_field(name="이름", value=message.author.name, inline=True)
            embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
            embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
            embed.add_field(name="아이디   ", value=message.author.id, inline=True)
            embed.set_thumbnail(url=message.author.avatar_url)
            await message.channel.send(message.channel, embed=embed)

        if message.content.startswith('!투표'):
            vote = message.content[4:].split("/")
            await message.channel.send(vote[0].format(message))
            for i in range(1, len(vote)):
                await message.channel.send(vote[i].format(message))
                await client.add_reaction(choose, '✔')



client = MyClient()
client.run('NTY3NzIwNjg3MjQ3MTYzMzky.XLXpKQ.QOGeYWw3xyeqAO3s8TwhjBGcw0U')
