from discord.ext import commands
import discord
import asyncio
import requests

bot = commands.Bot(command_prefix='!')
stock = "bitcoin" #found via coincap.io

async def background_task():
        await bot.wait_until_ready()
        while True:
                try:
                        response = requests.get('https://api.coincap.io/v2/assets/' + stock)
                        data = response.json()
                        name = str("{:,}".format(round(float(data['data']['priceUsd']),2)))+ " | "+ str(round(float(data['data']['changePercent24Hr']),2))+" %"
                        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="$" + name))
                        await asyncio.sleep(2)
                except:
                        pass

@bot.event
async def on_ready():
        print("now watching " + stock + " from coincap.io")

bot.loop.create_task(background_task())

bot.run('BOTTOKEN')
