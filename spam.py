import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix=".", intents=discord.Intents.all(), self_bot=True)

token = input("please input your token\n> ")

@client.event 
async def on_ready():
    print("Done!")
    print("example: .spam 10 1 text")

@client.command()
async def spam(ctx, coun = None, zad = None, *, text = None):
    if coun == None:
        print("Please input count message")
        await ctx.message.delete()
        print("example: .spam 10 1 text")
        return
    if text == None:
        print("Please input text on message")
        await ctx.message.delete()
        print("example: .spam 10 1 text")
        return
    if zad == None:
        for i in range(int(coun)):
            await ctx.send(text)
        print("example: .spam 10 1 text")
        return
    try:
        zad = str(zad)
    except:
        return
    for i in range(int(coun)):
        await ctx.send(text)
        await asyncio.sleep(int(zad))
        
try:
    client.run(token, bot=False)
except:
    print("Token is not valid")