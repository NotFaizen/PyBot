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
from replit import db

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

class Utilities:
  def botCommands(separator=", "):
    return separator.join([str(each) for each in list(bot.commands)])

  def serverNames(separator=", "):
    return separator.join([str(each) for each in list(bot.guilds)])

  async def channelSendMessage(channelID,message:str):
    await bot.get_channel(channelID).send(message)

  async def help_embed(ctx:commands.Context,command:str,example,usage,description,cooldown:int="None",aliases:str="None"):
    embed = discord.Embed(description=f"""**Description:** {description} \n**Cooldown:** {cooldown} \n**Usage:** `{usage}` \n**Aliases:** {aliases} \n**Example:** \n{example}""", color=ctx.author.color).set_author(name=f"Command: py!{command}", icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed)

bot.func = util
bot.test_func = Utilities
bot.key = os.getenv("key")

@bot.listen()
async def on_message(message):
  if (message.author.bot):
    return
  if (message.author == bot.user):
    return
  if (f"<@!{bot.user.id}>" in message.content) or (f"<@{bot.user.id}>" in message.content):
    embed = discord.Embed(description=f"Hi **{message.author.name}**! My prefix is `Py!`, run `Py!help` to get started.",color=message.author.color).set_author(name="PyBot", icon_url=bot.user.avatar_url).set_footer(text="The prefix and all commands are case insensitive")
    await message.reply(embed=embed)
@bot.event
async def on_connect():
  print(cf.green("Connected to discord!"))

@bot.event
async def on_ready():
  db.set("start_time",time.time())
  print(cf.green(f"Logged in as {bot.user}!\n|-----------------------------------------|"))
  
keep_alive()

def berker(text):
  text = quote(str(text))
  r = requests.get(f"https://app.resetxd.repl.co/berk?text={text}")
  with open("./dumb_shit/berk.png","wb") as thefile:
      thefile.write(r.content)
      thefile.close()


berk_maker_9000 = aioify(obj=berker)

@bot.command()
async def berk(ctx,*,text):
  await berk_maker_9000(text=text)
  file = discord.File("./dumb_shit/berk.png")
  await ctx.reply(file=file)

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
    "asyncio": asyncio,
    "channel": ctx.channel,
    "author": ctx.author,
    "guild": ctx.guild,
    "message": ctx.message,
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