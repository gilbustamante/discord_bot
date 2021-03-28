"""GW2 Bot for Discord"""
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")


# Event handling with decorator:
client = discord.Client()

@client.event
async def on_ready():
    """Runs when bot connects to Discord"""
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f"{client.user} is connected to:\n"
        f"{guild.name} (id: {guild.id})"
    )
    members = "\n - ".join([member.name for member in guild.members])
    print(f"Guild Members:\n - {members}")

# Event handling by subclassing 'Client'
#class CustomClient(discord.Client):
#    async def on_ready(self):
#        print(f"{self.user} has connected to Discord")
#client = CustomClient()


client.run(TOKEN)
