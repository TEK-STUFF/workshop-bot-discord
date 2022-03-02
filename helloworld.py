#!/usr/bin/env python3
#coding=utf8

import discord
from dotenv import load_dotenv
from os import getenv

load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')

client = discord.Client()

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