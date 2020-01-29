import discord
from discord.ext import commands
import random

class Vip(commands.Cog, name="Vip"):
    def __init__(self, client):
        self.client = client

    # make vip commands
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def give_vip(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send("choose someone to get vip.")
            return
        role = discord.utils.get(ctx.guild.roles, name="vip")
        await member.add_roles(role)
        await ctx.send(f"{member.mention} you have vip now!")
        return

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def remove_vip(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send("choose who has to get vip removed")
            return
        role = discord.utils.get(ctx.guild.roles, name="vip")
        await member.remove_roles(role)
        await ctx.send(f"{member.mention} you dont have vip any more.")

    # vip only commands
    @commands.command()
    @commands.has_role("vip")
    @commands.bot_has_permissions(manage_roles=True)
    async def color(self, ctx, color):
        colors = ["red", "orange", "yellow", "green", "blue", "pink", "purple"]
        if color in colors:
            roles = [discord.utils.get(ctx.guild.roles, name=colors[0]), discord.utils.get(ctx.guild.roles, name=colors[1]),
                     discord.utils.get(ctx.guild.roles, name=colors[2]), discord.utils.get(ctx.guild.roles, name=colors[3]),
                     discord.utils.get(ctx.guild.roles, name=colors[4]), discord.utils.get(ctx.guild.roles, name=colors[5]),
                     discord.utils.get(ctx.guild.roles, name=colors[6])]
            await ctx.author.remove_roles(roles[0], roles[1], roles[2], roles[3], roles[4], roles[5], roles[6])
            role = discord.utils.get(ctx.guild.roles, name=color)
            await ctx.author.add_roles(role)
            await ctx.send(f"you now have the color {color}")
        elif color == "default":
            roles = [discord.utils.get(ctx.guild.roles, name=colors[0]),
                     discord.utils.get(ctx.guild.roles, name=colors[1]),
                     discord.utils.get(ctx.guild.roles, name=colors[2]),
                     discord.utils.get(ctx.guild.roles, name=colors[3]),
                     discord.utils.get(ctx.guild.roles, name=colors[4]),
                     discord.utils.get(ctx.guild.roles, name=colors[5]),
                     discord.utils.get(ctx.guild.roles, name=colors[6])]
            await ctx.author.remove_roles(roles[0], roles[1], roles[2], roles[3], roles[4], roles[5], roles[6])
            await ctx.send("you do not have a special color any more")
        else:
            await ctx.send("pick a color from .colors")

    @commands.command()
    @commands.has_role("vip")
    async def colors(self, ctx):
        colors = ["red", "orange", "yellow", "green", "blue", "pink", "purple"]
        embed = discord.Embed(title="Colors", colour=discord.Colour.dark_purple())
        desc =  f"{colors[0]}\n"
        desc += f"{colors[1]}        \n"
        desc += f"{colors[2]}         \n"
        desc += f"{colors[3]}         \n"
        desc += f"{colors[4]}         \n"
        desc += f"{colors[5]}           \n"
        desc += f"{colors[6]}         \n"
        embed.description = desc
        await ctx.send(content=None, embed=embed)


    @commands.command()
    @commands.has_role("vip")
    async def namechange(self, ctx):
        name = ["potato man", "billyapi", "cupcake destroyer", "boogey man", "reaper of cheese", "billy54", "german guy", "simonelo", "cyber truck guy", "eagelxx", "zombieslayer",
                "fridge opener48", "pope69", "obama"]
        await ctx.author.edit(nick=random.choice(name))
        await ctx.send(f"your name is now {name}")


    @commands.command()
    @commands.has_role("vip")
    async def resetname(self, ctx):
        await ctx.author.edit(nick=ctx.author)


def setup(client):
    client.add_cog(Vip(client))