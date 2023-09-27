#!/usr/bin/env python3
import time, asyncio, sys, random


from telethon import TelegramClient, events, utils, Button

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input("Mau akun mana = ")

#bot_id = 'KampungMaifamxBot'
Area = 'Gua Tambang'

print("Pilih bot yang digunakan")



mpm = input("\tKetik 1 untuk Bot Alpha\n\tKetik 2 untuk Bot X\n\tKetik 3 untuk Bot X4\n   Angka = ")

if mpm == '1':
    bot_id = 'KampungMaifamBot'
elif mpm == '2':
    bot_id = 'KampungMaifamXBot'
elif mpm == '3':
    bot_id = 'KampungMaifamX4Bot'
    

print("Mau Alat Apa")

mpm = input("\t1. ⛏⛏⛏⛏\n\t2. ⛏⛏⛏\n\t3. ⛏⛏\n\t4. ⛏\n\t5. 💣\n\t6. ⛏⛏⛏⛏⛏\n  Angka = ")

if mpm == '1':
    Alat = '⛏⛏⛏⛏'
elif mpm == '2':
    Alat = '⛏⛏⛏'
elif mpm == '3':
    Alat = '⛏⛏'
elif mpm == '4':
    Alat = '⛏'
elif mpm == '5':
    Alat = '💣'
elif mpm == '6':
    Alat = '⛏⛏⛏⛏⛏'


with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot_id, Alat))
        @client.on(events.NewMessage(from_users=bot_id))
        async def handler(event):
            pesan = event.raw_text

            if "Tingkatkan kemampuanmu" in pesan:
                time.sleep(2)
                await event.click(text=Alat)
                print(pesan)
                return

            elif "Kamu mendapat" in pesan:
                time.sleep(2)
                await event.click(text=Alat)
                print(pesan)
                return
                
            elif 'Kamu tidak memiliki' in pesan:
                time.sleep(2)
                await event.respond('/restore_max_confirm')
                print(time.asctime(), 'Isi Ulang Energi')
                return
                
            elif 'Energi berhasil' in pesan:
                time.sleep(2)
                await event.respond(Alat) 
                return
            
            else :
                time.sleep(2)
                await event.click(text=Alat)
                print(time.asctime(), 'Lempar bom')
                print(pesan)
                return
            
client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')