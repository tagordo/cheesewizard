import discord
from discord.ext import commands
import time


class Moderation(commands.Cog, name="Moderation"):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def kick(self, ctx, member: discord.Member = None, reason=None):
        if not member:
            await ctx.send("who has to be kicked?")
            return
        await member.kick()
        await ctx.send(f"{member.mention} has been kicked reason= {reason}")

    @commands.command()
    @commands.has_permissions(ban_member=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, reason=None):
        if not member:
            await ctx.send("who has to be banned?")
            return
        await member.ban()
        await ctx.send(f"{member.mention} has been banned reason= {reason}")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member = None, reason=None):
        if not member:
            await ctx.send("who has to be muted?")
            return
        role = discord.utils.get(ctx.guild.roles, name="muted")
        await member.add_roles(role)
        await ctx.send(f"{member.mention} has been muted reason= {reason}")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send("who has to be unmuted?")
            return
        if discord.ext.commands.has_role("muted"):
            role = discord.utils.get(ctx.guild.roles, name="muted")
            await member.remove_roles(role)
            await ctx.send(f"{member.mention} has been unmuted")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        amount += 1
        await ctx.channel.purge(limit=amount)
        amount -= 1
        await ctx.send(f"deleted {amount} messages")
        time.sleep(3)
        await ctx.channel.purge(limit=1)

    @commands.command()
    async def help(self, ctx, *, commands=None):
        if not commands:
            embed = discord.Embed(title="Help command", colour=discord.Colour.dark_purple())
            embed.add_field(name="😄Fun commands", value="do .help Fun for help with fun commands")
            embed.add_field(name="🧰Moderation", value="do .help Moderation for help with moderation commands")
            embed.add_field(name="💎Vip", value="do .help Vip for help with vip commands")
            await ctx.send(content=None, embed=embed)
        if commands == "fun":
            embed = discord.Embed(title="Fun commands", colour=discord.Colour.dark_purple())
            embed.add_field(name="inspiration", value="give's you a inspiration quote")
            embed.add_field(name="question", value="ask a question to cheese wizard")
            embed.add_field(name="youtube", value="look something up on youtube")
            embed.add_field(name="randomcolor", value="get a random color + hex code")
            embed.add_field(name="slots", value="play a game on the slot machine")
            embed.add_field(name="cat", value="get a random cat picture")
            embed.add_field(name="pokedex", value="look a pokemon up in the pokedex")
            embed.add_field(name="binary", value="make your message in to binary")
            await ctx.send(content=None, embed=embed)
        if commands == "vip":
            embed = discord.Embed(title="vip", colour=discord.Colour.dark_purple())
            embed.add_field(name="color", value="give your self a  different color(.colors for all the colors you can do)")
            embed.add_field(name="colors", value="give's you all the all colors to use in .color")
            await ctx.send(content=None, embed=embed)
        if commands == "moderation":
            embed = discord.Embed(title="moderation", colour=discord.Colour.dark_purple())
            embed.add_field(name="kick", value="kick someone from the server")
            embed.add_field(name="ban", value="ban someone from the server")
            embed.add_field(name="mute", value="make it so that someone can't talk any more")
            embed.add_field(name="unmute", value="make it so someone can talk again if they were muted")
            embed.add_field(name="clear", value="clear a amount of messages")
            await ctx.send(content=None, embed=embed)



def setup(client):
    client.add_cog(Moderation(client))
