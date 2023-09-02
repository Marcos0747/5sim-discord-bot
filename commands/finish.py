#imports
import requests, json, discord, datetime, config as CONFIG
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
async def finish_order(ctx, id=None):
    if id is None:
        await ctx.send("🆔 Debes proporcionar la ID de la order para usar este comando.")
        return
    r = requests.get(f'https://5sim.net/v1/user/finish/{id}', headers=headers)
    
    if r.status_code == 200:
        r = json.loads(r.text)
        embed = discord.Embed(
            title=':white_check_mark: Acabada!',
            colour=discord.Color.green()
        )
        
        embed.add_field(name='Order ID', value=r['id'], inline=False)
        embed.add_field(name='País', value=r['country'], inline=False)
        embed.add_field(name='Número', value=r['phone'], inline=False)
        embed.add_field(name='Precio', value=r['price'], inline=False)
        embed.add_field(name='Producto', value=r['product'], inline=False)
        embed.add_field(name='Status', value=r['status'], inline=False)
        
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title=':x: ERROR :x:',
            colour=discord.Color.red(),
            description='Order no encontrada'
        )
        
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_command(finish_order)
    







#🥀

    #######################################
   #                                     #
  #  Bot made with 💝 by Marcos0747    #
 #                                    #
#####################################
                                        #🥀