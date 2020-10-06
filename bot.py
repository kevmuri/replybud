# bot.py
import os

import discord
from dotenv import load_dotenv

import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	coolquips = ['Umm hello? based department?', '@here everyone get in here and see how much that message sucked', 'Excellent point, friend :)', 'Repent, Zoomer.', 'hahaha epic reddit bacon message ahahaha heres your gold good sir extra choccy milky for you', 'Haha soy!!!', '**{} has been banned from this channel for that abhorrent post.**'.format(message.author), 'cringe!'
	]
	max = 10
	replychance = random.randint(1, max)
	print(f'New message posted. Random number is {replychance}. {max} is needed.')
	if replychance == max:
		response = random.choice(coolquips)
		print(f'New quip: {response}')
		await message.channel.send(response)

client.run(TOKEN)
