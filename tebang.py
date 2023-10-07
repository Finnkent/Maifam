#!/usr/bin/env python3
import time
import re
import asyncio 
import sys
import random

from telethon import TelegramClient, events, utils, Button
api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file =input("Mau akun mana = ")

bot_id = ('danaudalamhutan', 'KampungMaifamBot', 'KampungMaifamXBot')
crop = '/tebangTanaman'

tnm = input("Nama tanaman = ")
jmlh = input("Jumlah tanaman = ")
tanam = f"/tanam_{tnm}_{jmlh}"

match_tanam = re.match(r'/tanam_(\w+)_(\d+)', tanam)
if match_tanam:
    tnm = match_tanam.group(1)
    jmlh = int(match_tanam.group(2))
    
    
async def nungguin(w):
   await asyncio.sleep(w)

print("Peringatan : Script ini akan menebang semua tanaman Anda.")
confirmation = input("Apakah Anda yakin ingin melanjutkan? \n(1 untuk lanjut dan 0 untuk batalkan) : ")

if confirmation == '1':
    print("Melanjutkan...")
    with TelegramClient(sesi_file, api_id, api_hash) as client:
         client.loop.run_until_complete(client.send_message(bot_id[2], tanam))

else:
    print("Operasi dibatalkan.")
    sys.exit()
    
@client.on(events.NewMessage(from_users=bot_id[2]))
async def handler(event):
        pesan = event.raw_text
        
        if "🌲 Tebang Tanaman" in pesan:
            print(time.asctime()+" Tebang")
            kode = int(pesan.split('_')[1])
            time.sleep(2)
            await event.respond(f"/tebangTanaman_{kode}_{jmlh}")
            return
            
        if 'kamu yakin ingin menebang' in pesan:
            time.sleep(2)
            await event.click(text="TebangTanaman")
            return
          
        if 'Tanaman telah ditebang' in pesan:
            time.sleep(2)
            await event.respond(tanam)
            return
          
        if 'Kamu berhasil menanam' in pesan or 'Lahan tersisa di kebun' in pesan:
            time.sleep(2)
            await event.respond(crop)
            return
          
        if 'Kamu tidak memiliki cukup energi' in pesan:
            print(time.asctime(), 'Habis energi')
            time.sleep(2)
            await event.respond('/restore')
            return
        

        if 'Energi berhasil dipulihkan' in pesan:
            print('energi di pulihkan')
            await nungguin(1)

          
          
with client:
    client.start()
    #client.loop.create_task(mancingddh(client,245))
    client.run_until_disconnected()