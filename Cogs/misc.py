import discord,time,aiohttp,color,util
from discord.ext import commands

from replit import db
from config import yeah
from util import url
from datetime import datetime
# 260047232065


class Misc(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  perms = {
    "admin": "https://discord.com/oauth2/authorize?client_id=902857424413798430&permissions=8&scope=bot",
    "none": "https://discord.com/oauth2/authorize?client_id=902857424413798430&permissions=0&scope=bot",
    "min": "https://discord.com/oauth2/authorize?client_id=902857424413798430&permissions=260047232065&scope=bot"
  }
  @commands.Cog.listener()
  async def on_ready(self):
    print(f"""| {self.__class__.__name__} Cog has been loaded\n------------------------------------------|""")

  @commands.command(name="invite", aliases=["inviteme"])
  async def invite(self,ctx):
    e = discord.Embed(
    title="Invite me to your server",
    description=f"**Admin perms:** [Click here]({self.perms['admin']}) \n\n**No perms:** [Click here]({self.perms['none']}) \n\n**Minimum perms:** [Click here]({self.perms['min']})",
    color=0x00ff00,
    url="https://github.com/NotFaizen/PyBot")
    await ctx.reply(embed=e, mention_author=False)
  @commands.command(name="ping", aliases=["latency"])
  async def pingpong(self,ctx):
    start_time=time.time()
    msg = await ctx.reply("Pinging...")
    end_time=time.time()

    bot_ping = round(self.bot.latency * 1000, 2)
    roundtrip = round((end_time - start_time) * 1000, 2)
    await msg.edit(content=f"Bot latency : `{bot_ping}` ms \nAPI latency: `{roundtrip}` ms")

  @commands.command(name="src",aliases=["source"])
  async def source_code(self,ctx):
    await ctx.send("PyBot's source code \nhttps://replit.com/@gofaizen/OwO#main.py")

  @commands.command(name="define", aliases=["def","urban" , "asyncdef"])
  async def define(self,ctx,*,query:str):
    bot = self.bot
    _query = url("encode", query)
    URL = f"https://apiv1.spapi.ga/fun/define?word={_query}"
    if (util.status_code(URL) != 200):
      return await ctx.reply("An error occurred, try again later.")
    res = await bot.func.jsonRequest(URL)
    word = res["word"]
    definition = res["definition"]
    example = res["example"]
    URL = res["urbanURL"]


    embed = discord.Embed(title=word, url=URL, color=ctx.author.color)
    embed.add_field(name="Definition", value=f"```\n{definition}\n```",inline=False)
    embed.add_field(name="Example", value=f"```\n{example}\n```")
    embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed) 

  @commands.command(description="Calculates the given expression")
  async def calc(self, ctx, *, expression):
        if len(expression) > 30:
            await ctx.send("**Too big equation**")
        else:
            st = expression.replace("+", "%2B")
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"https://api.mathjs.org/v4/?expr={st}"
                ) as response:
                    ex = await response.text()
                    if len(ex) > 200:
                        await ctx.send("Too big result")
                    else:
                        embed = discord.Embed(
                            timestamp=ctx.message.created_at,
                            title="Input",
                            description=f"```\n{expression}\n```",
                            color=0xFF0000,
                        )
                        embed.add_field(
                            name=f"Output", value=f"```\n{ex}\n```", inline=False
                        )
                        embed.set_thumbnail(url="")
                        await ctx.send(embed=embed)

  @commands.command(name="ocr", aliases=["recog"])
  async def ocr(self,ctx,*,image_url):
    url = f"https://api.ocr.space/parse/imageurl?apikey=helloworld&url={image_url}"
    res = await self.bot.func.jsonRequest(url)
    data = res["ParsedResults"][0]["ParsedText"]
    embed = discord.Embed(description=f"**Text:**\n{data}\n**Image:**",color=ctx.author.color)
    embed.set_image(url=image_url)
    await ctx.reply(embed=embed)
  @commands.command(name="avatar",aliases=["av","pfp"])
  async def avatar(self,ctx,member: discord.Member=None):
    if (member is None):
      member = ctx.author
    png = member.avatar_url_as(format="png")
    jpg = member.avatar_url_as(format="jpg")
    webp = member.avatar_url_as(format="webp")
    embed = discord.Embed(
      title=f"{member.name}'s avatar",
      color=ctx.author.color
      )\
    .add_field(
      name="Download links:", value=f"[png]({png}) | [jpg]({jpg}) | [webp]({webp})"
    )\
    .set_image(
      url=member.avatar_url
    )
    await ctx.reply(embed=embed)
  @commands.command(name="uptime",aliases=["up"])
  async def pybot_uptime(self,ctx):
    embed = discord.Embed(
      title="PyBot Uptime",
      description=f"Up since <t:{int(round(db.get('start_time')))}:R>",
      color=color.Color.azure()
    )
    await ctx.reply(embed=embed)
def setup(bot):
  bot.add_cog(Misc(bot))