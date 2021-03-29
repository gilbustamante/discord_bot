"""ISS Bot for Discord"""
import os
from datetime import datetime
from discord.ext import commands
from dotenv import load_dotenv
import reverse_geocoder as rg
import requests

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    """Runs when bot connects to Discord"""
    print(f"{bot.user.name} has connected to Discord")


@bot.command(name="ISS")
async def find_iss(ctx):
    """Returns the location of the ISS"""
    url = "http://api.open-notify.org/iss-now.json"
    res = requests.get(url).json()
    time = datetime.utcfromtimestamp(res['timestamp']).strftime('%x %X')
    latitude = res['iss_position']['latitude']
    longitude = res['iss_position']['longitude']
    position = rg.search((latitude, longitude))[0]
    fmt_position = (f"{position['name']}, {position['admin1']}")
    msg = f"""
    ```
    Time: {time}
    Position:
        Latitude: {latitude}
        Longitude: {longitude}
        Nearest City: {fmt_position}
    ```
    """
    await ctx.send(msg)


#@bot.event
#async def on_error(event, *args, **kwargs):
#    """Handle errors"""
#    with open("err.log", "a") as f:
#        if event == 'find_iss':
#            f.write(f"--UNHANDLED MESSAGE-- {args[0]}\n")
#        else:
#            raise

bot.run(TOKEN)
