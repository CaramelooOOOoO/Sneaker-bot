import discord
from discord.ext import commands
from a import search

token = "MTAwOTUyMTI1NDI1ODIwMDYwNw.GMDdeg.UBWgRpQ9tclo4vEciTC1D9Y-BqHLoFWisM1wtc"

client = discord.Client(intents=discord.Intents.default())

channel_id = "1009530167082876939"

@client.event
async def on_message(message):
    if message.content.split(' ')[0] == '>stockx':
        query = message.content.replace('>stockx ', '') 
        
        item = search(query)
        
        embed = discord.Embed(
            title=item["title"],
            url="https://stockx.com/" + item["shortDescription"]
        )
        embed.set_thumbnail(
            url=item['media']['imageUrl']
        )
        embed.add_field(
            name='Colourway',
            value=item['colorway']
        )
        embed.add_field(
            name='Style ID',
            value=item['styleId']
        )
        embed.add_field(
            name='ID',
            value=item['shortDescription']
        )
        embed.add_field(
            name='Last Sale',
            value=item['market']['lastSale']
        )
             
        
        
        await message.channel.send(embed=embed)
           
client.run(token)