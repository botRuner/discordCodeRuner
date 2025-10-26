import discord
from discord.ext import commands
from function_program import find_torrent, find_direct
from dotenv import load_dotenv
import os

load_dotenv()  # Load token from .env
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    await bot.tree.sync()

# Slash command examples
from discord import app_commands

@bot.tree.command(name="findtorrent", description="Search for torrents")
@app_commands.describe(input_text="Enter your search query")
async def findtorrent_cmd(interaction: discord.Interaction, input_text: str):
    result = find_torrent(input_text)
    await interaction.response.send_message(result)

@bot.tree.command(name="finddirect", description="Search for direct links")
@app_commands.describe(input_text="Enter your search query")
async def finddirect_cmd(interaction: discord.Interaction, input_text: str):
    result = find_direct(input_text)
    await interaction.response.send_message(result)

bot.run(TOKEN)
