#!/usr/bin/env python3
import time, asyncio, sys, random
import logging

from telethon import TelegramClient, events, utils

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = 'Horang'

restore = '/restore_max_confirm'
siram = '/siram'
panen = '/ambilPanen'
farm = 'Kebun'
bot = ['danaudalamhutan', 'KampungMaifamXBot', 'KampungMaifamX4Bot', 'KampungMaifamBot']
ternak = ['/ambilHasil']
feed = '/beriMakan'
jumlah_perolehan = 0
tnk = 0

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
        global tnk, jumlah_perolehan
        pesan = event.raw_text
        
        
        if "Berhasil menyiram tanaman" in pesan:
            print(time.asctime(), 'Berhasil menyiram')
            tnk = 0
            jumlah_perolehan = 0  # Reset perolehan jika tidak ada yang bisa dipanen
            time.sleep(2)
            await event.respond(ternak[tnk])
                #await event.respond(tanam)
            return

        if "Kamu berhasil memanen" in pesan:
            print(time.asctime(), pesan)
            await asyncio.sleep(2)
            jumlah_perolehan += 1
            if jumlah_perolehan >= 1:
                await event.respond(siram)
                jumlah_perolehan = 0
            else:
                if tnk < len(ternak):
                    await event.respond(feed)
                    tnk += 1
                else:
                    tnk = 0
                    await event.respond(feed)

        if "Kamu memperoleh:" in pesan:
            print(time.asctime(), 'Hasil ternak')
            await asyncio.sleep(2)
            jumlah_perolehan += 1
            if jumlah_perolehan >= 10:
                await event.respond(panen)
                jumlah_perolehan = 0
            else:
                if tnk < len(ternak):
                    await event.respond(feed)
                    tnk += 1
                else:
                    tnk = 0
                    await event.respond(feed)
            
            
        if "Tak ada yang bisa dipanen" in pesan:
            print(time.asctime(), pesan)
            tnk = 0
            jumlah_perolehan = 0  # Reset perolehan jika tidak ada yang bisa dipanen
            time.sleep(2)
            await event.respond(ternak[tnk])
                #await event.respond(tanam)
            return
          
          
        if "Berhasil memberi makan ternak" in pesan:
            print(time.asctime(), pesan)
            tnk = 0
            time.sleep(2)
            await event.respond(ternak[tnk])
            return
          
        if "Tak ada ternak untuk" in pesan:
            print(time.asctime(), pesan)
            tnk = 0
            time.sleep(2)
            await event.respond(ternak[tnk])
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
                time.sleep(2)
                await event.respond(ternak[tnk])
            return
          
       
        
    client.start() 
    print(time.asctime(), '-', 'start')
    client.loop.create_task(mancingddh(client,245))
    print(time.asctime(), '-', 'ddh')
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')