#imports
import requests, discord, json, datetime, asyncio, config as CONFIG
from discord.utils import get
from discord.ext import commands, tasks
from datetime import datetime
from data import loggers 
#imports
global esms

#semi-config
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=['?','!', '.'], case_insensitive=True, intents=intents)
bot.remove_command('help')
token = (CONFIG.API_TOKEN)
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
}
#semi-config
Activation = False
#code
@bot.command()
async def buy(ctx, country=None, operator=None, product=None):
    if country is None or operator is None or product is None:
        await ctx.send("Debes proporcionar todos los argumentos: `país`, `operadora` y `producto`.")
        return    
    global embedsms, smsv

    def get_code():
        global embedsms
        r = json.loads(requests.get(f'https://5sim.net/v1/user/check/{str(dio["id"])}',headers=headers).text)
        if len(r['sms']) == 0:
            return False
        else:
            try:
                global smsv
                for message in r['sms']:
                    smsv = message['text']
            except Exception as e:
                print(e)
                return False

            embedsms = discord.Embed(
                title='📬 SMS RECIVIDO 📬',
                colour=discord.Color.green()
            )
            embedsms.add_field(name='Order ID', value=r['id'], inline=True)
            embedsms.add_field(name='SMS', value=smsv, inline=True)
            embed.add_field(name="",value="\u200b",  inline=False)
            embedsms.add_field(name='Producto', value=r['product'], inline=True)
            embedsms.add_field(name='Status', value=r['status'], inline=True)
            embed.set_footer(text="Termina la order usando ?finis_order | order ID")

    Activation = True
    while Activation:
        try:
            dio = requests.get(f'https://5sim.net/v1/user/buy/activation/{country}/{operator}/{product}', headers=headers)

            if dio.status_code == 200:
                dio = json.loads(dio.text)

                created_at = dio['created_at']
                expires = dio['expires']

                c = datetime.strptime(created_at.split('.')[0].replace('T', ' '), '%Y-%m-%d %H:%M:%S')
                e = datetime.strptime(expires.split('.')[0].replace('T', ' '), '%Y-%m-%d %H:%M:%S')
                delta = (e) - (c)
                time_in_seconds = delta.total_seconds()
                time_in_minutes = time_in_seconds / 60
                
                embed = discord.Embed(
                    title='✅ HECHO ✅',
                    colour=discord.Color.green()
                )
                embed.add_field(name='Order ID', value=dio['id'], inline=True)
                embed.add_field(name='País', value=dio['country'], inline=True)
                embed.add_field(name='Número', value=dio['phone'], inline=True)
                embed.add_field(name='Operador', value=dio['operator'], inline=True)
                embed.add_field(name='Precio', value=dio['price'], inline=True)
                embed.add_field(name='Producto', value=dio['product'], inline=True)
                embed.add_field(name='Expira', value=int(time_in_minutes), inline=True)
                embed.add_field(name='Status', value=dio['status'], inline=True)
                await ctx.send(embed=embed)
                Activation = False
                get_code()
                while get_code() == False:
                    await asyncio.sleep(0.10)
                    pass
                await ctx.send(f'{ctx.author.mention}', embed=embedsms)

            else:
                embed = discord.Embed(
                    title=':x: ERROR :x:',
                    colour=discord.Color.red(),
                    description=f'{dio.text}')
                await ctx.send(embed=embed)
                return
                
        except Exception as e:
            embed = discord.Embed(
                title=':x: ERROR :x:',
                colour=discord.Color.red(),
                description=f'{e}')     
            await ctx.send(embed=embed)
            return False

def setup(bot):
    bot.add_command(buy)









#🥀

    #######################################
   #                                     #
  #  Bot made with 💝 by Marcos0747    #
 #                                    #
#####################################
                                        #🥀









