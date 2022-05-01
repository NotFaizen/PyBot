import discord; import random
from discord.ext import commands
from replit import db
from config import yeah
from util import isNaN
from pag import Pag
class Utilities(commands.Cog):
  def __init__(self,bot):
    self.bot = bot    
  @commands.Cog.listener()
  async def on_ready(self):
      print(f"""| {self.__class__.__name__} Cog has been loaded\n------------------------------------------|""")
  @commands.command(name="bio")
  async def get_bio(self, ctx, member:discord.User=None):
    if member == None:
      member = ctx.author

    bio = db.get(f"{member.id}_bio")

    if db.get(f"{ctx.author.id}_bio") == None:
      return await ctx.send("You haven't set a bio yet")
    if bio == None:
      return await ctx.reply(f"No bio found for this user in the database")
    embed = discord.Embed(
      title=f"{member}'s bio",
      description=f"{bio}",
      color=ctx.author.color
    ).set_footer(text="Set a bio using py!setbio")
    await ctx.reply(embed=embed,mention_author=False)

  @commands.command(name="setbio")
  async def set_bio(self,ctx,*, bio_content):
    db[f"{ctx.author.id}_bio"] = bio_content
    await ctx.reply(f"{yeah} Set your bio to `{bio_content}`, use `py!bio` to view it.")
  
  @commands.command(name="count-brackets", aliases=["countbrackets", "bracket-count", "bracketcount"])
  async def count_brackets(self,ctx,*,text:str):
    sqr = {
      "left": text.count("]"),
      "right": text.count("[")
    }
    # curly = {
    #   "left": text.count("}"),
    #   "right": text.count("{")
    # }
    _round = {
      "left": text.count(")"),
      "right": text.count("(")
    }
    dol = text.count("$")
    semi = text.count(";")
    await ctx.reply(f"""
`[` = {sqr["right"]}
`]` = {sqr["left"]}
`)` = {_round["left"]}
`(` = {_round["right"]}
`$` = {dol}
`;` = {semi}
    """)
  @commands.command(name="discrim")
  async def discriminator(self,ctx,*,discrim:str=None):
    if (discrim is None):
      discrim = str(ctx.author.discriminator)
    
    disc = discrim.replace("#","")
    if ((len(disc) > 4) or (len(disc) < 4)):
      return await ctx.reply("Not a valid discriminator")
    if (isNaN(disc)):
      return await ctx.reply("Not a valid discriminator")
    members = "\n".join([str(member) for member in ctx.guild.members if (member.discriminator == disc)])

    members = str(members)
    pager = Pag(
      colour=ctx.author.color,
      timeout=100,
      entries=[members[i : i + 300] for i in range(0, len(members), 300)],
      length=1
    )
    await pager.start(ctx)
def setup(bot):
  bot.add_cog(Utilities(bot))
