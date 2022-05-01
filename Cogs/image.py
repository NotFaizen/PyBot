import discord,requests,os,asyncio
from discord.ext import commands
from aioify import aioify

def gravey(image):
    url = f"https://api.bsmnt.cf/maker/v1?&image1={image}&background=https://cdn.discordapp.com/attachments/850033801581297755/932223750806569011/589f095464b351149f22a8a3.png&canvaswidth=1200&canvasheight=1200&image1x=310&image1y=510&image1width=450&image1height=450"
    r = requests.get(url)
    with open("dumb_shit/grave.png","wb") as f:
      f.write(r.content)
      f.close()
grave_maker = aioify(obj=gravey)
class Image(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  @commands.Cog.listener()
  async def on_ready(self):
      print(f"""| {self.__class__.__name__} Cog has been loaded\n------------------------------------------|""")


  @commands.command()
  async def grave(self,ctx,*,member: discord.Member=None):
    if (member is None):
      member = ctx.author
    avatar = str(member.avatar_url_as(format="png"))[:-10]
    await grave_maker(image=avatar)
    file = discord.File("dumb_shit/grave.png")
    await ctx.reply(file=file)
    os.remove("./dumb_shit/grave.png")

def setup(bot):
  bot.add_cog(Image(bot))
