from time import time
import time as Time
from discord.ext import commands
from inspect import getsource
import discord,os,sys,random,math,util,aiohttp,asyncio,requests
from popcat_wrapper import popcat_wrapper as pop
import numpy as np

class EvalCommand(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    def resolve_variable(self, variable):
        if hasattr(variable, "__iter__"):
            var_length = len(list(variable))
            if (var_length > 100) and (not isinstance(variable, str)):
                return f"<a {type(variable).__name__} iterable with more than 100 values ({var_length})>"
            elif (not var_length):
                return f"<an empty {type(variable).__name__} iterable>"
        
        if (not variable) and (not isinstance(variable, bool)):
            return f"<an empty {type(variable).__name__} object>"
        return (variable if (len(f"{variable}") <= 1000) else f"<a long {type(variable).__name__} object with the length of {len(f'{variable}'):,}>")
    
    def prepare(self, string):
        arr = string.strip("```").replace("py\n", "").replace("python\n", "").split("\n")
        if not arr[::-1][0].replace(" ", "").startswith("return"):
            arr[len(arr) - 1] = "return " + arr[::-1][0]
        return "".join(f"\n\t{i}" for i in arr)
    
    @commands.Cog.listener()
    async def on_ready(self):
      print(f"""| {self.__class__.__name__} Cog has been loaded\n------------------------------------------|""")

    @commands.command(pass_context=True, aliases=['eval', 'exec', 'evaluate', 'ev'])
    @commands.is_owner() # reset for owner
    async def _eval(self, ctx, *, code: str):
        silent = ("-s" in code)
        
        code = self.prepare(code.replace("-s", ""))
        args = {
            "discord": discord,
            "sauce": getsource,
            "commands": commands,
            "sys": sys,
            "os": os,
            "import": __import__,
            "this": self,
            "ctx": ctx,
            "bot": self.bot,
            "random": random,
            "pop": pop,
            "utils": util,
            "time": Time,
            "math": math,
            "numpy": np,
            "aiohttp": aiohttp,
            "asyncio": asyncio,
            "requests": requests,
            "asyncio": asyncio,
            "channel": ctx.channel,
            "author": ctx.author,
            "guild": ctx.guild,
            "message": ctx.message
        }
        
        try:
            exec(f"""async def func():
            {code} 
            """, args)
            a = time()
            response = await eval("func()", args)
            await ctx.message.add_reaction("✅")   
            if silent or (response is None) or isinstance(response, discord.Message):
                del args, code
                return
                     
            await ctx.send(f"```py\n{self.resolve_variable(response)}```")
        except Exception as e:
            await ctx.send(f"Error occurred:```\n{type(e).__name__}: {str(e)}```")
        
        del args, code, silent
        
def setup(bot):
    bot.add_cog(EvalCommand(bot))