# bot.py
import discord
from discord.ext import commands
from discord import app_commands
from function_program import find_torrent, find_direct
from dotenv import load_dotenv, dotenv_values

# Load environment variables from .env if present (local dev)
load_dotenv()
config = dotenv_values(".env")
TOKEN = config.get("DISCORD_TOKEN")

if not TOKEN:
    raise ValueError("DISCORD_TOKEN not found in environment variables")

# Bot intents
intents = discord.Intents.default()  # For slash commands, message content intent not required
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    # Sync slash commands
    try:
        synced = await bot.tree.sync()
        print(f"🔗 Synced {len(synced)} slash commands")
    except Exception as e:
        print(f"❌ Sync error: {e}")

# Slash command: /findtorrent
@bot.tree.command(name="findtorrent", description="Search for torrents")
@app_commands.describe(input_text="Enter your search query")
async def findtorrent_cmd(interaction: discord.Interaction, input_text: str):
    result = find_torrent(input_text)
    await interaction.response.send_message(result)

# Slash command: /finddirect
@bot.tree.command(name="finddirect", description="Search for direct links")
@app_commands.describe(input_text="Enter your search query")
async def finddirect_cmd(interaction: discord.Interaction, input_text: str):
    result = find_direct(input_text)
    await interaction.response.send_message(result)

# Run bot
bot.run(TOKEN)
