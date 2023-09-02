#imports
import requests, json, datetime, discord, config as CONFIG
from discord.utils import get
from discord.ext import commands, tasks
from datetime import datetime
#imports

#semi-config
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=['?','!', '.'], case_insensitive=True, intents = intents)
bot.remove_command('help')
token = (CONFIG.API_TOKEN)
headers = {
    
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
}
#semi-config
Activation  =  False
#code
@bot.command()
async def balance(ctx):
    r = json.loads(requests.get(f'https://5sim.net/v1/user/profile', headers=headers).text)

    embed = discord.Embed(
        title = '🎈 Balance',
        description = f'''{r['balance']} ₽\n1,00 Rublo ruso (₽) =0,0096379263 Euros (€)''',
        color=discord.Colour(0x87cbec))
    
    await ctx.send(embed=embed)


def setup(bot):
    bot.add_command(balance)








#🥀

    #######################################
   #                                     #
  #  Bot made with 💝 by Marcos0747    #
 #                                    #
#####################################
                                        #🥀