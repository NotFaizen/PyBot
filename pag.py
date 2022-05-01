import discord,asyncio,requests
from discord.ext import buttons
from util import encodeURIComponent
quote = lambda x: x.replace(" ", "+")

class Pag(buttons.Paginator):
    async def teardown(self):
        try:
            await self.page.clear_reactions()
        except discord.HTTPException:
            pass

def writer(url,name):
  exts = [".png",".jpg",".webp",".gif",".jpeg",".mp4"]
  your_mother = tuple((ext for ext in exts))
  if not (name.endswith(your_mother)):
    return;
  with open(f"dumb_shit/{name}","wb") as file:
      r = requests.get(url)
      file.write(r.content)
      file.close()
class WelcomeCard:
  def __init__(self,*,text_1:str,text_2:str,text_3:str):
    self.text_1 = text_1
    self.text_2 = text_2
    self.text_3 = text_3
    self.baseurl = f"https://api.popcat.xyz/welcomecard?text1={quote(self.text_1)}&text2={quote(self.text_2)}&text3={quote(self.text_3)}"
  def set_background(self,*,image: str):
    self.baseurl += f"&background={image}"
    return self
  def set_avatar(self,*,image: str):
    self.baseurl += f"&avatar={image}"
    return self
  def set_color(self,*,color: str=None):
    if (color is None):
      pass
    self.baseurl += f"&color={color}"
    return self
  def deploy(self):
    return self.baseurl
    return self


async def GetMessage(
    bot, ctx, contentOne="Default Message", contentTwo="\uFEFF", timeout=100
):
    """
    This function sends an embed containing the params and then waits for a message to return
    Params:
     - bot (commands.Bot object) :
     - ctx (context object) : Used for sending msgs n stuff
     - Optional Params:
        - contentOne (string) : Embed title
        - contentTwo (string) : Embed description
        - timeout (int) : Timeout for wait_for
    Returns:
     - msg.content (string) : If a message is detected, the content will be returned
    or
     - False (bool) : If a timeout occurs
    """
    embed = discord.Embed(title=f"{contentOne}", description=f"{contentTwo}",color=ctx.author.color)
    sent = await ctx.send(embed=embed)
    try:
        msg = await bot.wait_for(
            "message",
            timeout=timeout,
            check=lambda message: message.author == ctx.author
            and message.channel == ctx.channel,
        )
        if msg:
            return msg.content
    except asyncio.TimeoutError:
        return await sent.edit(content="Message timed out")


