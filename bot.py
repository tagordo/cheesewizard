import discord
from discord.ext import commands
import os

# https://discordapp.com/api/oauth2/authorize?client_id=670749597697703947&permissions=8&scope=bot
client = commands.Bot(command_prefix=".")
client.remove_command("help")


@client.event
async def on_ready():
    print("bot is ready")

@client.event
async def on_member_join(member):
    id = client.get_guild(665280882025693220)
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send(f"{member.mention} joined the server there are now {id.member_count} in the server")

@client.command()
async def botinfo(ctx):
    ping = int(round(client.latency * 1000, 1))
    embed = discord.Embed(title="server info", colour=discord.Colour.dark_purple())
    desc = f"bot maker: BOT_tagordo#1926\n"
    desc += f"bot version: 1.0.0\n"
    desc += f"ping: {ping}ms\n"
    desc += f"commands: gebruik .help\n"
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.description = desc
    await ctx.send(content=None, embed=embed)


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run("# token here")
