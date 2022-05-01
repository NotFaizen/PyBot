from . import popcatutils
from aiohttp import ClientSession
base_url = "https://api.popcat.xyz/"
base = "https://api.popcat.xyz/" 
# /country endpoint 
async def country(name:str, property=None):
  async with ClientSession() as cs:
    async with cs.get(f"https://api.popcat.xyz/countries/{name}") as r:
      data = await r.json()

  """Gives info on the provided country. The name field is the country name and the property field is which attribute of the country you want (eg: currency, flag, etc)

  properties: name, domain, calling_codes, capital, region, population, area, flag, currency.name, currency.short, currency.symbol"""
  if property == None:
    return data
  elif property == "currency.name":
    return data['currency']['name']
  elif property == "currency.symbol":
    return data['currency']['symbol']
  elif property == "currency.short":
    return data['currency']['short']
  else:
    return data[f'{property}']

# /banner endpoint
async def banner(ID:int):
  async with ClientSession() as cs:
    async with cs.get(f"https://api.popcat.xyz/banners/{ID}") as r:
      data = await r.json()
      return data['banner']

# /npm endpoint
async def npm(name:str,property=None):
  """Returns info on any package registered on npmjs.org. The name field is the name of the package you want info about

  properties: name, version, description, keywords, author, author_email, last_published, maintainers, repository, downloads_this_year"""
  async with ClientSession() as cs:
    async with cs.get(f"https://api.popcat.xyz/npm?q={name}") as r:
      data = await r.json()
      if property == None:
        return data
      else:
        return data[property]

# /fact endpoint
async def randomfact():
  async with ClientSession() as cs:
    async with cs.get(f"https://api.popcat.xyz/fact") as r:
      data = await r.json()
      return data['fact']
  
# /instagram endpoint
async def instagramUser(user:str, property=None):
  async with ClientSession() as cs:
    async with cs.get(f"https://api.popcat.xyz/instagram?user={user}") as r:
      data = await r.json
      if property == None:
        return data
      else:
        return data[property]

# /drake endpoint
async def drake(text1:str, text2:str):
	# local vars
	x = text1.replace(" ", "+")
	y = text2.replace(" ", "+")
	url = f"https://api.popcat.xyz/drake?text1={x}&text2={y}"

	# not local vars?
	return url

# /pooh endpoint
async def pooh(text1:str,text2:str):
	# local vars i suppose?
	x = text1.replace(" ", "+")
	y = text2.replace(" ", "+")
	url = f"https://api.popcat.xyz/pooh?text1={x}&text2={y}"

	# EZ Clap copy pasta :OMEGALUL:
	return url

# /ship endpoint
async def ship(user1:str,user2:str):
	# not local vars lol
	x = user1.replace("webp?size=2048","png").replace("gif?size=2048","png").replace("webp?size=4069","png").replace("png?size=4069","png")
	y = user2.replace("webp?size=2048","png").replace("gif?size=2048","png").replace("webp?size=4069","png").replace("png?size=4069","png")
	url = f"https://api.popcat.xyz/ship?user1={x}&user2={y}"

	return url

# /colorify endpoint
async def colorify(image:str, color:str):
	x = image.replace("webp?size=2048","png").replace("gif?size=2048","png").replace("webp?size=4069","png").replace("png?size=4069","png")
	url = f"https://api.popcat.xyz/colorify?image={x}&color={color}"

	return url

# /biden endpoint
async def biden(text:str):
	x = text.replace(" ", "+")
	url = f"https://api.popcat.xyz/biden?text={x}"

	return url

# /joke endpoint
async def joke():
  async with ClientSession() as cs:
    async with cs.get(f"https://api.popcat.xyz/joke") as r:
      data = await r.json()
      return data['joke']

# /pikachu endpoint
async def pikachu(text:str):
	x = text.replace(" ", "+")
	url = f"https://api.popcat.xyz/pikachu?text={x}"

	return url

# /drip endpoint
async def drip(image:str):
	x = image.replace("webp?size=2048","png").replace("gif?size=2048","png").replace("webp?size=4069","png").replace("png?size=4069","png")
	url = f"https://api.popcat.xyz/drip?image={x}"

	return url

