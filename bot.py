import discord
from discord.ext import commands
import datetime
import os
import json
import asyncio
from itertools import cycle

#client config

status = ['Prefix = ">>"', 'ArdanKR_#9290', '>>help']

client = commands.Bot(command_prefix = '>>')
client.remove_command('help')

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)

    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status, type=3))
        await asyncio.sleep(5)

#commands

@client.event
async def on_message(message):
    if message.content.startswith('>>userinfo'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x6184ff)

        embed.set_author(name=message.author.name + '#' + message.author.discriminator + "'s Profile")
        embed.add_field(name='**Nickname & Tag**', value=message.author.name + '#' + message.author.discriminator, inline=True)
        embed.add_field(name='**In-Server Name**', value=message.author.display_name, inline=True)
        embed.add_field(name='**Account creation date**', value=str(date.year) + '년 ' + str(date.month) + '월 ' + str(date.day) + '일 ', inline=True)
        embed.add_field(name='**User ID**', value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text='Requested by • ' + message.author.name + '#' + message.author.discriminator)

        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('>>list'):
        list = []
        for server in client.servers:
            list.append(server.name)
        await client.send_message(message.channel, "\n".join(list))

    if message.content.startswith('>>avatar'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x6184ff)

        embed.set_author(name=message.author.name + '#' + message.author.discriminator + "'s Avatar")
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text='Requested by • ' + message.author.name + '#' + message.author.discriminator, icon_url=message.author.avatar_url)

        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('>>developer'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x6184ff)

        embed.set_author(name='Credits')
        embed.add_field(name='Master Developer', value='``ArdanKR_#9290``', inline=True)
        embed.add_field(name='Code', value='``PYTHON``', inline=False)
        embed.add_field(name='Hosting', value='``Heroku 24 hour``', inline=False)
        embed.add_field(name='Other', value='`Copyright ⓒ 2019 ArdanKR_#9290 All right reserved`', inline=False)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('>>help'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x6184ff)

        embed.set_author(name='XSplace Bot Command List')
        embed.add_field(name='**General Command**', value='``>>help`` , ``>>avatar`` , ``>>list`` , ``>>userinfo`` , ``>>about``', inline=True)
        embed.add_field(name='**Bot Information**', value='``>>delvoper``', inline=False)
        embed.add_field(name='**Other**', value='`Copyright ⓒ 2019 ArdanKR_ All right reserved`', inline=False)
        embed.set_footer(text='Thanks to use XSplace. If you have an error or problem, please contact ArdanKR_#9290')
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('>>about'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x6184ff)

        embed.set_author(name='About Bot')
        embed.add_field(name='Version', value='``0.1 alpha``', inline=True)
        embed.add_field(name='󠀀󠀀 󠀀󠀀', value='󠀀󠀀 󠀀󠀀')
        embed.add_field(name='XSplace#7270 BOT Profile', value='󠀀󠀀 󠀀󠀀')
        embed.add_field(name='**Nickname & Tag**', value='XSplace', inline=True)
        embed.add_field(name='**Bot ID**', value='604188013139984384', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/606346201784123396/606792801635663881/1564741015418.png')
        embed.set_footer(text='XSplace By ArdanKR_#9290', icon_url='https://cdn.discordapp.com/attachments/603214980707516416/606795951037743123/1564741015418.png')

        await client.send_message(message.channel, embed=embed)

#client setting
client.loop.create_task(change_status())
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
