import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def test(ctx):
    await ctx.send("Hello!")

bot.run("MTE2NzE4MTE2MzI3ODg5NzIwMg.GlULAO.hG1DEthmFTnpHHrpfnheD14ipcRbGuLjrMCOL8")




