import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os

Client = discord.Client()
client = commands.Bot(command_prefix="!")


quotesA = {
    0: "Heahaha sorry I don't know why I'm laughing...AAAAHHH! Hehahahhahahahaa. AAAAAHHHH! HEHAEHAHAHAHAHAHAHHAHAHAHAHAHAHHHHH. I don't know why I cant help it, I'm sorry! Sorry! It's just the teNSION HAHAHAHAHAHAHAHAHHAHAHH! AHHHHHHH!! I'M SORRY I'M SORRY.AAAAAAAAAHHHH!!!!!!! Hahahahahahha, ahh. Ohh Gawd, I'm sorry it's just .....ahhhhh....",
    1: "If he gets certified as a cheat, I will seek him out and legally sue him",
    2: "HAHAHA! No, no, It doesn't bloody do anything..... YES, YES IT DOES! YES IT DOES!!!! \nHOLD ON. HOLD ON. CHECK, CHECK, ROOK B1 !!!!!!!!!!!!!!!!!!!!! ROOK B1 !!!!!! Oh my god that's the best little combination I've ever played",
    3: "HAHAHAHHAHAHAHAHHAHAHHA. Sorry, just a bit of stress relief",
    4: "Now we're cooking with gas!"
    }

quotesB = {
    5: "Oh this shit again...\n oh, okay great. Oh fuck it,\n I'm resigning. Fuck off. Seriously,\n I don't want to play assholes",
    6: "He's either a psychopath or a GM",
    7: "DIIIEEEEE!!!!!!",
    8: "mmmm apple juice...."
    }


@client.event
async def on_ready():
    print("operational")


client.counter = 1


@client.event
async def on_message(message):
    if message.content.upper() in ('HEY KC', '!HEY KC'):
        if client.counter == 1:
            option1 = random.randint(0, 4)
            remark1 = quotesA[option1]
            await client.send_message(message.channel, remark1)
            client.counter += 1
        elif client.counter == 2:
            option2 = random.randint(5, 8)
            remark2 = quotesB[option2]
            await client.send_message(message.channel, remark2)
            client.counter -= 1



client.run(os.getenv("TOKEN"))
