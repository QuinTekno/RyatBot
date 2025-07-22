import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv() # Load environment variables from .env 
token = os.getenv("DISCORD_TOKEN")

intents=discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# load all cogs
@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extentions(f"cogs.{filename[:-3]}")


#start the bot
bot.run(token)
# Replace with your token, or load from .env
