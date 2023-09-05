#!/usr/bin/env python3
import time
import asyncio
import sys
import random

from telethon import TelegramClient, events, utils, Button

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = 'Helio'

hasil = '/homesx'
Masak = '/masak_MiniBacon_220'
bot = 'kampungmaifamxbot'
curi = '/homesx'
alpha = 'kampungmaifambot'
buron = '/eat_holysnack'

with TelegramClient(sesi_file, api_id, api_hash) as client:
   client.loop.run_until_complete(client.send_message(bot, curi))
    
@client.on(events.NewMessage(from_users=bot))
async def handler(event):
        pesan = event.raw_text

        #file = open("homesx.txt","a+")
        if  ('Abandoned Houses' in pesan) or ('Rumah Kosong' in pesan) : 
            print('kunjungi rumah warga')
            time.sleep(2)
            #await event.respond('masuk')

            hasil = pesan.split('\n')
            
            print('Alamat')
            count = 0
            for i in range(1,6):
                z = hasil[i*5].replace('curiBarang', 'stealItem')    
                await event.respond(z)
                print('kirim')
                #file.write(z+'\n')
                print('maling alamat ke-'+str(i))  
                count+=1
                #number+=1
            
                if count%2==0:
                    time.sleep(2)
                    await event.respond(buron)
                    print(time.asctime(), 'Hapus Buronan')
                time.sleep(3.5)
            await event.respond('/homesx')
            #file.close()
            return
            
        if 'Your energy is too low' in pesan or 'Kamu tidak memiliki cukup energi' in pesan:
          	print('habis energi')
          	time.sleep(5)
          	await client.send_message(bot, '/restore_max_confirm')
          	return
        	
        if 'Polisi menemukanmu' in pesan or 'Kamu terkurung dalam penjara' in pesan:
            print('kena polisi')
            time.sleep(2)
            await event.respond('/release')
            return
          
        if 'Apa kamu yakin untuk menggunakan' in pesan:
            print(time.asctime(), 'Sogok polisi dlu')
            time.sleep(2)
            await event.click(text="Confirm")
            return
        
        if 'Sekarang kamu bebas sebebas' in pesan:
            print('Bebas')
            time.sleep(2)
            await event.respond(curi)
            return
          
        #if 'Seseorang bernama' in pesan:
            #print('Ada yang mau nyuri')
            #time.sleep(10)
            #await client.send_message(alpha,'/aktifkan_sekarang')
            #time.sleep(10)
            #await client.send_message(bot,'/aktifkan_sekarang') 
            #time.sleep(10)
            #return
         
        #if 'Berhasil memasak' in pesan:
            #time.sleep(2)
            #await event.respond(Masak)
            #print(pesan)
            #return
          
        #if 'Kamu tidak bisa memasak' in pesan:
            #time.sleep(2)
            #print(time.asctime(), 'Istirahat dulu yaah')
            #time.sleep(2)
            #await event.respond(curi)
            #return
        
        
client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')

       
