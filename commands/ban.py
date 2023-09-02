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
headers = {
    
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
}
#semi-config
#code
@bot.command()
async def ban_order(ctx, id=None):
    if id is None:
        await ctx.send("🆔 Debes proporcionar la ID de la order para usar este comando.")
        return    
    channel = ctx.channel

    response = requests.get(f'https://5sim.net/v1/user/ban/{id}', headers=headers).text
    responsejson = json.loads(response)
    phone = responsejson['phone']
    
    if responsejson['status'] == 'BANNED':
        await channel.send(f'✅ Teléfono `{phone}` con el ID `{id}` banneado correctamente ✅')

def setup(bot):
    bot.add_command(ban_order)








#🥀

    #######################################
   #                                     #
  #  Bot made with 💝 by Marcos0747    #
 #                                    #
#####################################
                                        #🥀