async def clown(image:str):
	x = image.replace("webp?size=2048","png").replace("gif?size=2048","png").replace("webp?size=4069","png").replace("png?size=4069","png")
	url = f"https://api.popcat.xyz/drip?image={x}"

	return url

async def mock(text:str):
  msg = popcatutils.replaced(text)
  async with ClientSession() as cs:
    async with cs.get(f"https://api.popcat.xyz/mock?text={msg}") as r:
      data = await r.json()
      return data['text']

async def translate(text:str, language):
  y = text.replace(" ", "+")
  async with ClientSession as cs:
    async with cs.get(f"https://api.popcat.xyz/translate?text={y}&to={language}") as r:
      data = r.json()
      return data['translated']

async def reverse(text:str):
  text = popcatutils.replaced(text)
  async with ClientSession() as cs:
    async with cs.get(f"https://api.popcat.xyz/reverse?text={text}") as r:
      data = r.json()
      return data['text']

async def uncover(image:str):
  image = popcatutils.pngImage(image)
  url = f"{base_url}uncover?image={image}"
  return url

async def ad(image:str):
  image = popcatutils.pngImage(image)
  url = f"{base_url}ad?image={image}"
  return url
  
async def blur(image:str):
  image = popcatutils.pngImage(image)
  url = f"{base_url}blur?image={image}"
  return url

async def invert(image:str):
  image = popcatutils.pngImage(image)
  url = f"{base_url}invert?image={image}"
  return url

async def greyscale(image:str):
  image = popcatutils.pngImage(image)
  url = f"{base_url}grayscale?image={image}"
  return url

async def alert(text:str):
  # text = popcatutils.replaced(text)
  # url = f"{base_url}alert?text={text}"
  return "Deprecated until further notice"

async def caution(text:str):
  text = popcatutils.replaced(text)
  url = f"{base_url}caution?text={text}"
  return url

async def colorinfo(color,property=None):
  async with ClientSession() as cs:
    async with cs.get(f"https://api.popcat.xyz/color/{color}") as r:
      data = await r.json()
      if property == None:
        return data
      else:
        return data[property]

async def jokeoverhead(image:str):
  image = popcatutils.pngImage(image)
  url = f"{base_url}jokeoverhead?image={image}"
  return url

async def mnm(image:str):
  image = popcatutils.pngImage(image)
  url = f"{base_url}mnm?image={image}"
  return url

async def doublestruck(text:str):
  text = popcatutils.replaced(text)
  url = f"{base_url}doublestruck?text={text}"
  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = await r.json()
      return data['text']

async def texttomorse(text:str):
  text = popcatutils.replaced(text)
  url = f"{base_url}texttomorse?text={text}"
  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = r.json()
      return data['morse']

async def wouldyourather(property=None):
  url = f"{base_url}wyr"
  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = r.json()
      if property == None:
        return data
      else:
        return data[property]

async def randommeme(property=None):
  url = f"{base_url}meme"
  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = r.json()
      if property == None:
        return data
      else:
        return data[property]

async def itunes(song:str, property=None):
  song = popcatutils.replaced(song)
  url = f"{base_url}itunes?song={song}"
  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = r.json()
      if property == None:
        return data
      else:
        return data[property]

async def playstore(app:str, property=None):
  app = popcatutils.replaced(app)
  url = f"{base_url}playstore?q={app}"
  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = r.json()
      if property == None:
        return data
      else:
        return data[property]

async def binary_encode(text:str):
  text = popcatutils.replaced(text)
  url = f"{base_url}encode?text={text}"
  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = r.json()
      return data['binary']

async def binary_decode(binary):
  binary = popcatutils.replaced(binary)
  url = f"{base_url}decode?binary={binary}"
  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = r.json()
      return data['text']

async def facts(text:str):
  text = popcatutils.replaced(text)
  url = f"{base_url}facts?text={text}"
  return url

async def _8ball():
  async with ClientSession as cs:
    async with cs.get(f"{base_url}8ball") as r:
      data = await r.json()
      return data['answer']

