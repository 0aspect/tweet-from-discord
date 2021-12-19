import time
import tweepy
import discord
from discord.ext import commands

token = "your bots token here"
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command("help")

badwords = {'add your list of not so friendly words here'}

consumer_key = " "
consumer_secret = " "

access_token = " "
access_token_secret = " "

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

@bot.event
async def on_ready():
    print("bot ready")
    await bot.change_presence(activity=discord.Game('tweeting'))

@bot.command()
async def twidder(ctx, *, arg):
    api.update_status(arg)
    twt=discord.Embed(title="Twidder Bot", description=f"https://twitter.com/add_your_twitter_handle_here", color=0x9900ff)
    twt.add_field(name="your tweet has been made", value=f"Tweet contents: ```{arg}```", inline=False)
    twt.set_footer(text="coded with shit code by aspect")
    await ctx.send(embed=twt)
    time.sleep(2)
    
bot.run(token)
