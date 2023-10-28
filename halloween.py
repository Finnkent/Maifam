import time, asyncio, sys, random

import logging

from telethon import TelegramClient, events, utils, Button

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input("Akun : ")
bot_id = 'KampungMaifamXBot'
adv = '/Halloween2023'

logging.basicConfig(level=logging.ERROR)


with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot_id, adv))
        @client.on(events.NewMessage(from_users=bot_id))
        async def handler(event):
            pesan = event.raw_text
            
            if "Kamu terdaftar sebagai" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
              
            if "Permen:" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
            
client.start()
print('Started')
client.run_until_disconnected()