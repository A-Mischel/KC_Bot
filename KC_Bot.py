import discord
from discord import Embed
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os

Client = discord.Client()
client = commands.Bot(command_prefix="!")
client.counter = 1
quotes = {
    0: "Heahaha sorry I don't know why I'm laughing...AAAAHHH! Hehahahhahahahaa. AAAAAHHHH! HEHAEHAHAHAHAHAHAHHAHAHAHAHAHAHHHHH. I don't know why I cant help it, I'm sorry! Sorry! It's just the teNSION HAHAHAHAHAHAHAHAHHAHAHH! AHHHHHHH!! I'M SORRY I'M SORRY.AAAAAAAAAHHHH!!!!!!! Hahahahahahha, ahh. Ohh Gawd, I'm sorry it's just .....ahhhhh....",
    1: "If he gets certified as a cheat, I will seek him out and legally sue him",
    2: "HAHAHA! No, no, It doesn't bloody do anything..... YES, YES IT DOES! YES IT DOES!!!! \nHOLD ON. HOLD ON. CHECK, CHECK, ROOK B1 !!!!!!!!!!!!!!!!!!!!! ROOK B1 !!!!!! Oh my god that's the best little combination I've ever played",
    3: "HAHAHAHHAHAHAHAHHAHAHHA. Sorry, just a bit of stress relief",
    4: "Now we're cooking with gas!",
    5: "Oh this shit again...\n oh, okay great. Oh fuck it,\n I'm resigning. Fuck off. Seriously,\n I don't want to play assholes",
    6: "He's either a psychopath or a GM",
    7: "DIIIEEEEE!!!!!!",
    8: "mmmm apple juice...."
}


@client.event
async def on_ready():
    print("operational")


@client.event
async def on_message(message):
    if message.content.startswith('hiel'):
        await client.send_message(message.channel, ':kccommunism:')
    await client.process_commands(message)



@client.command()  # This is just the embeded page with all the bot info
async def KC():
    embed = discord.Embed(
        title='\t---KC_Bot---',
        description="I'm always watching ya wee shite! \n **Side note:** Feel free to message me if you have any suggestions or want to add content",
        colour=discord.Color.dark_red()
    )

    embed.set_footer(text='All source code can be found here: https://github.com/A-Mischel/KC_Bot')
    embed.set_image(url='https://en.chessbase.com/portals/all/2018/01/banter-blitz/kingscrusher-pic2.jpg')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/535165334450208778/535193619745996810/kccommunism.png')
    embed.set_author(name='skidabit',icon_url='https://yt3.ggpht.com/a-/AN66SAzbnAE9jmsJ1skkqEYTdjWJ6NN3ihKgpcoCGw=s900-mo-c-c0xffffffff-rj-k-no')
    embed.add_field(name='Command:  !Hey_KC',value='-To get a freshly baked, locally grown quote from the legend himself.', inline=False)
    embed.add_field(name='Command:  !KC', value=' -An Overview of your Overlord. ', inline=False)
    embed.add_field(name='etc...', value='More commands coming soon ', inline=True)

    await client.say(embed=embed)


@client.command()
async def HEY_KC():
    option = random.randint(0, 8)  # the random number corresponds with a quote
    if option == client.counter:  # basically im just making sure no quote repeats.
        if option == 0:  # so if the previos quote = the current quote I minus 1 from the random number
            option += 1  # and if that the number is zero then i just add 1
        else:
            option -= 1
    remark = quotes[option]
    client.counter = option
    await client.say(remark)


@client.command()
async def Giri():
        await client.say('draws')


@client.command()
async def Finegold():
    await client.say('RAWR...fries?')


client.run(os.getenv("TOKEN"))
