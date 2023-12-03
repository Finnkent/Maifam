#by Ditza
#!/usr/bin/env python3
import time
import re
import asyncio 
import sys
import random

from telethon import TelegramClient, events, utils, Button
api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = 'Finnkent'

dest = ('danaudalamhutan', 'KampungMaifamBot', 'KampungMaifamXBot')
maling = True

uang = 'Hapus menggunakan Uang'
#ch = 'Afterbluesky'
    
async def nungguin(w):
   await asyncio.sleep(w)

async def mancingddh(client,w):
    while True:
        await client.send_message(dest[0], "/fish")
        await nungguin(w)

with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(dest[2], '/homes_curiUang'))
    
@client.on(events.NewMessage(from_users=dest[2]))
async def handler(event):
        pesan = event.raw_text
        global maling
        
        if  ("Villager's Houses" in pesan) or ("Rumah Warga" in pesan):
            print(time.asctime()+" Kunjungi Rumah Warga ke - ")
            time.sleep(2)
            x = pesan.split('/curi')
            file = open("Homes.txt","a+")
            count = 0
            for i in range(1,11):
                y = x[i].split(' - ')
                z = y[0].replace('Uang', '/curiTernak')
                #file.write(z+'\n')
                await event.respond(z)
                print(time.asctime()+" Masuk Rumah")
                file.write(z+'\n')
                print(time.asctime()+" Maling Alamat ke-"+str(i))
                count+=1
            
                if count%10==0:
                    time.sleep(2)
                    await event.respond(uang)
                    print(time.asctime(), 'hapus buron')
                    #time.sleep(2)
                    #await client.send_message(dest[1], '/act_ThieveMastery')
                    #print(time.asctime(), 'Cek ACT')
                    #await asyncio.sleep(5)
                    #await event.respond('/act_ThieveMastery')
                    #time.sleep(2)
                    #await event.click(0)
                    #time.sleep(2)
                    #await event.respond('/harvestAnimal')
                    #print(time.asctime(), 'ambil hewan')
                    #time.sleep(2)
                    #await event.respond('/feed')
                    #print(time.asctime(), 'beri makan')
                    #time.sleep(2)
                    #await event.respond('/masak_Bacon_220')
                    #print(time.asctime(), 'masak')

                time.sleep(3)
            await event.respond('/homes_curiUang')
            file.close()
            return
            
        if 'Kamu tidak memiliki cukup energi' in pesan:
            print(time.asctime(), 'Habis energi')
            time.sleep(2)
            await event.respond('/restore_max_confirm')
            time.sleep(2)
            return
          
        if 'Energi berhasil dipulihkan' in pesan:
            print('energi di pulihkan')
            await nungguin(1)


        if 'Polisi menemukanmu' in pesan:
            print('kena polisi')
            await client.send_message(dest[2], '/release')
            print('nyogok polisi')
            await nungguin(1)
            
        if 'Apa kamu yakin untuk menggunakan' in pesan:
            print(time.asctime(), 'Sogok polisi dlu')
            time.sleep(2)
            await event.click(text="Confirm")
            return
          
        #if 'WonderstoneOfYouth' in pesan or 'Stealestrite' in pesan:
            #print('Item sihir nih')
            #time.sleep(2)
            #await client.forward_messages(ch, event.message)
            #time.sleep(4)
            #return
            
with client:
    client.start()
    client.loop.create_task(mancingddh(client,245))
    client.run_until_disconnected()