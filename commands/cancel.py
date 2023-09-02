#imports
import requests, discord, datetime, json, config as CONFIG
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
async def cancel_order(ctx, id=None):
    if id is None:
        await ctx.send("🆔 Debes proporcionar la ID de la order para usar este comando.")
        return    
    r = requests.get(f'https://5sim.net/v1/user/cancel/{id}', headers=headers)
    
    if r.status_code == 200:
        r = json.loads(r.text)
        embed = discord.Embed(
            title=':no_entry: Cancelado!',
            colour=discord.Color.red()
        )
        
        embed.add_field(name='Order ID', value=r['id'], inline=True)
        embed.add_field(name='País', value=r['country'], inline=True)
        embed.add_field(name='Número', value=r['phone'], inline=True)
        embed.add_field(name='Precio', value=r['price'], inline=True)
        embed.add_field(name='Producto', value=r['product'], inline=True)
        embed.add_field(name='Status', value=r['status'], inline=True)
        embed.add_field(name='\u200b', value='\u200b', inline=False)
        embed.add_field(name='Resultado', value='Order cancelada', inline=False)

        await ctx.send(embed=embed)
        return
    else:
        embed = discord.Embed(
            title=':x: ERROR :x:',
            colour=discord.Color.red()
        )
        
        embed.add_field(name='Error', value='Order no encontrada', inline=False)

        await ctx.send(embed=embed)
        return

def setup(bot):
    bot.add_command(cancel_order)








#🥀

    #######################################
   #                                     #
  #  Bot made with 💝 by Marcos0747    #
 #                                    #
#####################################
                                        #🥀