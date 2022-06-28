from discord.ext import commands
import discord
import requests

def create_board():
    r = requests.post("https://resapi.up.railway.app/game/tetris/create")
    r = r.json()
    return r

def action(game_id,action):
    r = requests.post(
    url="https://resapi.up.railway.app/game/tetris/action",
    json={
        "game_id":game_id,
        "action":action
    })
    r = r.json()
    return r


def numberChecker(emoji):
    if emoji == "⬇️": # soft drop
        return "soft_drop"
    elif emoji == "⏬": # hard drop
        return "hard_drop"
    elif emoji == "⬅️": # left
        return "left"
    elif emoji == "➡️": # right
        return "right"
    elif emoji == "🔄": # rotate
        return "rotate"
    elif emoji == "6️⃣": # swap
        return "swap"
    elif emoji == "7️⃣": # hold
        return "hold"
    else:
        return "tf"


def next_piece(piece):
    if piece == "I":
        return "https://cdn.discordapp.com/attachments/907213435358547968/984052010661859328/unknown.png"
    elif piece == "J":
        return "https://cdn.discordapp.com/attachments/907213435358547968/984052028634456084/unknown.png"

    elif piece == "L":
        return "https://cdn.discordapp.com/attachments/907213435358547968/984052046535720980/unknown.png"
    elif piece == "O":
        return "https://media.discordapp.net/attachments/907213435358547968/984052068539047957/unknown.png"
    elif piece == "S":
        return "https://media.discordapp.net/attachments/907213435358547968/984052088583626762/unknown.png"
    elif piece == "T":
        return "https://media.discordapp.net/attachments/907213435358547968/984052106338115644/unknown.png"
    elif piece == "Z":
        return "https://media.discordapp.net/attachments/907213435358547968/984052124235231262/unknown.png"

    
class tetris(commands.Cog):
    def __init__(self,bot):
      self.bot = bot

    @commands.command(pass_context=True)
    async def tetrisgame(self, ctx):
        def check1(reaction, user1):
            return user1 == ctx.author and str(reaction.emoji) in ["⬇️","⏬","⬅️","➡️","🔄","6️⃣","7️⃣"]

        # create game id to manage da game
        board = {}
        a = create_board()
        board["gameid"] = a["game_id"]
        board["gameboard"] = a["board"]
        board["score"] = 0
        
        
        embed = discord.Embed(title="tetris game")
        embed.description = board["gameboard"]
        embed.set_thumbnail(url=next_piece(a["next"]))
        MainMsg = await ctx.send(embed = embed)
        await MainMsg.add_reaction("⬇️")
        await MainMsg.add_reaction("⏬")
        await MainMsg.add_reaction("⬅️")
        await MainMsg.add_reaction("➡️")
        await MainMsg.add_reaction("🔄")
        await MainMsg.add_reaction("6️⃣")
        await MainMsg.add_reaction("7️⃣")
        playi = True
        turn = 0

        while playi:
            reaction, user1 = await self.bot.wait_for('reaction_add', check=check1)
            action1 = numberChecker(str(reaction.emoji))
            a = action(board["gameid"],action1)
            board["playing"] = a["playing"]
            board["gameboard"] = a["board"]
            board["score"] = a["score"]
            playi = board["playing"]
            embed.set_thumbnail(url=next_piece(a["next"]))
            embed.description = board["gameboard"]
            embed.set_footer(text="score: " + str(board["score"]))
            await MainMsg.edit(embed=embed)
        
def setup(bot):
  bot.add_cog(tetris(bot))