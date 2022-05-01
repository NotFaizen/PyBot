import popcat_wrapper.popcat_wrapper as pop
import os, discord, aiohttp,asyncio,re
from discord.ext import commands
from random import choice

def textSplit(string:str, separator:str):
  muhlist = string.split(separator)
  return [ each.strip() for each in muhlist ]
class Fun(commands.Cog):
  def __init__(self,bot):
    self.bot = bot    
  @commands.Cog.listener()
  async def on_ready(self):
      print(f"""| {self.__class__.__name__} Cog has been loaded\n------------------------------------------|""")

  @commands.command(name="biden")
  async def biden(self,ctx, *, text):
    embed = discord.Embed(title="Biden tweeted", color=discord.Colour.random())
    embed.set_image(url=await pop.biden(text))
    await ctx.reply(embed=embed)
  @commands.command() 
  async def joke(self,ctx):
    try:
      await ctx.reply(await pop.joke())
    except Exception as e:
      await ctx.reply("An error occurred while retrieving the joke; this is most likely an internal error, try again later")
      print(e)
  @commands.command()
  async def mock(self,ctx, *, text):
    res = await pop.mock(text)
    return await ctx.reply(res)
  @commands.command()
  async def neko(self,ctx):
    url = "https://nekos.best/api/v1/nekos"
    try:
      async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
          data = await r.json()
          e = discord.Embed(title="Random Nekos", color=discord.Colour.random())
          e.set_image(url=data['url'])
          e.set_footer(text="Powered by nekos.best")
          await ctx.reply(embed=e,mention_author=False)
    except:
      await ctx.reply("An error occurred")
  @commands.command(name="ds", aliases=["doublestruck"])
  async def ds(self,ctx, *, text):
    await ctx.reply(await pop.doublestruck(text), mention_author=False)
  @commands.command(name="chat")
  async def chat(self,ctx,*,message):
    async with aiohttp.ClientSession() as cs:
      async with cs.get(f"https://apiv2.spapi.ga/misc/clever?text={message}") as r:
        data = await r.json()
        await ctx.reply(
          data['response'] if (r.status == 200) else "There was an error while invoking this command."
        )
  @commands.command(name="8ball")
  async def _8ball(self,ctx,*,question):
    key = os.getenv("key")
    res = await self.bot.func.jsonRequest(f"https://api.gofaizen.repl.co/fun/8ball?key={key}","response")
    
    embed = discord.Embed(title="The magical 8ball",color=ctx.author.color)
    embed.add_field(name="Your question", value=f"```\n{question}\n```",inline=False)
    embed.add_field(name="8ball's answer", value=f"```\n{res}\n```",inline=False)
    await ctx.reply(embed=embed)
  @commands.command(name="choose",aliases=["choice"])
  async def choose(self,ctx,*,choices: str=None):
    if (choices is None) or not ("," in choices):
      return await ctx.reply("You need to provide two or more messages separated by commas")
    Choice = textSplit(choices,",")
    if (len(Choice) < 2):
      return await ctx.reply("You need to provide two or more messages separated by commas")
    random = choice(Choice)
    msg = await ctx.reply(f"Choosing...")
    await asyncio.sleep(1)
    await msg.edit(content=f"I choose `{random}`")


  @commands.command(name="owo",aliases=["owofy"])
  async def owoowow(self,ctx,*,string: str=None):
    # you wait here i come in a min after looking into how regex works in python 
    # you need the `re` module ik ik
    if (string is None):
      return await ctx.reply("where the string to owofy")

    faces=["(・`ω´・)",";;w;;","owo","UwU",">w<","^w^"];
    string = re.sub(r"/(?:r|l)/g", "w", string)
    string = re.sub(r"/(?:R|L)/g", "W", string)
    string = re.sub(r"/n([aeiou])/g", "ny$1", string)
    string = re.sub(r"/N([aeiou])/g", "Ny$1", string)
    string = re.sub(r"/N([AEIOU])/g", "", string)
    string = re.sub(r"/ove/g", "uv", string)
    string = re.sub(r"/\!+/g", " "+ choice(faces)+ " ", string)
    await ctx.send(string)
    
def setup(bot):
  bot.add_cog(Fun(bot))