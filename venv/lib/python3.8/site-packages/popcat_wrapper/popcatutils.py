from aiohttp import ClientSession
def replaced(msg:str):
  return msg.replace(" ", "+")

def pngImage(URL:str):
  x = URL.replace("webp?size=2048","png").replace("gif?size=2048","png").replace("webp?size=4069","png").replace("png?size=4069","png").replace("png?size=2048", "png").replace("webp","png").replace("jpg","png").replace("gif","png")

  return x
  
async def request(url:str):
  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = await r.json()
      return data

def isURL(url:str):
  res = request(f"https://api.popcat.xyz/is-url?url={url}")
  return res['isurl']






























































def secretmsg():
  return "If you're getting this message, that means you have found the easter egg / secret; you are cool, believe it! (DM NotFaizen#3463 with screenshot proof for a cookie)"