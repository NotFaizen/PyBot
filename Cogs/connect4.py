from discord.ext import commands
import discord
import requests

def create_board():
    r = requests.post("https://resapi.up.railway.app/game/connect-4/create",json={
        "player1":"🔴",
        "player2":"🟡",
        "empty":"⚪"
    })
    r = r.json()
    return r["game_id"]

def get_board(game_id):
    r = requests.post(
    url="https://resapi.up.railway.app/game/connect-4/get-board",
    json={
        "game_id":game_id
    })
    r = r.json()
    return r["board"]

def drop(game_id,col,player):
    r = requests.post(
    url="https://resapi.up.railway.app/game/connect-4/drop",
    json={
        "game_id":game_id,
        "column":col,
        "player":player
    })
    r = r.json()
    return r
    

def numberChecker(emoji):
    if emoji == "1️⃣":
        return 0
    elif emoji == "2️⃣":
        return 1
    elif emoji == "3️⃣":
        return 2
    elif emoji == "4️⃣":
        return 3
    elif emoji == "5️⃣":
        return 4
    elif emoji == "6️⃣":
        return 5
    elif emoji == "7️⃣":
        return 6
    else:
        return 0  

    
class connect4(commands.Cog):
    def __init__(self,bot):
      self.bot = bot

    @commands.command(pass_context=True)
    async def startgame(self, ctx,who:discord.Member=None):
        def check1(reaction, user1):
            return user1 == ctx.author and str(reaction.emoji) in ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣"]
        def check2(reaction, user1):
            return user1 == who and str(reaction.emoji) in ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣"]

        # create game id to manage da game
        board = {}
        board["game_id"] = create_board()
        board["player1"] = ctx.author.id
        board["player2"] = who.id
        print(board)
        embed = discord.Embed(title=f"{ctx.author.name} turn")
        embed.description = get_board(board["game_id"])
        MainMsg = await ctx.send(embed = embed)
        await MainMsg.add_reaction("1️⃣")
        await MainMsg.add_reaction("2️⃣")
        await MainMsg.add_reaction("3️⃣")
        await MainMsg.add_reaction("4️⃣")
        await MainMsg.add_reaction("5️⃣")
        await MainMsg.add_reaction("6️⃣")
        await MainMsg.add_reaction("7️⃣")
        game_over = False
        turn = 0

        while not game_over:
            if turn == 0:
                embed.title = f"{ctx.author.name} 's turn "
                reaction, user1 = await self.bot.wait_for('reaction_add', check=check1)
                col = int(numberChecker(str(reaction.emoji)))
                winner = drop(board["game_id"],col,1)
                if winner["winner"] != "none":
                    return await ctx.send("player1 won")
            else:
                embed.title = f"{who.name} 's turn "
                reaction, user1 = await self.bot.wait_for('reaction_add', check=check2)
                col = int(numberChecker(str(reaction.emoji)))
                winner = drop(board["game_id"],col,2)
                if winner["winner"] != "none":
                    await ctx.send("player2 won")

            embed.description = winner["board"]
            await MainMsg.edit(embed=embed)
            turn += 1
            turn = turn % 2     
        
def setup(bot):
  bot.add_cog(connect4(bot))