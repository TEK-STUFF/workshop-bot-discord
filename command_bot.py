#coding=utf8

import discord
from dotenv import load_dotenv
from os import getenv
import commands
from commands import *

load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message) :
    if client.user.name in message.content :
        await message.reply("coucou c'est moi")
        await message.add_reaction("💯")
    if message.content and message.content[0] == '>' :
        cmd = str(message.content.split()[0])
        cmd = cmd[1:]
        try :
            fonction = getattr(commands, cmd)
            await fonction(message,client)
        except (AttributeError) :
            await message.add_reaction("⁉️")

@client.event
async def on_ready() -> None :
    print(f"Je suis connecté à discord avec le compte '{client.user}' !")
    serveur = client.guilds[0]
    channel = serveur.get_channel(948344509006229504)
    if channel is not None :
        await channel.send("Bonjour discord !")
    else :
        print("Oups, je n'ai pas pu récupérer le channel")

client.run(TOKEN)