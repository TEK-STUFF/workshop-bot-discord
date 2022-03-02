#coding=utf8

import discord

async def say(message, client) :
    text = str(message.content.split(' ', 1)[1])
    await message.channel.send(text)