import discord
from discord.ext import commands
from discord import slash_command
from dotenv import load_dotenv
import os

def slash_command(name=None, description=None):
    def decorator(func):
        bot.tree.add_command(
            discord.app_commands.SlashCommand(
                name=name,
                description=description,
                callback=func
            )
        )
        return func
    return decorator

load_dotenv() # Load environment variables from .env 
token = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))  # Replace with your guild ID

intents=discord.Intents.default()
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix='?', intents=intents)

# load all cogs
@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")

    try:
        synced = await bot.tree.sync(guild=discord.Object(id=GUILD_ID))
        print(f"Synced {len(synced)} commands.")

    except Exception as e:
        print(f"Error syncing commands: {e}")
        await bot.tree.sync(guild=discord.Object(id=GUILD_ID))
        

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extensions(f"cogs.{filename[:-3]}")

@bot.command()
async def on_message(self, message: discord.Message):
    if message.author == bot.user:
        return

    await message.channel.send("Hello!")



#start the bot
bot.run(token)
# Replace with your token, or load from .env
