from discord.ext import commands
from discord.ext.commands import *
import asyncio,traceback

class ErrorHandler(commands.Cog):
  """A cog for global error handling."""

  def __init__(self, bot: commands.Bot):
      self.bot = bot

  @commands.Cog.listener()
  async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
    """A global error handler cog."""
    owner = await self.bot.fetch_user(672791500995690517)
    reset = await self.bot.fetch_user(424133185123647488)
    if isinstance(error, CommandNotFound):
        return
    elif isinstance(error, CommandOnCooldown):
        message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds."
    elif isinstance(error, MissingPermissions):
        message = f"You need the `{error.missing_perms.upper()}` permission to run this command"
    elif isinstance(error, MissingRequiredArgument):
        message = f"Missing a required argument: `{error.param}`"
    elif isinstance(error, UserInputError):
        message = "Something about your input seems fishy, please check your input and try again!"
    elif isinstance(error, NotOwner):
        return
    elif isinstance(error, CommandInvokeError):
        message = f"Command raised an error: ```py\n{error}\n```"
    elif isinstance(error, TooManyArguments):
        message = "Too many arguments were passed. Pass the correct amount of arguments and try again."
    elif isinstance(error, NSFWChannelRequired):
        message = "This command can only be used in an NSFW channel."
    elif isinstance(error, BotMissingPermissions):
      message = f"I am missing {error.missing_perms.upper()} perms. Try again after giving me the perms."
    else:
        message = "Something went wrong, try again later."
        await asyncio.sleep(1)
        raise error
    return await ctx.reply(message)

def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))
