import discord,aiohttp,asyncio,os,io
from discord.ext import commands
from urllib.parse import quote
from util import getNSFW
class NSFW(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  @commands.Cog.listener()
  async def on_ready(self):
      print(f"""| {self.__class__.__name__} Cog has been loaded\n------------------------------------------|""")
  embed = discord.Embed(color=discord.Colour.random())
  @commands.command(name="ass")
  @commands.is_nsfw()
  async def ass(self,ctx):
    self.embed.set_image(url=await getNSFW("ass"))
    await ctx.reply(mention_author=False, embed=self.embed)

  @commands.command(name="bdsm")
  @commands.is_nsfw()
  async def bdsm(self,ctx):
    self.embed.set_image(url=await getNSFW("bdsm"))
    await ctx.reply(mention_author=False, embed=self.embed)
  
  @commands.command(name="blowjob")
  @commands.is_nsfw()
  async def blow(self,ctx):
    self.embed.set_image(url=await getNSFW("blowjob"))
    await ctx.reply(mention_author=False, embed=self.embed) 

  @commands.command(name="boobs")
  @commands.is_nsfw()
  async def boobas(self,ctx):
    self.embed.set_image(url=await getNSFW("boobs"))
    await ctx.reply(mention_author=False, embed=self.embed)

  @commands.command(name="futanari")
  @commands.is_nsfw()
  async def futa(self,ctx):
    self.embed.set_image(url=await getNSFW("futanari"))
    await ctx.reply(mention_author=False, embed=self.embed)

  @commands.command(name="hentai")
  @commands.is_nsfw()
  async def hentai(self,ctx):
    self.embed.set_image(url=await getNSFW("hentai"))
    await ctx.reply(mention_author=False, embed=self.embed)

  @commands.command(name="lewdneko")
  @commands.is_nsfw()
  async def loodneko(self,ctx):
    self.embed.set_image(url=await getNSFW("lewdneko"))
    await ctx.reply(mention_author=False, embed=self.embed)

  @commands.command(name="succubus")
  @commands.is_nsfw()
  async def succubi(self,ctx):
    self.embed.set_image(url=await getNSFW("succubus"))
    await ctx.reply(mention_author=False, embed=self.embed)


  
  
def setup(bot):
  bot.add_cog(NSFW(bot))