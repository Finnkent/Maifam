#!/usr/bin/env python3
import time, asyncio, sys, random
import logging

from telethon import TelegramClient, events, utils

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = 'Horang'

print("\nPilih tempat mancing")
pilih = input('\tKetik 1 untuk 💦 Lala\n\tKetik 2 untuk 💦 Mimi\n\tKetik 3 untuk 💦 Badabu\n\tKetik 4 untuk 🏝 Soprano\n\tKetik 5 untuk 💧 Bulari\n\tKetik 6 untuk 🌊 Narrow/Sempit\n\tKetik 7 untuk 🌊 Gabagaba\n\tKetik 8 untuk 🌊 Ancient/Purba\n\tKetik 9 untuk 🌊 Haunted/Berhantu\n\tKetik 10 untuk 🌊 All\n\tKetik 11 untuk 💦 Danau Penjara\n   Angka =  ')
if pilih == '1': 
    tempat = 'Lala River' 
elif pilih == '2': 
    tempat = 'Mimi River' 
elif pilih == '3': 
    tempat = 'Badabu River' 
elif pilih == '4': 
    tempat = 'Soprano Lake' 
elif pilih == '5': 
    tempat = 'Bay of Bulari' 
elif pilih == '6': 
    tempat = 'Narrow Sea'
elif pilih == '7': 
    tempat = 'Gabagaba Ocean' 
elif pilih == '8': 
    tempat = 'Ancient Sea' 
elif pilih == '9': 
    tempat = 'Haunted Sea'
elif pilih == '10': 
    tempat = 'All Sea'
elif pilih == '11': 
    tempat = 'Danau Penjara'
    
alat = 'Tarik Jala' 

restore = '/restore_max_confirm'
siram = '/siram'
panen = '/ambilPanen'
farm = 'Kebun'
bot = ['danaudalamhutan', 'KampungMaifamXBot', 'KampungMaifamX4Bot', 'KampungMaifamBot']
ternak = ['/ambilHasil']
feed = '/beriMakan'
jumlah_perolehan = 0
jumlah_penanaman = 0
tnk = 0


logging.basicConfig(level=logging.ERROR)
    
async def bentar(w):
    await asyncio.sleep(w)
    

async def mancingddh(client,w):
    while True:
        await client.send_message(bot[0], "/fish")
        await bentar(w)
        
tanam_commands = ['/tanam_Kentang_593', '/tanam_Wortel_593', '/tanam_Strawberry_593']

