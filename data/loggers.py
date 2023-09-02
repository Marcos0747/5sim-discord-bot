from discord_webhook import DiscordWebhook
import datetime, discord, requests
import config as CONFIG


def send_log(user_id, user_name):
    if CONFIG.LOGGER_BUY:  
        webhook_url = CONFIG.WHLOGS  
        webhook = DiscordWebhook(url=webhook_url)

        embed = discord.Embed(title='Comando Buy', color=0xd5eb6c, description='El usuario ha usado el comando buy.')
        embed.set_footer(text=f'Usuario: {user_name} | ID: {user_id}')
        embed.add_field(name='Comando', value='buy', inline=False)
        footer_text = embed.footer.text  

        content = f'👤 Nombre de Usuario : `{user_name}` | 🆔 Identificador : `{user_id}`'
        data = {
            'content': content,
            'embeds': [{
                'title': embed.title,
                'color': embed.color.value,
                'footer': {'text': footer_text},
                'fields': [
                    {'name': field.name, 'value': field.value, 'inline': field.inline}
                    for field in embed.fields
                ],
                'description': embed.description
            }]
        }
        response = requests.post(webhook_url, json=data)

        return response








#🥀

    #######################################
   #                                     #
  #  Bot made with 💝 by Marcos0747    #
 #                                    #
#####################################
                                        #🥀
