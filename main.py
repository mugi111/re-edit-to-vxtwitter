from discord.ext import commands
import discord

import config

from urlextract import URLExtract
extractor = URLExtract()
from urllib.parse import urlparse


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(
    command_prefix='/',
    intents=intents
)


@bot.event
async def on_message(msg: discord.Message):
    if msg.author.bot:
        return
    urls=extractor.find_urls(msg.content)
    if urls:
        for url in urls:
            domain = urlparse(url).hostname
            if domain in config.detect_list:
                if urlparse(url).path.split('/')[2] == 'status':
                    await msg.reply(url.replace(domain, 'vxtwitter.com'))

bot.run(config.token)
