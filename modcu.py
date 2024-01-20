import time, os
import asyncio
import sys, re
import random
from time import sleep
from random import randint
from datetime import datetime
from telethon import TelegramClient, events, utils, Button
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = 'Frizi'

bot_id = 'TrueMafiaBot'
lanjut = '/next@TrueMafiaBot'
grup = -1001876432938
msg = 'modcuu woii'

    
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(grup , lanjut))
    @client.on(events.NewMessage(incoming=True, from_users=bot_id))
    async def handle_chat(event):
        pesan = event.raw_text
                
        if "Perhatian!" in pesan:
            await event.click(0)
            print(time.asctime(), 'Game baru')
            return
                
        if "Anda adalah 👨🏼 Warga" in pesan:
            time.sleep(7)
            await client.send_message(grup ,lanjut)
            print(time.asctime(), 'Next')
            return
              
        if "Permainan sudah dimulai..." in pesan:
            time.sleep(3)
            await client.send_message(grup,lanjut)
            print(time.asctime(), 'Lanjut')
            return
                
        if "Permainan telah berakhir" in pesan:
            print(time.asctime(), pesan)
            time.sleep(2)
            await client.send_message(grup,msg)
            return

        
    @client.on(events.NewMessage(chats=grup))
    async def handler(event):
        pesan = event.raw_text
        
        if "Jumlah minimum pemain - 4" in pesan or "Jika pemain 12 sedikit untuk" in pesan:
            print(time.asctime(), pesan)
            await bentar(2)
            await client.send_message(grup, lanjut)
            return
          
        
                
    client.start() 
    print(time.asctime(), 'Mulai...')
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	