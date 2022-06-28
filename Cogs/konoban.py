from discord.ext import commands
import discord
import requests

def create_board(level):
    r = requests.post("https://resapi.up.railway.app/game/sokoban/create",json={
        "level":level
    })
    r = r.json()
    return r

def drop(game_id,action):
    r = requests.post(
    url="https://resapi.up.railway.app/game/sokoban/action",
    json={
        "game_id":game_id,
        "action":action
    })
    r = r.json()
    return r
    

def numberChecker(emoji):
    if emoji == "⬅️":
        return "left"
    elif emoji == "➡️":
        return "right"
    elif emoji == "⬆️":
        return "up"
    elif emoji == "⬇️":
        return "down"
    else:
        return None

    
class KonoBan(commands.Cog):
    def __init__(self,bot):
      self.bot = bot

    @commands.command(pass_context=True)
    async def sokoban(self, ctx, level:str):
        def check1(reaction, user1):
            return user1 == ctx.author and str(reaction.emoji) in ["⬅️","➡️","⬆️","⬇️"]

        # create game id to manage da game
        board = create_board(level)
        embed = discord.Embed(title="konoban game!")
        embed.description = board["board"]
        MainMsg = await ctx.send(embed = embed)
        await MainMsg.add_reaction("➡️")
        await MainMsg.add_reaction("⬆️")
        await MainMsg.add_reaction("⬇️")
        await MainMsg.add_reaction("⬅️")
        game_over = False
        while not game_over:
            reaction, user1 = await self.bot.wait_for('reaction_add', check=check1)
            action = numberChecker(str(reaction.emoji))
            winner = drop(board["game_id"],action)
            if winner["win"] == "True":
                game_over = True
                embed.description = "Game Over!"
                await MainMsg.edit(embed=embed)
                return

            embed.description = winner["board"]
            await MainMsg.edit(embed=embed)
        
def setup(bot):
  bot.add_cog(KonoBan(bot))