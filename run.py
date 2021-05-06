from discord.ext import commands
from yahoo_fin import stock_info as si
import discord
import asyncio

bot = commands.Bot(command_prefix='!')
stock = "BTC-USD" # <--- change this depending on the Yahoo Finance stock symbol, BTC-USD, DOGE-USD, ETH-USD, etc

async def background_task():
        await bot.wait_until_ready()
        while True:
            change = si.get_quote_data(stock)
            name=str(round(si.get_live_price(stock),2))+ " | "+str(round(change["regularMarketChangePercent"],2))+" %"
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="$" + name))
            await asyncio.sleep(2)

@bot.event
async def on_ready():
        print("Now watching " + stock + " from Yahoo Finance")

bot.loop.create_task(background_task())

bot.run('BOTTOKEN')
