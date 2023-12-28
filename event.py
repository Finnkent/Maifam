import time, asyncio, sys, random



import logging

from telethon import TelegramClient, events, utils, Button

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input("Akun : ")

bot_id = 'KampungMaifamX4Bot'
cmd = '/xm2023_GudangSanta'
grup = -1001611827546
jeda = 6

logging.basicConfig(level=logging.ERROR)


with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot_id, cmd))
        @client.on(events.NewMessage(from_users=bot_id))
        async def handler(event):
            pesan = event.raw_text
            
              
            if "namun ia telah kabur" in pesan or "Kamu mencuri dari" in pesan or "telah kabur..." in pesan:
                time.sleep(jeda)
                await event.click(text="Cari Hadiah")
                return
              
            elif "Pelan-pelan" in pesan or "Berhasil mengambil" in pesan:
                time.sleep(jeda)
                await event.click(text="Cari Hadiah")
                return
              
            elif "dari jauh melihat" in pesan:
                time.sleep(jeda)
                await event.click(text="Curi")
                return
            
            elif "menemukan sebuah" in pesan:
                time.sleep(jeda)
                await event.click(text="Ambil")
                return
              
            elif "Berhasil mengambil 📱 iPong15ProMag" in pesan:
                await client.forward_messages(grup, event.message)
                return
            
client.start()
print('Started')
client.run_until_disconnected()