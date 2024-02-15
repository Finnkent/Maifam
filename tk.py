#!/usr/bin/env python3
import time, asyncio, sys

from telethon import TelegramClient, events, utils, Button

api_id =  
api_hash = 
sesi_file = input("Akun = ")

restore = '/restore_max_confirm'
#bot
print("\ncontoh: Angka = 2")
print("Pilih bot yng digunakan")
mpm = input("\tKetik 1 untuk Bot Alpha\n\tKetik 2 untuk Bot X\n\tKetik 3 untuk Bot X4\n   Angka = ")
if mpm == '1':
    bot_id = 'KampungMaifamBot'
elif mpm == '2':
    bot_id = 'KampungMaifamXBot'
elif mpm == '3':
    bot_id = 'KampungMaifamX4Bot'

#jenis hewan 
print()
hewan = input("Nama hewan = ")
#jumlah 
print()
jmlh = input("berapa jumlahnya = ")

ternak = f"/pelihara_{hewan}_{jmlh}"

with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot_id, ternak))

    @client.on(events.NewMessage(from_users=bot_id))
    async def handler(event):
        pesan = event.raw_text
        
        if "Berhasil menambahkan" in pesan or "Kandang ternak khusus penuh" in pesan:
            print(time.asctime(), pesan)
            time.sleep(2)
            await event.respond('/ambilHewan')
            return
        
        if "Kamu berhasil mendapat" in pesan:
            print(time.asctime(), pesan)
            time.sleep(2)
            await event.respond(ternak)
            return
          
        
        if "Kamu tidak memiliki cukup energi" in pesan:
            print(time.asctime(), 'Isi Ulang Energi')
            time.sleep(2)
            await event.respond(restore)
            return
                
        if "Energi berhasil" in pesan:
            print(time.asctime(), 'Energi pulih')
            time.sleep(2)
            await event.respond(ternak) 
            return
          
        elif "Tidak ada yang bisa diambil" in pesan:
            print(time.asctime(), pesan)
            time.sleep(2)
            await event.respond(ternak)
            return
        
        
    client.start() 
    print(time.asctime(), '-', 'mulai')
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	
