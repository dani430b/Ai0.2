import discord
from discord.ext import commands
from diffusers import StableDiffusionPipeline
import torch
import os

from authtoken import auth_token
from discord.ext.commands.context import Context

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", revision="fp16", torch_dtype=torch.float16, use_auth_token=auth_token, device_map="auto")

intents = discord.Intents.default()
intents.message_content = True
#client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="$", intents=intents)

class Generate(commands.Converter):
    pass

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def gen(ctx, arg):
    arg2 = arg
    await ctx.send("Generating")
    image = pipe(arg2).images[0]
    image.save(f"Picture.png")
    await ctx.channel.send(file=discord.File("picture.png"))
    
@bot.command()
async def show(ctx):
    await ctx.channel.send(file=discord.File("picture.png"))

bot.run("MTE1Nzc1NTQ1NDI1MjkxMjc3MQ.GfFzA0.g-_giLzGRLv8RJm4bCF37I01QoBOJF9z7NoDSU")