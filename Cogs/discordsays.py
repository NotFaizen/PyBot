from discord.ext import commands
import discord,os
from aioify import aioify
from requests import get
from util import encodeURIComponent
def writer(link):
  rep = get(link)
  with open("./dumb_shit/file.png","wb") as lefile:
    lefile.write(rep.content)
    lefile.close()
  

writermethod = aioify(obj=writer)

class discordsays(commands.Cog):
    def __init__(self,bot):
      self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
      print(f"""| {self.__class__.__name__} Cog has been loaded\n------------------------------------------|""")

    @commands.command(pass_context=True)
    async def discordsays(self, ctx,who:discord.Member=None):
      if (who is None):
        return await ctx.reply("You need to mention someone or use their username, id or username and tag")
      baseLink = f"https://resapi.up.railway.app/discordsays?avatar={who.avatar_url}&username={encodeURIComponent(str(who.name))}"
      def checker(m):
        return m.channel == ctx.channel and m.author == ctx.author
      
      msg = await ctx.send("what message?")
      response = await self.bot.wait_for("message",check=checker)
      message_content = response.content
      baseLink += f"&message={encodeURIComponent(str(message_content))}"
      await msg.edit(content="what color? [no can be a answer too]")
      response = await self.bot.wait_for("message",check=checker)
      if "no" in response.content or "No" in response.content:
        pass
      else:
        color = response.content
        baseLink += f"&color=%23{str(color)}"
      await msg.edit(content="what time? [no can be a answer too] [default is set to `Today at 03:00 AM`] ")
      response = await self.bot.wait_for("message",check=checker)
      if "no" in response.content or "No" in response.content:
        pass
      else:
        color = response.content
        baseLink += f"&time={encodeURIComponent(str(color))}"
      await writermethod(baseLink)
      file = discord.File("./dumb_shit/file.png")
      await ctx.send(file=file)
      os.remove("dumb_shit/file.png")
def setup(bot):
  bot.add_cog(discordsays(bot))