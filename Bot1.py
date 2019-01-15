import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
client = commands.Bot(command_prefix="!")


quotes = {0: "Heahaha sorry I don't know why I'm laughing...AAAAHHH! Hehahahhahahahaa. AAAAAHHHH! HEHAEHAHAHAHAHAHAHHAHAHAHAHAHAHHHHH. I don't know why I cant help it, I'm sorry! Sorry! It's just the teNSION HAHAHAHAHAHAHAHAHHAHAHH! AHHHHHHH!! I'M SORRY I'M SORRY.AAAAAAAAAHHHH!!!!!!! Hahahahahahha, ahh. Ohh Gawd, I'm sorry it's just .....ahhhhh....",
           1: "If he gets certified as a cheat, I will seek him out and legally sue him",
           4: "HAHAHA! No, no, It doesn't bloody do anything..... YES, YES IT DOES! YES IT DOES!!!! \nHOLD ON. HOLD ON. CHECK, CHECK, ROOK B1 !!!!!!!!!!!!!!!!!!!!! ROOK B1 !!!!!! Oh my god that's the best little combination I've ever played",
           9: "HAHAHAHHAHAHAHAHHAHAHHA. Sorry, just a bit of stress relief",
           2: "Now we're cooking with gas!",
           3: "Oh this shit again...\n oh, okay great. Oh fuck it,\n I'm resigning. Fuck off. Seriously,\n I don't want to play assholes",
           5: "He's either a psychopath or a GM",
           6: "DIIIEEEEE!!!!!!",
           7: "mmmm apple juice...."
}


@client.event
async def on_ready():
    print("operational")


@client.event
async def on_message(message):
    if message.content == 'hey KC':
        option = random.randint(0, 7)
        remark = quotes[option]
        await client.send_message(message.channel, remark)

client.run("NTM0NzkwMDYxMzkzMTgyNzIy.Dx-uOQ.65tKa2UKvQq91bQwLBAbjJeETC0")
