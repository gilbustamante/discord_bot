"""GW2 Bot for Discord"""
import os
from discord.ext import commands
from dotenv import load_dotenv
import sys
from datetime import datetime
import random

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    """Runs when bot connects to Discord"""
    print(f"{bot.user.name} has connected to Discord")


@bot.command(name="ping")
async def ping_pong(ctx):
    """Respond to Ping with Pong"""
    response = "pong!"
    await ctx.send(response)



@bot.event
async def on_error(event, *args, **kwargs):
    """Handle errors"""
    with open("err.log", "a") as f:
        if event == 'on_message':
            f.write(f"UNHANDLED MESSAGE ({datetime.now()}): {args[0]}\n"
                    f"Exception info: {sys.exc_info()}\n")
        else:
            raise

@bot.command(name="roll")
async def roll_dice(ctx, number_of_dice: int, number_of_sides: int):
    """Roll the dice!"""
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

bot.run(TOKEN)
