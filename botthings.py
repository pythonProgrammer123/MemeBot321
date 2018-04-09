import discord
import asyncio
import random
import praw
import time

reddit = praw.Reddit(client_id = 'uueNV9hwkRDWrw',
                     client_secret = 'cvSw7_mvx2_TrqfeyMWrBOthqNI',
                     username = 'FetcherBot321',
                     password = 'iqmal102',
                     user_agent = 'prawUsementsv1')

subreddit = reddit.subreddit("dankmemes")

hot_me_irl = subreddit.new(limit = 1)




client = discord.Client()

chat_filter = ["GAY"]

@client.event
async def on_ready():
    print("-----------")
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("BOT IS READY!")
    print("------------")


@client.event
async def on_message(message):
    channel = client.get_channel("lagu_pacak")
    print(message.author.name)
    print(message.author.id)
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            await client.send_message(message.channel, "***DID SOMEONE JUST SAY GAY? LMAO YOU NIGGAS GAY!***")
            await client.send_message(message.channel, "https://imgur.com/gallery/f4jxP")
        

            
            



client.run("NDMxNzA3NDIzMTgzNjAxNjc1.DairLw.ATPy-bDKdqqycmN7RjPUtWNq18Y")


