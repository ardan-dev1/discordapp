import discord
from discord.ext import commands
import datetime
import os
import json
import asyncio
from itertools import cycle

#client config

client = commands.Bot(command_prefix = '>>')
client.remove_command('help')

#commands

@client.event
async def on_message(message):
    if message.content.startswith('>>유저정보'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x6184ff)

        embed.set_author(name=message.author.name + '#' + message.author.discriminator + "님의 프로필")
        embed.add_field(name='**닉네임 & 태그**', value=message.author.name + '#' + message.author.discriminator, inline=True)
        embed.add_field(name='**별명**', value=message.author.display_name, inline=True)
        embed.add_field(name='**계정 생성 일자**', value=str(date.year) + '년 ' + str(date.month) + '월 ' + str(date.day) + '일 ', inline=True)
        embed.add_field(name='**유저 ID**', value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text='Requested by • ' + message.author.name + '#' + message.author.discriminator)

        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('>>리스트'):
        list = []
        for server in client.servers:
            list.append(server.name)
        await client.send_message(message.channel, "\n".join(list))

    if message.content.startswith('>>아바타'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x6184ff)

        embed.set_author(name=message.author.name + '#' + message.author.discriminator + "님의 프로필 사진입니다")
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text='Requested by • ' + message.author.name + '#' + message.author.discriminator, icon_url=message.author.avatar_url)

        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('>>개발자'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x6184ff)

        embed.set_author(name='크레딧')
        embed.add_field(name='개발자', value='``ArdanKR_#9290``', inline=True)
        embed.add_field(name='코드', value='``PYTHON``', inline=False)
        embed.add_field(name='호스팅', value='``Heroku 24 hour``', inline=False)
        embed.add_field(name='그 외', value='`Copyright ⓒ 2019 ArdanKR_#9290 All right reserved`', inline=False)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('>>도움말'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x6184ff)

        embed.set_author(name='XSplace 봇 명령어 목록')
        embed.add_field(name='**일반 명령어**', value='``>>도움말`` , ``>>아바타`` , ``>>리스트`` , ``>>유저정보`` , ``>>봇정보``', inline=True)
        embed.add_field(name='**봇 정보**', value='``>>개발자``', inline=False)
        embed.add_field(name='**Other**', value='`Copyright ⓒ 2019 ArdanKR_ All right reserved`', inline=False)
        embed.set_footer(text='Thanks to use XSplace. If you have an error or problem, please contact ArdanKR_#9290')
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('>>봇정보'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x6184ff)

        embed.set_author(name='봇 정보')
        embed.add_field(name='버전', value='``0.1 알파``', inline=True)
        embed.add_field(name='󠀀󠀀 󠀀󠀀', value='󠀀󠀀 󠀀󠀀')
        embed.add_field(name='XSplace#7270 봇 프로필', value='󠀀󠀀 󠀀󠀀')
        embed.add_field(name='**닉네임 & 태그**', value='XSplace#7270', inline=True)
        embed.add_field(name='**봇 ID**', value='604188013139984384', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/606346201784123396/606792801635663881/1564741015418.png')
        embed.set_footer(text='XSplace By ArdanKR_#9290', icon_url='https://cdn.discordapp.com/attachments/603214980707516416/606795951037743123/1564741015418.png')

        await client.send_message(message.channel, embed=embed)

#client setting
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
