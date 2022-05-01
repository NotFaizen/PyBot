import discord,aiohttp,asyncio,os,io,config,sys,time
from discord.ext import commands
from urllib.parse import quote
from aioify import aioify
class Developer(commands.Cog):
  def __init__(self,bot):
    self.bot = bot    
  @commands.Cog.listener()
  async def on_ready(self):
      print(f"""| {self.__class__.__name__} Cog has been loaded\n------------------------------------------|""")
  @commands.command(name="reload")
  @commands.is_owner()
  async def reload(self, ctx,*, extension=None):
    bot = self.bot
    command_count = len(bot.commands)
    # if extension is None reload all cogs
    if (extension == None):
      for filename in os.listdir('./Cogs'):
        if filename.endswith(".py") and not filename.startswith("_"):
          bot.reload_extension(f'Cogs.{filename[:-3]}')
          bot.reload_extension("jishaku")
          embed = discord.Embed(title='Reload', description=f'{config.yeah} Successfully reloaded {command_count} commands!', color=discord.Colour.green())
      await ctx.reply(embed=embed, mention_author=False)
    # else reload the specified cog
    else:
      bot.reload_extension(f"Cogs.{extension}")
      embed = discord.Embed(description=f'{config.yeah} Successfully reloaded {extension} cog', color=discord.Colour.green())
      await ctx.reply(embed=embed, mention_author=False)
  @commands.command(name="readfile",aliases=['rf', " readfile", " rf"])
  @commands.is_owner()
  async def read_file(self,ctx,path:str):
    try:
      res = self.bot.func.readFile(path)
      if (len(res) < 2000):
        await ctx.reply(f"```py\n{res}\n```", mention_author=False)
      else:
        file = discord.File(path)
        await ctx.reply(file=file)
    except FileNotFoundError:
      # await ctx.reply(f"No such file or directory: '{path}'")
      pass
  @commands.command(name="reboot",aliases=["restart"])
  async def restartt_datt_bott(self,ctx):
    def restart_bot():
      time.sleep(1)
      os.execv(sys.executable, ['python'] + sys.argv)

    reset = aioify(obj=restart_bot)
    @commands.command(name= 'restart')
    async def restart(self,ctx):
      msg = await ctx.send("Restarting bot...")
      await asyncio.sleep(1)
      reset()
      await asyncio.sleep(1)
      await msg.edit(content="Bot Successfully")

def setup(bot):
  bot.add_cog(Developer(bot))