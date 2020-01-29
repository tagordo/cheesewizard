import discord
from discord.ext import commands
import random
import requests
import json
import aiohttp


class Fun(commands.Cog, name="Fun"):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def inspiration(self, ctx):
        quote = ["Failure will never overtake me if my determination to succeed is strong enough.Failure will never overtake me if my determination to succeed is strong enough.",
                 "Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence.",
                 "The secret of getting ahead is getting started.", "Never bend your head. Always hold it high. Look the world straight in the eye.",
                 "What you get by achieving your goals is not as important as what you become by achieving your goals.",
                 "Believe you can and you're halfway there.", "No matter what you're going through, there's a light at the end of the tunnel.",
                 "Life is like riding a bicycle. To keep your balance, you must keep moving.", "You are never too old to set another goal or to dream a new dream.",
                 "The most wasted of days is one without laughter.", "You must do the things you think you cannot do.",
                 "Stay close to anything that makes you glad you are alive.", "Happiness is not by chance, but by choice."]
        await ctx.send(random.choice(quote))

    @commands.command()
    async def question(self, ctx, question):
        answer = ["yes", "no", "maybe", "ask a friend", "ask again later", "only if you want to", "sometimes"]
        image = ["https://img.buzzfeed.com/buzzfeed-static/static/2017-12/6/16/enhanced/buzzfeed-prod-fastlane-03/enhanced-360-1512596118-1.png",
                 "https://cadiznoticias.es/wp-content/uploads/2016/10/no.jpg",
                 "https://www.radiorucphen.nl/wp-content/uploads/maybe.jpg",
                 "https://cdn.clipart.email/3c8fbbf0c80a4fcd915d95bfbd29381b_ask-a-friend-clipart-clipartxtras_638-359.jpeg",
                 "https://cdn.dribbble.com/users/303999/screenshots/2391010/ask_again_later_800x600_1x.jpg",
                 "https://cdn.discordapp.com/attachments/665281612384043020/670815758464450571/Naamloos.png",
                 "https://static1.squarespace.com/static/54185496e4b0bec2d7f1935b/t/5a7b4c3624a69401d179e116/1574797748623/?format=1500w"]
        pickanswer = random.choice(answer)
        embed = discord.Embed(title=pickanswer, colour=discord.Colour.dark_purple())
        if pickanswer == "yes":
            embed.set_image(url=image[0])
        elif pickanswer == "no":
            embed.set_image(url=image[1])
        elif pickanswer == "maybe":
            embed.set_image(url=image[2])
        elif pickanswer == "ask a friend":
            embed.set_image(url=image[3])
        elif pickanswer == "ask again later":
            embed.set_image(url=image[4])
        elif pickanswer == "only if you want to":
            embed.set_image(url=image[5])
        else:
            embed.set_image(url=image[6])
        await ctx.send(content=None, embed=embed)

    @commands.command()
    async def youtube(self, ctx, search=None):
        if not search:
            await ctx.send("what are you searcher for?")
        await ctx.send(f"https://www.youtube.com/results?search_query={search}")

    @commands.command()
    async def randomcolor(self, ctx):
        hex1 = ["A", "B", "C", "D", "E", "F", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        hex2 = ["A", "B", "C", "D", "E", "F", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        hex3 = ["A", "B", "C", "D", "E", "F", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        hex4 = ["A", "B", "C", "D", "E", "F", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        hex5 = ["A", "B", "C", "D", "E", "F", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        hex6 = ["A", "B", "C", "D", "E", "F", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        hex1 = random.choice(hex1)
        hex2 = random.choice(hex2)
        hex3 = random.choice(hex3)
        hex4 = random.choice(hex4)
        hex5 = random.choice(hex5)
        hex6 = random.choice(hex6)
        await ctx.send(f"https://www.colorcombos.com/images/colors/{hex1}{hex2}{hex3}{hex4}{hex5}{hex6}.png")
        await ctx.send(f"hexcolor is {hex1}{hex2}{hex3}{hex4}{hex5}{hex6}")

    @commands.command()
    async def slots(self, ctx):
        slot1 = ["🍎", "🍊", "🍐", "🍋", "🍉", "🍇", "🍓", "🍒"]
        slot2 = ["🍎", "🍊", "🍐", "🍋", "🍉", "🍇", "🍓", "🍒"]
        slot3 = ["🍎", "🍊", "🍐", "🍋", "🍉", "🍇", "🍓", "🍒"]
        slot1 = random.choice(slot1)
        slot2 = random.choice(slot2)
        slot3 = random.choice(slot3)
        await ctx.send(f"{slot1}{slot2}{slot3}")
        if slot1 == slot2 == slot3:
            await ctx.send(f"all matching you win {ctx.author.mention}")

        if slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
            await ctx.send(f"2 matching you win! {ctx.author.mention}")
        else:
            await ctx.send("sorry you did not win.")

    @commands.command()
    async def cat(self, ctx):
        def catpic():
            r = requests.get(url="https://api.thecatapi.com/v1/images/search")
            website = r.text
            if len(website) >= 300:
                catpic()
                return
            pos1 = website.find("url")
            pos1 += 6
            pos2 = website.find('"', pos1)
            global cat
            cat = website[pos1:pos2]
            return
        catpic()
        embed = discord.Embed(title="kitty cat", color=discord.Colour.dark_purple())
        embed.set_image(url=cat)
        await ctx.send(embed=embed, content=None)

    @commands.command()
    async def pokedex(self, ctx, pokemon=None):
        if not pokemon:
            await ctx.send("geef een pokemon op")
            return
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://some-random-api.ml/pokedex?pokemon={pokemon}') as r:
                res = await r.json()
                print(res)
                if 'error' in res:
                    await ctx.send("unvalid pokemon")
                else:
                    embed = discord.Embed(title=res['name'], colour=discord.Colour.dark_purple())
                    desc = f"type: {res['type']}\n"
                    desc += f"nmr in pokedex: {res['id']}\n"
                    desc += f"height: {res['height']}\n"
                    desc += f"weight: {res['weight']}\n"
                    desc += f"gender: {res['gender']}\n"
                    desc += f"egg group: {res['egg_groups']}"
                    stats = f"hp: {res['stats']['hp']}\n"
                    stats += f"attack: {res['stats']['attack']}\n"
                    stats += f"defense: {res['stats']['defense']}\n"
                    stats += f"special attack: {res['stats']['sp_atk']}\n"
                    stats += f"special defense: {res['stats']['sp_def']}\n"
                    stats += f"speed: {res['stats']['speed']}\n"
                    stats += f"total: {res['stats']['total']}\n"
                    embed.set_thumbnail(url=res['sprites']['normal'])
                    embed.description = desc
                    embed.add_field(name="stats", value=stats, inline=False)
                    await ctx.send(embed=embed, content=None)

    @commands.command()
    async def binary(self, ctx, *, message):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://some-random-api.ml/binary?text={message}') as r:
                res = await r.json()
                await ctx.send(res['binary'])

    @commands.command()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/img/dog") as r:
                res = await r.json()
                embed = discord.Embed(title="doggo", colour=discord.Colour.dark_purple())
                embed.set_image(url=res['link'])
                await ctx.send(content=None, embed=embed)

def setup(client):
    client.add_cog(Fun(client))