#!/usr/bin/env python3
import time, asyncio, sys, random
import logging

from telethon import TelegramClient, events, utils

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = 'Horang'

siram = '/siram'
panen = '/ambilPanen'
farm = 'Kebun'
bot = ['danaudalamhutan', 'KampungMaifamXBot', 'KampungMaifamX4Bot', 'KampungMaifamBot']

logging.basicConfig(level=logging.ERROR)
    
async def bentar(w):
    await asyncio.sleep(w)

async def mancingddh(client,w):
    while True:
        await client.send_message(bot[0], "/fish")
        await bentar(w)
        
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot[1], siram))

    @client.on(events.NewMessage(from_users=bot[1]))
    async def handler(event):
        pesan = event.raw_text
        
        
        if "Berhasil menyiram tanaman" in pesan:
            time.sleep(245)
            await event.respond(panen)
            return
            
        if "Kamu berhasil memanen" in pesan:
            print(time.asctime(), pesan)
            time.sleep(2)
            await event.respond(siram)
            return
        
            
        if "Tak ada yang bisa dipanen" in pesan:
            time.sleep(2)
            await event.respond(siram)
            return
            
        if "Lahan tersisa di kebun kamu tidak mencukupi" in pesan:
            time.sleep(2)
            await event.respond(panen)
            return
         
        if 'Kamu tidak memiliki cukup energi' in pesan:
            print('Energi habis')
            time.sleep(2)
            await event.respond('/restore_max_confirm')
            return
            
        if 'Energi berhasil dipulihkan' in pesan:
            time.sleep(2)
            await event.respond(siram)
            return
        
        if 'Tak ada tanaman untuk disiram' in pesan:
            time.sleep(2)
            await event.respond(farm)
            return
          
        if '🌲 Kebun' in pesan:
            if 'siap panen!!' in pesan:
                time.sleep(2)
                await event.respond(panen)
            else:
                time.sleep(245)
                await event.respond(panen)
            return
          
       
        
    client.start() 
    print(time.asctime(), '-', 'start')
    client.loop.create_task(mancingddh(client,245))
    print(time.asctime(), '-', 'ddh')
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')