#!/usr/bin/env python3

import os
import discord
import datetime
from discord.ext import tasks
from dotenv import load_dotenv
from votes import get_votes, get_sessions

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = discord.Client(intents=intents)

IMAGE_URL = "https://imageproxy.ifunny.co/resize:640x,quality:90x75/images/1e60fcae0eccf9b3ae1bce0a337127d1b5e3bfcff419978664dbb2dfb349154c_3.jpg"
CHANNEL_ID = 1036348210140156024 # Change to your own channel 
RESULTADOS_TSE = "https://resultados.tse.jus.br/oficial/app/index.html#/eleicao/resultados"

@bot.event
async def on_ready():
    print(f"[+] {bot.user} is working!")
    status.start()

@tasks.loop(minutes=1)
async def status():
    channel = bot.get_channel(CHANNEL_ID)
    embed = discord.Embed(
        title = "Eleições 2022",
        description = f"Seções apuradas: {get_sessions()}%",
        url = RESULTADOS_TSE,
        color = 0x00B2EE # Light Blue
    )

    today = datetime.datetime.now()
    today = today.strftime("%d de %b. %H:%M")

    embed.set_image(url=IMAGE_URL)
    embed.add_field(name="Resultados", value=get_votes(), inline=False)
    embed.set_footer(text=today)

    await channel.send(embed=embed)

try:
    load_dotenv()
    bot.run(os.getenv("TOKEN"))

except:
    print("""\nAn error occurred while loading your Discord Bot Token, 
so it is recommended to set up a dotenv file and add your token like this:\n
TOKEN="Your_Token"\n\nIf this is not the case, your token is probably not valid.""")
