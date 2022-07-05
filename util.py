import numpy as np
import aiohttp,discord,os,requests,config
from discord.ext import commands
import random as rand
from resql import ReSql
from aiohttp import ClientSession
from urllib.parse import quote,unquote
from typing import Union

db = ReSql()

async def banner(user_id:int, size:int=1024):
  sizes = [64, 128, 256, 512, 1024, 2048]
  if not size in sizes:
    return "Invalid size. Valid sizes: 64, 128, 256, 512, 1024, 2048"
  async with aiohttp.ClientSession() as cs:
    async with cs.get(f"https://api.popcat.xyz/banners/{user_id}") as r:
      data = await r.json()
    res = data['banner'].replace("?size=1024", "")
    if res == "None":
      return res
    else:
      return f"{res}?size={size}"

def enlarge(emote, size:int=None):
  id = emote.split(":")[2].split(">")[0]
  sizes = [64, 128, 256, 512, 1024, 2048]
  url = f"https://cdn.discordapp.com/emojis/{id}.png?size={size}"
  if (size is None):
    return f"https://cdn.discordapp.com/emojis/{id}.png"
  if (emote.startswith("<a")):
    url = url.replace("png", "gif")
  if not (size in sizes):
    return("Invalid size. Valid sizes: 64, 128, 256, 512, 1024, 2048")
  return url
  

async def getNSFW(endpoint:str):
  key = os.getenv("key")
  try:
    async with aiohttp.ClientSession() as cs:
      async with cs.get(f"https://api.gofaizen.repl.co/nsfw/{endpoint}?key={key}") as r:
        data = await r.json()
        return data['url']
  except Exception as e:
    raise e

def writeFile(src:str,content:any):
  """Writes {content} in the file passed in {src}. If {src} doesn't exist, it makes the file"""
  try:
    with open(src,"w") as deeznuts:
      deeznuts.write(content)
  except FileNotFoundError:
    return (f"No such file or directory: '{src}'")


def createFile(name:str):
  """Creates the file with {name}."""
  with open(name,"w") as deeznuts:
    deeznuts.write("")

def readFile(src:str):
  """Reads the contents of the given file"""
  try:
    with open(src,"r") as deeznuts:
      return deeznuts.read()
  except FileNotFoundError:
    return (f"No such file or directory: '{src}'")
  except discord.errors.HTTPException:
    return ("The file does not have any content to read")

def replaceText(text,text_to_replace,new_text):
  return str(text).replace(str(text_to_replace), str(new_text))

def randomText(*choices):
  return rand.choice(str(choices))

def random(min, max):
  return np.random.randint(min, max)


async def jsonRequest(url, property=None):
  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = await r.json()
      if property==None:
        return dict(data)
      else:
        return data[property]

def textSplit(string:str, separator:str):
  try:
    muhlist = string.split(separator)
    db.insert("split", [each.strip() for each in muhlist])
  except:
    db.insert("split",None)
def splitText(index:int):
  try:
    index -= 1
    return db.get("split")[index]
  except KeyError:
    return
  finally:
    db.insert("split",[])

def joinSplitText(separator:str):
  return separator.join(db.get("split"))

def getTextSplitLength():
  try:
    return len(db.get("split"))
  finally:
    db.insert("split",[])

def url(method:str, string:str):
  if (method == "encode"): return quote(string)
  if (method == "decode"): return unquote(string)

encodeURIComponent = lambda string: quote(string) 
decodeURIComponent = lambda string: unquote(string) 

def isNaN(text):
  key = os.environ["key"]
  r = requests.get(f"https://api.gofaizen.repl.co/misc/isnan?num={text}&key={key}")
  data = r.json()
  return bool(data["isNaN"])

async def help_embed(ctx:commands.Context,command:str,example,usage,description,cooldown:int="None",aliases:str="None"):
    embed = discord.Embed(description=f"""**Description:** {description} \n**Cooldown:** {cooldown} \n**Usage:** `{usage}` \n**Aliases:** {aliases} \n**Example:** \n{example}""", color=ctx.author.color).set_author(name=f"Command: py!{command}", icon_url=ctx.author.avatar_url).set_footer(text="<> = Argument required | [] = Argument optional")
    await ctx.send(embed=embed)

def clean_code(content):
    if content.startswith("```") and content.endswith("```"):
        return "\n".join(content.split("\n")[1:])[:-3]
    else:
        return content

def display_stdout(content):
  from prettyprinter import pprint
  import io, contextlib
  stdout = io.StringIO()
  with contextlib.redirect_stdout(stdout):
    pprint(content)
    return stdout.getvalue()
  pprint(content)

def status_code(url: str):
  import requests
  return requests.get(url.strip()).status_code

async def color_test(ctx,color: Union[int,discord.colour.Color],filler_text: str=config.lispum):
  embed = discord.Embed(
    description=filler_text,
    color=color
  )
  await ctx.reply(embed=embed)


def user_avatar(ctx,user: Union[int,discord.User] = "png", size=None):
    sizes = [64, 128, 256, 512, 1024, 2048]
    if not (size in sizes):
        raise ValueError(f'bad argument: "{size}". Must be {", ".join(sizes)}')
    