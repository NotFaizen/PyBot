import discord,aiohttp,asyncio,os,io
from discord.ext import commands
from urllib.parse import quote
class Test(commands.Cog):
  def __init__(self,bot):
    self.bot = bot    
  @commands.Cog.listener()
  async def on_ready(self):
      print(f"""| {self.__class__.__name__} Cog has been loaded\n------------------------------------------|""")

  @commands.command(name="test1")
  async def test_1(self,ctx,*,argument):
    await ctx.reply(f"Argument = {argument}")
  @commands.command(name="test2")
  async def test_2(self,ctx,member:discord.User):
    await ctx.send(member.name)
  @commands.command(name="test3")
  async def test_3(self,ctx,emoji:discord.Emoji):
    await ctx.send(emoji.url)
def setup(bot):
  bot.add_cog(Test(bot))