from Options.Options import *

import subprocess
import requests
import json
import random

TitrePage("Ip Generator + Checker")

def send_embed_webhook(webhook_url, embed_content, username=None, url=None):
                payload = {
                'embeds': [embed_content],
                'username': username,
                'avatar_url': url
                 }

                headers = {
            'Content-Type': 'application/json'
             }

                response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
username = 'Red-Tiger'
url = 'https://cdn.discordapp.com/attachments/1184160374342299688/1184160439001686056/IMG_1506.png?ex=658af659&is=65788159&hm=9a0297ee590e78acbafc75bc4686ce2b553e40a2f2a850101378a09f23e32d08&'
webhook = input(f"{couleur.RED}\nWebhook ? (y, n) -> {couleur.RESET}")
if webhook in ['y']:
    webhook_url = input(f"{couleur.RED}\nURL Webhook -> {couleur.RESET}")
def ping_ip(ip_address, nombre):

    try:

        result = subprocess.run(['ping', '-n', '1', ip_address], capture_output=True, text=True, timeout=2)
        
        
        if webhook in ['y']:
            if result.returncode == 0:
             print(f"{couleur.GREEN}[+] | {couleur.CYAN}{ip_address}{couleur.GREEN} | Ip Found | Tests n°{nombre}{couleur.RESET}")
             embed_content = {
           'title': f'Ip Found, Tests n°{nombre}',
           'description': f"**__Ip Online:__**\n```{ip_address}```",
           'color': 0xf00020,
           'footer': {
            "text": "Red-Tiger",
            "icon_url": "https://media.discordapp.net/attachments/944760272265031720/1179429697495498834/IMG_1506.png?ex=6582fb00&is=65708600&hm=cbdc48779b762d4d7c95c34bb68a8aabf8314519d0b50c4d7371bea19eac5db4&=&format=webp&quality=lossless",
             }
            }

             send_embed_webhook(webhook_url, embed_content, username, url)


            else:
                  print(f"{couleur.RED}[X] | {couleur.CYAN}{ip_address}{couleur.RED} | Ip Invalid | Tests n°{nombre}{couleur.RESET}")
        if webhook in ['n']:
             if result.returncode == 0:
                print(f"{couleur.GREEN}[+] | {couleur.CYAN}{ip_address}{couleur.GREEN} | Ip Found | Tests n°{nombre}{couleur.RESET}")
             else:
                  print(f"{couleur.RED}[X] | {couleur.CYAN}{ip_address}{couleur.RED} | Ip Invalid | Tests n°{nombre}{couleur.RESET}")
             

    except subprocess.TimeoutExpired:
        print(f"{couleur.RED}[X] | {couleur.CYAN}{ip_address}{couleur.RED} | Ip Invalid | Tests n°{nombre}{couleur.RESET}")
nombre = 0
while True:
    nombre_random1 = random.randint(1, 200)
    nombre_random2 = random.randint(1, 200) 
    nombre_random3 = random.randint(1, 100) 
    nombre_random4 = random.randint(1, 100)
    
    nombre += 1
    ip = f'{nombre_random1}.{nombre_random2}.{nombre_random3}.{nombre_random4}'


    ping_ip(ip, nombre)
    TitrePage(f"Red-Tiger | Ip Générator + Checker | Tentative n°{nombre}")