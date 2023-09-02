#imports
import os, json, time, requests, discord, datetime, asyncio, config as CONFIG, threading, colorama, random
from discord.utils import get
from discord.ext import commands, tasks
from datetime import datetime
from Chromify import Fore, init
from config import MESSAGE_LOGS
#imports

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=['?','!', '.'], case_insensitive=True, intents = intents)
bot.remove_command('help')
RPC = random.choice(CONFIG.RPCS)
token = (CONFIG.API_TOKEN)
BOT_STATUS = (CONFIG.BOT_STATUS)


Activation  =  False



def thrit(func):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
    return wrapper



@bot.event
async def on_ready():
    print(f'{Fore.LIGHT_GREEN}    ______     _              ____  ____  ______{Fore.RESET}')
    print(f'{Fore.LIGHT_GREEN}   / ____/____(_)___ ___     / __ )/ __ \/_  __/{Fore.RESET}')
    print(f'{Fore.LIGHT_GREEN}  /___ \/ ___/ / __ `__ \   / __  / / / / / /   {Fore.RESET}')
    print(f'{Fore.LIGHT_GREEN} ____/ (__  ) / / / / / /  / /_/ / /_/ / / /    {Fore.RESET}')
    print(f'{Fore.LIGHT_GREEN}/_____/____/_/_/ /_/ /_/  /_____/\____/ /_/     {Fore.RESET}')
    print(f'{Fore.BLUE}Conectado como: {bot.user.name}{Fore.RESET}')
    print(f'{Fore.BLUE}Bot ID: {bot.user.id}{Fore.RESET}')
    print(f"{Fore.BLUE}Estado del bot en config.py: {BOT_STATUS}{Fore.RESET}")
    print(f"{Fore.BLUE}Discord Version: {discord.__version__}{Fore.RESET}")
    await bot.change_presence(status=discord.Status(CONFIG.BOT_STATUS), activity=discord.Game(RPC))
    command_files = os.listdir('./commands')
    command_files = [file for file in command_files if file.endswith('.py')]
    command_names = [file[:-3] for file in command_files]

    for name in command_names:
        command_module = __import__(f"commands.{name}", fromlist=[name])
        setup = getattr(command_module, "setup", None)
        print(f"{Fore.RED}[{Fore.CYAN}Comando Cargado{Fore.RED}]: {Fore.WHITE}{name}")
        if callable(setup):
            setup(bot)

for command in bot.commands:
    if command.callback is not None:
        command.callback = thrit(command.callback)


logs = 'data/logs'

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if MESSAGE_LOGS: 
        if not os.path.exists(logs):
            os.makedirs(logs)
        file_path = os.path.join(logs, 'logs_mensajes.txt')
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f'{message.author.name}: {message.content}\n')

    await bot.process_commands(message)
    
    
#Ignorar
@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000 
    embed = discord.Embed(
        title='Pong! :ping_pong:',
        description=f'Latencia: `{latency:.2f}` ms',
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed) 
#Ignorar


bot.run(CONFIG.BOT_TOKEN)








#🥀

    #######################################
   #                                     #
  #  Bot made with 💝 by Marcos0747    #
 #                                    #
#####################################
                                        #🥀