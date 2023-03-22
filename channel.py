import requests
from telethon import TelegramClient, functions, events, sync
import re,os
from time import sleep
from telethon.sync import TelegramClient, events
from telethon import functions,types
tele_bot = "6079327194:AAFcpnsB9vEbcjdfI70KQ1aYtlj8qTlIgxQ"
own_id = "5582470474"
o = input("EnTeR UsEr : ")
app =  TelegramClient("fy",api_id=16885299,api_hash="89b9ac040eaf94268318ec3a43c39cdd")
app.start()
qq = 0
result = app(functions.channels.CreateChannelRequest(
    title="hmd .",
    about="@A_N_3"
))
ch = result.updates[1].channel_id
print(ch)
def fucker(o):
    global qq
    if 7==7:
    	qq+=1
    	url = f"https://t.me/{o}"
    	req = requests.get(url)
    	if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
    		sj = app(functions.channels.UpdateUsernameRequest(
    channel=ch, username=o
))
    		if sj == True:
    			y = requests.post(f"""https://api.telegram.org/bot{tele_bot}/sendmessage?chat_id={own_id}&text=𓆩 We are the strongest  !'
⎱UserName: ❲ @{o} ❳
⎱ClickS: ❲ {qq} ❳
⎱Save: ❲ Channel ❳""")
while True:
		if 8==8:
			print(str(f"[ {qq} ] @{o}"))
			fucker(o)	
app.run()