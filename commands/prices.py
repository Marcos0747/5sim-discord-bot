#imports
import requests, json, discord, config as CONFIG
from discord.utils import get
from discord.ext import commands, tasks
#imports

#semi-config
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=['?','!', '.'], case_insensitive=True, intents = intents)
bot.remove_command('help')
token = (CONFIG.API_TOKEN)
headers = {'Accept': 'application/json'}
params = (
    ('product', 'discord'),
    ('country', 'england'),
)
#semi-config
#code
@bot.command()

async def prices(ctx):
    
    prices = requests.get('https://5sim.net/v1/guest/prices', headers=headers, params=params).text
    prices = json.loads(prices)
    lycamobile = prices['england']['discord']['lycamobile']['cost']
    virtual34 = prices['england']['discord']['virtual34']['cost']

    await ctx.send(f'LycaMobile: {lycamobile}\nVirtual34: {virtual34}')

def setup(bot):
    bot.add_command(prices)








#🥀

    #######################################
   #                                     #
  #  Bot made with 💝 by Marcos0747    #
 #                                    #
#####################################
                                        #🥀
