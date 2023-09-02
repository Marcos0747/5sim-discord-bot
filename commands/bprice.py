#imports
import discord, requests
from discord.utils import get
from discord.ext import commands, tasks
from concurrent.futures import ThreadPoolExecutor
#imports
#semi-config
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=['?','!', '.'], case_insensitive=True, intents = intents)
bot.remove_command('help')
#semi-config
#code
@bot.command()
async def best_price(ctx, product_name):
    bestPrice = 1337
    bestPriceCT = ""
    Countries = ['afghanistan', 'albania', 'algeria', 'angola', 'anguilla', 'antiguaandbarbuda', 'argentina', 'armenia', 'aruba', 'australia', 'austria', 'azerbaijan', 'bahamas', 'bahrain', 'bangladesh', 'barbados', 'belarus', 'belgium', 'belize', 'benin', 'bhutane', 'bih', 'bolivia', 'botswana', 'brazil', 'bulgaria', 'burkinafaso', 'burundi', 'cambodia', 'cameroon', 'canada', 'capeverde', 'caymanislands', 'chad', 'chile', 'china', 'colombia', 'comoros', 'congo', 'costarica', 'croatia', 'cyprus', 'czech', 'djibouti', 'dominica', 'dominicana', 'easttimor', 'ecuador', 'egypt', 'england', 'equatorialguinea', 'eritrea', 'estonia', 'ethiopia', 'finland', 'france', 'frenchguiana', 'gabon', 'gambia', 'georgia', 'germany', 'ghana', 'greece', 'grenada', 'guadeloupe', 'guatemala', 'guinea', 'guineabissau', 'guyana', 'haiti', 'honduras', 'hongkong', 'hungary', 'india', 'indonesia', 'ireland', 'israel', 'italy', 'ivorycoast', 'jamaica', 'japan', 'jordan', 'kazakhstan', 'kenya', 'kuwait', 'kyrgyzstan', 'laos', 'latvia', 'lesotho', 'liberia', 'lithuania', 'luxembourg', 'macau', 'madagascar', 'malawi', 'malaysia', 'maldives', 'mauritania', 'mauritius', 'mexico', 'moldova', 'mongolia', 'montenegro', 'montserrat', 'morocco', 'mozambique', 'myanmar', 'namibia', 'nepal', 'netherlands', 'newcaledonia', 'newzealand', 'nicaragua', 'niger', 'nigeria', 'northmacedonia', 'norway', 'oman', 'pakistan', 'panama', 'papuanewguinea', 'paraguay', 'peru', 'philippines', 'poland', 'portugal', 'puertorico', 'reunion', 'romania', 'russia', 'rwanda', 'saintkittsandnevis', 'saintlucia', 'saintvincentandgrenadines', 'salvador', 'samoa', 'saotomeandprincipe', 'saudiarabia', 'senegal', 'serbia', 'seychelles', 'sierraleone', 'singapore', 'slovakia', 'slovenia', 'solomonislands', 'southafrica', 'spain', 'srilanka', 'suriname', 'swaziland', 'sweden', 'switzerland', 'taiwan', 'tajikistan', 'tanzania', 'thailand', 'tit', 'togo', 'tonga', 'tunisia', 'turkey', 'turkmenistan', 'turksandcaicos', 'uganda', 'ukraine', 'uruguay', 'usa', 'uzbekistan', 'venezuela', 'vietnam', 'virginislands', 'zambia', 'zimbabwe']
    Products = ['1688', '23red', '32red', '99app', 'ace2three', 'adidas', 'agroinform', 'airbnb', 'airtel', 'aitu', 'akelni', 'alfa', 'algida', 'alibaba', 'aliexpress', 'alipay', 'amasia', 'amazon', 'aol', 'apple', 'astropay', 'auchan', 'avito', 'avon', 'azino', 'b4ucabs', 'baidu', 'banqi', 'bigolive', 'billmill', 'bisu', 'bitaqaty', 'bitclout', 'bittube', 'blablacar', 'blizzard', 'blockchain', 'blued', 'bolt', 'brand20ua', 'burgerking', 'bykea', 'cafebazaar', 'caixa', 'careem', 'carousell', 'cdkeys', 'cekkazan', 'citaprevia', 'citymobil', 'clickentregas', 'cliqq', 'clubhouse', 'cmtcuzdan', 'coinbase', 'coinfield', 'craigslist', 'cryptocom', 'dbrua', 'deliveroo', 'delivery', 'dent', 'dhani', 'didi', 'digikala', 'discord', 'disneyhotstar', 'divar', 'dixy', 'dodopizza', 'domdara', 'dominospizza', 'dostavista', 'douyu', 'dream11', 'drom', 'drugvokrug', 'dukascopy', 'easypay', 'ebay', 'ebikegewinnspiel', 'edgeless', 'electroneum', 'eneba', 'ezbuy', 'faberlic', 'facebook', 'fiqsy', 'fiverr', 'foodpanda', 'foody', 'forwarding', 'freecharge', 'galaxy', 'gamearena', 'gameflip', 'gamekit', 'gamer', 'gcash', 'get', 'getir', 'gett', 'gg', 'gittigidiyor', 'global24', 'globaltel', 'globus', 'glovo', 'google', 'grabtaxi', 'green', 'grindr', 'hamrahaval', 'happn', 'haraj', 'hepsiburadacom', 'hezzl', 'hily', 'hopi', 'hqtrivia', 'humblebundle', 'humta', 'huya', 'icard', 'icq', 'icrypex', 'ifood', 'immowelt', 'imo', 'inboxlv', 'indriver', 'ininal', 'instagram', 'iost', 'iqos', 'ivi', 'iyc', 'jd', 'jkf', 'justdating', 'justdial', 'kakaotalk', 'karusel', 'keybase', 'komandacard', 'kotak811', 'kucoinplay', 'kufarby', 'kvartplata', 'kwai', 'lazada', 'lbry', 'lenta', 'lianxin', 'line', 'linkedin', 'livescore', 'magnit', 'magnolia', 'mailru', 'mamba', 'mcdonalds', 'meetme', 'mega', 'mercado', 'michat', 'microsoft', 'miloan', 'miratorg', 'mobile01', 'momo', 'monese', 'monobank', 'mosru', 'mrgreen', 'mtscashback', 'myfishka', 'myglo', 'mylove', 'mymusictaste', 'mzadqatar', 'nana', 'naver', 'ncsoft', 'netflix', 'nhseven', 'nifty', 'nike', 'nimses', 'nrjmusicawards', 'nttgame', 'odnoklassniki', 'offerup', 'offgamers', 'okcupid', 'okey', 'okta', 'olacabs', 'olx', 'onlinerby', 'openpoint', 'oraclecloud', 'oriflame', 'other', 'ozon', 'paddypower', 'pairs', 'papara', 'paxful', 'payberry', 'paycell', 'paymaya', 'paypal', 'paysend', 'paytm', 'peoplecom', 'perekrestok', 'pgbonus', 'picpay', 'pof', 'pokec', 'pokermaster', 'potato', 'powerkredite', 'prajmeriz2020', 'premiumone', 'prom', 'proton', 'protonmail', 'protp', 'pubg', 'pureplatfrom', 'pyaterochka', 'pyromusic', 'q12trivia', 'qiwiwallet', 'quipp', 'rakuten', 'rambler', 'rediffmail', 'reuse', 'ripkord', 'rosakhutor', 'rsa', 'rutube', 'samokat', 'seosprint', 'sheerid', 'shopee', 'signal', 'sikayetvar', 'skout', 'snapchat', 'snappfood', 'sneakersnstuff', 'socios', 'sportmaster', 'spothit', 'ssoidnet', 'steam', 'surveytime', 'swvl', 'taksheel', 'tango', 'tantan', 'taobao', 'telegram', 'tencentqq', 'ticketmaster', 'tiktok', 'tinder', 'tosla', 'totalcoin', 'touchance', 'trendyol', 'truecaller', 'twitch', 'twitter', 'uber', 'ukrnet', 'uploaded', 'vernyi', 'vernyj', 'viber', 'vitajekspress', 'vkontakte', 'voopee', 'wechat', 'weibo', 'weku', 'weststein', 'whatsapp', 'wildberries', 'wingmoney', 'winston', 'wish', 'wmaraci', 'wolt', 'yaay', 'yahoo', 'yalla', 'yandex', 'yemeksepeti', 'youdo', 'youla', 'youstar', 'zalo', 'zoho', 'zomato']


    def get_product_price(country):
        try:
            data = requests.get(f"https://5sim.net/v1/guest/products/{country}/any").json()
            if product_name in data:
                price = data[product_name]["Price"]
                return country, price
        except:
            return country, float("inf")

    if product_name in Products:
        with ThreadPoolExecutor() as executor:
            results = executor.map(get_product_price, Countries)

        min_price = float("inf")
        bestPriceCT = []

        for result in results:
            if result is not None:
                country, price = result
                if price < min_price:
                    min_price = price
                    bestPriceCT = [country]
                elif price == min_price:
                    bestPriceCT.append(country)

        if bestPriceCT:
            await ctx.send(f"El mejor precio es `{min_price}₽` de {', '.join(bestPriceCT)}")
        else:
            await ctx.send("No ha habido resultados")
    else:
        await ctx.send("Lo siento, no he encontrado el producto.")

def setup(bot):
    bot.add_command(best_price)








#🥀

    #######################################
   #                                     #
  #  Bot made with 💝 by Marcos0747    #
 #                                    #
#####################################
                                        #🥀