async def welcomecard(background:str, text1:str, text2:str, text3:str, avatar:str):
  text1 = popcatutils.replaced(text1)
  text2 = popcatutils.replaced(text2)
  text3 = popcatutils.replaced(text3)
  avatar = popcatutils.pngImage(avatar)

  url = f"{base_url}welcomecard?background={background}&text1={text1}&text2={text2}&text3={text3}&avatar={avatar}"

  return url

async def sadcat(text:str):
  text = popcatutils.replaced(text)
  url = f"{base_url}sadcat?text={text}"

  return url

async def oogway(text:str):
  text = popcatutils.replaced(text)
  url = f"{base_url}oogway?text={text}"
  return url

async def communism(image:str):
  image = popcatutils.pngImage(image)
  url = f"{base_url}communism?image={image}"

  return url

async def car(property=None):
  url = f"{base_url}car"

  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = await r.json()
      if property == None:
        return data
      else:
        return data[property]

async def showerthoughts():
  url = f"{base}showerthoughts" 
  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = await r.json()
      return data['result']

async def quote():
  async with ClientSession() as cs:
    async with cs.get(f"{base}quote") as r:
      data = await r.json()
      return data['quote']

async def lyrics(song:str, property=None):
  song = popcatutils.replaced(song)

  async with ClientSession() as cs:
    async with cs.get(f"{base}lyrics?song={song}") as r:
      data = r.json()
    if property == None:
      return data
    else:
      return data[property]

async def subreddit(name:str, property=None):
  url = f"{base}subreddit/{name}"
  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = await r.json()
      
      if property == None: 
        return data
      else: 
        return data[property]


async def wanted(image:str):
  image = popcatutils.pngImage(image)
  url = f"{base}wanted?image={image}"
  
  return url

async def gunOverlay(image:str):
  base_url = "https://api.popcat.xyz/gun?image="
  pngIMG = popcatutils.pngImage(image)
  return base_url+pngIMG

async def simp(image:str):
  base_url = "https://api.popcat.xyz/simpstamp?image="
  pngIMG = popcatutils.pngImage(image)
  return base_url+pngIMG

async def lulcat(text:str):
  base_url = "https://api.popcat.xyz/lulcat?text="+text
  a = ClientSession()
  resp = await a.get(base_url)
  jsonresponse = await resp.json()["text"]
  return jsonresponse

async def weather(location:str, property=None):
  base_url = "https://api.popcat.xyz/weather?q="+location
  a = ClientSession()
  resp = await a.get(base_url)
  jsonresponse = await resp.json()
  if property == None:
    return jsonresponse
  else:
    return jsonresponse[property]
  
async def opinion(image:str, text:str):
  image = popcatutils.pngImage(image)
  text = popcatutils.replaced(text)
  url = f"{base}opinion?image={image}&text={text}"
  return url

async def pet(image:str)->str:
  img = popcatutils.pngImage(image)
  return f"https://api.popcat.xyz/pet?image={img}"

async def url_shortner(url:str,extension:str) -> str:
  if popcatutils.isURL(url) == False:
    return "url_shortener(): Invalid URL provided" 
  base_url = f"{base}shorten?url={url}&extension={extension}"
  client = ClientSession()
  resp = await client.get(base_url)
  resp = await resp.json()
  return resp["shortened"]

async def screenshot(url:str)->str:
  if popcatutils.isURL(url) == False:
    return "screenshot(): Invalid URL provided"
  return f"https://api.popcat.xyz/screenshot?url={url}"


async def github(user:str, property=None) -> dict:
  base_url = f"https://api.popcat.xyz/github/{user}"
  client = ClientSession()
  resp = await client.get(base_url)
  resp = await resp.json()
  if property == None:
    return resp
  else:
    return resp[property]

async def whowouldwin(image1:str,image2:str):
  image1 = popcatutils.pngImage(image1)
  image2 = popcatutils.pngImage(image2)
  return f"https://api.popcat.xyz/whowouldwin?image2={image2}&image1={image1}"
