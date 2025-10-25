# bot.py
import discord
from discord.ext import commands
from discord import app_commands
from function_program import find_torrent, find_direct
from dotenv import load_dotenv, dotenv_values

# Load .env file
load_dotenv()
config = dotenv_values(".env")  # Read token from .env
TOKEN = config.get("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"🔗 Synced {len(synced)} slash commands.")
    except Exception as e:
        print(f"❌ Sync error: {e}")

# /findtorrent command
@bot.tree.command(name="findtorrent", description="Search for torrents")
@app_commands.describe(input_text="Enter search query")
async def findtorrent_cmd(interaction: discord.Interaction, input_text: str):
    result = find_torrent(input_text)
    await interaction.response.send_message(result)

# /finddirect command
@bot.tree.command(name="finddirect", description="Search for direct links")
@app_commands.describe(input_text="Enter search query")
async def finddirect_cmd(interaction: discord.Interaction, input_text: str):
    result = find_direct(input_text)
    await interaction.response.send_message(result)

bot.run(TOKEN)
