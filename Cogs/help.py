import discord; import config
from discord.ext import commands
from util import help_embed
class HelpCommand(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
      print(f"""| {self.__class__.__name__} Cog has been loaded\n------------------------------------------|""")

  ######## MAIN HELP COMMAND ########
  @commands.group(invoke_without_command=True)
  async def help(self,ctx):
    embed = discord.Embed(title="Help", color=ctx.author.color,description="Run `py!help <command>` for extensive help on a command")\
    .add_field(name="Fun", value="`joke`, `mock`, `ds`, `neko`, `8ball`, `chat`, `choice`",inline=False)\
    .add_field(name="Image",value="`discordsays`, `berk`, `biden`, `grave`",inline=False)\
    .add_field(name="Utils", value="`count-brackets`, `bio`, `setbio`, `discrim`, `avatar`")\
    .add_field(name="Misc", value="`ping`, `invite`, `define`, `ocr`",inline=False)
    if (await self.bot.is_owner(ctx.author)):
      embed.add_field(name="Developer", value="`reload`, `eval`, `jsk`, `alteval`",inline=False)
    if (ctx.channel.is_nsfw()):
      embed.add_field(name="NSFW", value="`ass`, `bdsm`, `blowjob`, `boobs`, `futanari`, `hentai`, `lewdneko`, `succubus`", inline=False)
    embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed, mention_author=False)

  ############# SUB COMMANDS #############

  ######## FUN COMMANDS ########
  @help.command()
  async def joke(self,ctx):
    bot=self.bot
    await bot.func.help_embed(
      ctx,
      "joke",
      description="Sends some funny jokes for you to laugh at",
      usage="py!joke", 
      example="py!joke"
    )
  @help.command()
  async def mock(self,ctx):
    await help_embed(
      ctx,
      command="mock",
      description="Returns your text in a sarcastic tone",
      usage="py!mock <text_to_mock>", 
      example="""py!mock when the impostor is sus
      py!mock this bot is goose
      py!mock Add this bot to your server for a cookie
      py!mock It's wednesday my dudes
      py!mock It's a constructor, "__init__"?
      """
    )
  @help.command()
  async def biden(self,ctx):
    await help_embed(
      ctx,
      command="biden",
      description="Make Joe ~~Mama~~ Biden tweet your text",
      usage="py!biden <text>", 
      example="""py!mock I hereby change my name to joe mama
      py!biden Follow TheRealFaizen on twitter
      py!biden Hello America!
      py!biden Look ma I won the elections :>
      py!biden Trump who?
      """
    )
  @help.command()
  async def berk(self,ctx):
    berk = str(await self.bot.fetch_user(551786741296791562))
    await help_embed(
      ctx,
      command="berk",
      description=f"Make `@{berk}` say anything",
      usage="py!berk <text>",
      example="""py!berk Bye World!
      py!berk I am berk
      py!berk NotFaizen is cool 
      py!berk deez nuts
      py!berk Join basement developers or else...
      """
      )
  @help.command()
  async def discordsays(self,ctx):
    await help_embed(
      ctx,
      command="discordsays",
      description=f"Creates a fake discord message",
      usage="py!discordsays <user>",
      example="py!discordsays @NotFaizen"
      )
  @help.command()
  async def ds(self,ctx):
    await help_embed(
      ctx,
      command="ds",
      aliases="doublestruck",
      description=f"Sends your text with doublestruck font",
      usage="py!ds <text>",
      example="py!ds when the impostor is sus"
      )
  @help.command()
  async def neko(self,ctx):
    await help_embed(
      ctx,
      command="neko",
      description=f"Cat girls? Hell yeah.",
      usage="py!neko",
      example="py!neko"
      )
  @help.command(name="8ball")
  async def _8ball(self,ctx):
    await help_embed(
      ctx,
      command="8ball",
      description=f"Ask the mighty 8ball any question",
      usage="py!8ball <question>",
      example="py!8ball Will I ever get a girlfriend?"
    )

  @help.command(name="chat")
  async def chatbot(self,ctx):
    await help_embed(
      ctx,
      command="chat",
      description=f"Chat with the bot",
      usage="py!chat <message>",
      example=f"py!chat hello"
    )
  ######## MISC COMMANDS ########
  @help.command()
  async def ping(self,ctx):
    await help_embed(
      ctx,
      command="ping",
      aliases="latency",
      description=f"Shows the bot's latency in ms",
      usage="py!ping",
      example="py!ping"
    )
  @help.command()
  async def invite(self,ctx):
    await help_embed(
      ctx,
      command="invite",
      aliases="inviteme",
      description=f"Returns the bot's invite link",
      usage="py!invite",
      example="py!invite"
    )
  ######## UTILITY COMMANDS ########  
  @help.command()
  async def setbio(self,ctx):
    await help_embed(
      ctx,
      command="setbio",
      description=f"Set's your bio which you can view later (tip: you can use markdown)",
      usage="py!setbio <bio_content>",
      example="py!setbio Omae wa mou shindeiru"
    )
  @help.command()
  async def bio(self,ctx):
    await help_embed(
      ctx,
      command="bio",
      description=f"Returns your or the mentioned user's bio",
      usage="py!bio [user_id / username / username+tag]",
      example=f"py!bio NotFaizen\npy!bio NotFaizen#02222\npy!bio {config.owner_id}"
    )
  @help.command()
  async def define(self,ctx):
    await help_embed(
      ctx,
      command="define",
      aliases="def, asyncdef, urban",
      description=f"Search for anything on urban dictionary",
      usage="py!define <query>",
      example=f"py!define reddit"
    )
  @help.command(name="count-brackets")
  async def count_brackets(self,ctx):
    await help_embed(
      ctx,
      command="count-brackets",
      aliases="countbrackets, bracket-count, bracketcount",
      description=f"Count the number of brackets in your code",
      usage="py!count-brackets <code>",
      example=f"py!count-brackets await ctx.send(\"hi\")"
    )
  @help.command(name="ocr")
  async def ocr(self,ctx):
    await help_embed(
      ctx,
      command="ocr",
      aliases="recog",
      description=f"Extract text from an image",
      usage="py!ocr <image_url>",
      example=f"py!ocr https://cdn.gofaizen.xyz/gone.png"
    )
  @help.command(name="discrim")
  async def discrim(self,ctx):
    await help_embed(
      ctx,
      command="discrim",
      description=f"Displays all users with a specific tag",
      usage="py!discrim [tag]",
      example=f"""py!discrim
      py!discrim 0001
      py!discrim #0001"""
    )
  @help.command(name="grave")
  async def grave(self,ctx):
    await help_embed(
      ctx,
      command="grave",
      description=f"Displays your or a member's avatar on a grave overlay",
      usage="py!grave [user_id / username / username+tag]",
      example=f"""py!grave
      py!grave NotFaizen
      py!grave {config.owner_id}
      py!grave NotFaizen#0222"""
    )
def setup(bot):
  bot.add_cog(HelpCommand(bot))