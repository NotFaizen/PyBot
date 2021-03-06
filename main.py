import os
os.system("pip install resql==0.1.5")

from prettyprinter import pprint
import os,discord,requests,util,asyncio,io,contextlib,textwrap
import time,random,math,aiohttp,numpy,config
import colorful as cf
import popcat_wrapper.popcat_wrapper as pop


from aioify import aioify
from urllib.parse import quote
from discord.ext import commands
from discord.ext.commands import when_mentioned_or
from keep_alve import keep_alive
from traceback import format_exception
from datetime import datetime
from resql import ReSql
from color import Color
from threading import Thread

prefixes: tuple = ("py!", "PY!", "Py!", "pY!")
cf.use_style("monokai")


bot = commands.Bot(
  allowed_mentions=discord.AllowedMentions.none(),
  command_prefix=when_mentioned_or("py!", "PY!", "Py!", "pY!"),
  case_insensitive=True,
  intents=discord.Intents.all(),
  strip_after_prefix=True,
  owner_ids=config.owners,
  help_command=None
)

db = ReSql("gibmeyanfei.db")

class Utilities:
  def botCommands(separator=", "):
    return separator.join([str(each) for each in list(bot.commands)])

  def serverNames(separator=", "):
    return separator.join([str(each) for each in list(bot.guilds)])

  async def channelSendMessage(channelID,message:str):
    await bot.get_channel(channelID).send(message)

bot.db = db
bot.func = util
bot.test_func = Utilities
bot.key = os.getenv("key")
bot.Color = Color ; bot.Colour = Color
bot.time = time.time()

keep_alive()

def berker(text):
  time = None
  text = quote(str(text))
  who = bot.get_user(551786741296791562)
  name = quote(str(who.name))
  avatar = who.avatar_url
  url = f"https://api-production-adc9.up.railway.app/discordsays?avatar={avatar}&username={name}&message={text}"
  r = requests.get(url)
  with open("./dumb_shit/berk.png","wb") as thefile:
    thefile.write(r.content)
berk_maker_9000 = aioify(obj=berker)

@bot.event
async def on_ready():
  print(cf.green(f"Logged in as {bot.user}!\n|-----------------------------------------|"))

@bot.event
async def on_connect():
  print(cf.green("Connected to discord!"))

@bot.event
async def on_message_edit(before, after):
  if after.content != before.content:
    await bot.process_commands(after)

@bot.listen("on_message")
async def ping_for_prefix(message):
  if (message.author.bot):
    return
  if (message.author == bot.user):
    return
  if (f"<@!{bot.user.id}>" in message.content) or (f"<@{bot.user.id}>" in message.content):
    embed = discord.Embed(
      description=f"Hi **{message.author.name}**! My prefix is `Py!`, run `Py!help` to get started.",
      color=message.author.color
    )
    embed.set_author(name="PyBot", icon_url=bot.user.avatar_url)
    embed.set_footer(text="The prefix and all commands are case insensitive")
    await message.reply(embed=embed)

@bot.command()
async def berk(ctx,*,text):
  await berk_maker_9000(text)
  file = discord.File("./dumb_shit/berk.png")
  await ctx.reply(file=file)
  os.remove("dumb_shit/berk.png")
@bot.command(name="alteval")
@commands.is_owner()
async def _eval(ctx, *, code):
  from util import clean_code
  from pag import Pag
  await ctx.reply("Let me evaluate this code for you! Won't be a sec")
  code = clean_code(code)

  local_variables = {
    "discord": discord,
    "commands": commands,
    "bot": bot,
    "ctx": ctx,
    "commands": commands,
    "os": os,
    "import": __import__,
    "random": random,
    "pop": pop,
    "utils": util,
    "time": time,
    "math": math,
    "numpy": numpy,
    "aiohttp": aiohttp,
    "requests": requests,
    "asyncio": asyncio,
    "channel": ctx.channel,
    "author": ctx.author,
    "guild": ctx.guild,
    "message": ctx.message
  }

  stdout = io.StringIO()

  try:
      with contextlib.redirect_stdout(stdout):
          exec(
              f"async def func():\n{textwrap.indent(code, '    ')}", local_variables,
          )

          obj = await local_variables["func"]()
          result = f"{stdout.getvalue()}\n-- {obj}\n"
  except Exception as e:
      result = "".join(format_exception(e, e, e.__traceback__))

  pager = Pag(
      colour=ctx.author.color,
      timeout=100,
      title="Paginator paginating pagination",
      entries=[result[i : i + 1000] for i in range(0, len(result), 1000)],
      length=1,
      prefix="```py\n",
      suffix="```",
  )

  await pager.start(ctx)

if __name__ == "__main__":
  for cog in os.listdir('./Cogs'):
    if (cog.endswith(".py")) and not (cog.startswith("_")):
      bot.load_extension(f'Cogs.{cog[:-3]}')
  bot.load_extension("jishaku")
  bot.run(os.getenv("token"))