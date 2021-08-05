import discord
from discord.ext import commands

description = '''A bot to show CurseForge uploads for Momo Studios'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

activity = discord.Activity(name='Watching Sam fix me up', type=discord.ActivityType.watching)
client = discord.Client(activity=activity)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

extensions = ['cogs.CurseCommands']

if __name__ == "__main__":
    for ext in extensions:
        bot.load_extension(ext)


bot.run('ODY4MzkyMjQyNzMyMjA0MDMy.YPu_TA.Nie_bBnXxsnwM4VFYx90fEpVEE8')