with TelegramClient(sesi_file, api_id, api_hash) as client:
    # Iterate through the planting commands and plant each crop one by one
    for command in tanam_commands:
        client.loop.run_until_complete(client.send_message(bot[1], command))
    
        @client.on(events.NewMessage(from_users=bot[1]))
        async def handler(event):
            global tnk, jumlah_perolehan, jumlah_penanaman
            pesan = event.raw_text
            
            
            if "Berhasil menyiram tanaman" in pesan:
                print(time.asctime(), 'Berhasil menyiram')
                tnk = 0
                jumlah_perolehan = 0  # Reset perolehan jika tidak ada yang bisa dipanen
                time.sleep(2)
                await event.respond(tempat)
                    #await event.respond(tanam)
                return
              
            if "Kamu berhasil menangkap" in pesan:
                print(time.asctime(), 'Ikan')
                tnk = 0
                jumlah_perolehan = 0  # Reset perolehan jika tidak ada yang bisa dipanen
                time.sleep(2)
                await event.respond(ternak[tnk])
                    #await event.respond(tanam)
                return
    
            if "Kamu berhasil memanen" in pesan:
                print(time.asctime(), pesan)
                time.sleep(2)
                jumlah_perolehan += 1
                if jumlah_perolehan >= 1:
                    await event.respond(command)
                    jumlah_perolehan = 0
                else:
                    if tnk < len(ternak):
                        time.sleep(2)
                        await event.respond(feed)
                        tnk += 1
                    else:
                        tnk = 0
                        time.sleep(2)
                        await event.respond(feed)
    
            if "Kamu memperoleh:" in pesan:
                print(time.asctime(), 'Hasil ternak')
                time.sleep(2)
                if jumlah_perolehan >= 3:
                    await event.respond(panen)
                    jumlah_perolehan = 0
                else:
                    if tnk < len(ternak):
                        time.sleep(2)
                        await event.respond(feed)
                        tnk += 1
                    else:
                        tnk = 0
                        time.sleep(2)
                        await event.respond(feed)
                
                
            if "Tak ada yang bisa dipanen" in pesan:
                print(time.asctime(), pesan)
                tnk = 0
                jumlah_perolehan = 0  # Reset perolehan jika tidak ada yang bisa dipanen
                time.sleep(2)
                await event.respond(farm)
                    #await event.respond(tanam)
                return
              
              
            if "Berhasil memberi makan ternak" in pesan:
                tnk = 0
                jumlah_perolehan += 1
                time.sleep(2)
                await event.respond(ternak[tnk])
              
            if "Tak ada ternak untuk" in pesan:
                print(time.asctime(), pesan)
                tnk = 0
                jumlah_perolehan = 0
                time.sleep(2)
                await event.respond(ternak[tnk])
                return
            
            if "Kamu berhasil menanam" in pesan:
                jumlah_penanaman += 1
                time.sleep(2)
                if jumlah_penanaman == 3:
                    await event.respond(siram)
                    jumlah_penanaman = 0
                else:
                    time.sleep(2)
                    if jumlah_penanaman == 1:
                        await event.respond(tanam_commands[1])
                    elif jumlah_penanaman == 2:
                        await event.respond(tanam_commands[2])
                return
    
            elif "Lahan tersisa di kebun kamu tidak mencukupi" in pesan:
                time.sleep(2)
                await event.respond(panen)
                return
             
            elif 'Kamu tidak memiliki cukup energi' in pesan:
                print('Energi habis')
                time.sleep(2)
                await event.respond('/restore_max_confirm')
                return
                
            elif 'Energi berhasil dipulihkan' in pesan:
                time.sleep(2)
                await event.respond(siram)
                return
            
            elif 'Tak ada tanaman untuk disiram' in pesan:
                
                time.sleep(2)
                await event.respond(farm)
                return
              
            elif '🌲 Kebun' in pesan:
                if 'siap panen!!' in pesan:
                    time.sleep(2)
                    await event.respond(panen)
                elif 'Kebun kamu kosong' in pesan:
                    time.sleep(2)
                    await event.respond(bot[1], command)
                elif 'x /siram' in pesan:
                    time.sleep(2)
                    await event.respond(siram)
                else:
                    if tnk < len(ternak):
                        time.sleep(2)
                        await event.respond(ternak[tnk])
                        tnk += 1
                    else:
                        tnk = 0
                        time.sleep(2)
                        await event.respond(ternak[tnk])
                return
            
            elif 'tidak memiliki cukup energi' in pesan:
                time.sleep(2)
                await event.respond(restore)
                print(time.asctime(), 'Isi Ulang Energi')
                
                        
            elif 'Energi berhasil' in pesan:
                time.sleep(2)
                await event.click(text=alat)
                print('Lanjut Gan')
                
                      
            elif '==' in pesan:
                time.sleep(2)
                await event.click(text=alat)
            
            elif 'Sungai dangkal' in pesan:
                time.sleep(2)
                await event.click(text=alat)
                
            elif 'Legenda mengatakan' in pesan:
                time.sleep(2)
                await event.click(text=alat)
                
            elif 'Hanya ikan besar' in pesan:
                time.sleep(2)
                await event.click(text=alat)
                
            elif 'Ikan langka' in pesan:
                time.sleep(2)
                await event.click(text=alat)
                
            elif 'Terletak di bagian' in pesan:
                time.sleep(2)
                await event.click(text=alat)
                
            elif 'Orang-orang mengklaim' in pesan:
                time.sleep(2)
                await event.click(text=alat)
                
            elif 'Bertahun-tahun yang' in pesan:
                time.sleep(2)
                await event.click(text=alat)
                
            elif 'Laut aneh berbahaya' in pesan:
                time.sleep(2)
                await event.click(text=alat)
                
            elif 'Laut terkutuk' in pesan:
                time.sleep(2)
                await event.click(text=alat)
                
            elif 'Bagian kecil' in pesan:
                time.sleep(2)
                await event.click(text=alat)
                
            elif 'Pemerintah Maikantri' in pesan:
                time.sleep(2)
                await event.click(text=alat)
                   
            
        client.start() 
        print(time.asctime(), '-', 'start')
        client.loop.create_task(mancingddh(client,245))
        print(time.asctime(), '-', 'ddh')
        client.run_until_disconnected() 
        print(time.asctime(), '-', 'berhenti')