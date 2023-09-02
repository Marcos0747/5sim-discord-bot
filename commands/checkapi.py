#imports
import discord, requests, config as CONFIG
from discord.ext import commands
from data import loggers 
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
@bot.command()
async def check_api(ctx):

    try:

        response = requests.get("https://5sim.net/v1/user/profile", headers=headers)
        embed = discord.Embed(title=":x: ERROR :x:", description="", colour=discord.Colour.red())

        if response.status_code == 200:
            embed = discord.Embed(title="✅ HECHO ✅", 
                                  description="", 
                                  colour=discord.Colour.green())
            embed.add_field(name="Request Perfecta", 
                            value="Todo está funcionado perfectamente.")
            await ctx.send(embed=embed)

        if response.status_code == 401:
            embed.add_field(name=":x: ERROR :x:", 
                            value="Recuerda poner tu apikey en el archivo `config.py`.")
            await ctx.send(embed=embed)

        if response.status_code == 429:
            embed.add_field(name="⏰ TOMA UN RESPIRO ⏰", 
                            value="Estás bajo rate limit, espera unos minutos y vuelve a intentarlo. ")
            await ctx.send(embed=embed)

    except AttributeError:
        embed = discord.Embed(title=":x: ERROR :x:", 
                              description="", 
                              colour=discord.Colour.red())
        embed.add_field(name="[401] Unauthorized", value="Recuerda poner tu apikey en el archivo `config.py`.")
        await ctx.send(embed=embed)

    except Exception:
        raise Exception

def setup(bot):
    bot.add_command(check_api)
    







#🥀

    #######################################
   #                                     #
  #  Bot made with 💝 by Marcos0747    #
 #                                    #
#####################################
                                        #🥀


