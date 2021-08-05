import discord
from curseforge.models.addon import Addon
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import curseforge

mc = curseforge.Minecraft()
coldsweat = mc.get_addon(506194)
momosorigins = mc.get_addon(506528)


class curseCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def updatecs(self, ctx, channel_id:discord.TextChannel, changelog):
        embed = discord.Embed(name="Cold Sweat Update", title="New Cold Sweat Update -", description=changelog,
                              color=discord.Color.dark_blue())
        embed.add_field(name="Download -", value=f"[Curseforge]( {coldsweat.url} ) \n [Direct Download]( {coldsweat.latest_file.url} )")
        embed.set_image(url="https://images-ext-2.discordapp.net/external/7BKmy33btox9TETWZHfK0lAPYIujTSoukn2XC0_sUtE/https/i.imgur.com/8MQNLqv.png")
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/llIsKheAP9uNSeMM7ZrCRObKdQWZU8sVfmQdCqYK2ZQ/https/i.imgur.com/VQSPSgv.png")
        await channel_id.send(embed=embed)

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def updatemo(self, ctx, channel_id: discord.TextChannel, changelog):
        embed = discord.Embed(name="Momos Survival Origins Update", title="Momo's Survival Origins Update -", description=changelog,
                              color=discord.Color.dark_grey())
        embed.add_field(name="Download -",
                        value=f"[Curseforge]( {momosorigins.url} ) \n [Direct Download]( {momosorigins.latest_file.url} )")
        embed.set_thumbnail(
            url="https://media.forgecdn.net/avatars/409/4/637623458258575897.png")
        await channel_id.send(embed=embed)

def setup(bot):
    bot.add_cog(curseCommands(bot))
