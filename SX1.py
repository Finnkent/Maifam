import time
import asyncio
import sys
import random

from telethon import TelegramClient, events, utils, Button

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input('Akun : ')

bot_id = 'KampungMaifamXBot'
Mine = '⛏'
mese = 'SpaceExploration'

with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot_id, mese))
        @client.on(events.NewMessage(from_users=bot_id))
        async def handler(event):
            pesan = event.raw_text


            if "Proses tambang"  in pesan:
                time.sleep(180)
                await event.click(text=Mine)                
                print(time.asctime(), 'Tambang')
                return

            if "Energi berhasil"  in pesan:
                time.sleep(2)
                await event.respond("/spaceExploration")             
                print(time.asctime(), 'Menu')
                return

            if "Chrysus"  in pesan:
                time.sleep(2)
                await event.click(text=Mine)                
                print(time.asctime(), 'Tambang')
                return

            if "Tunggu sekitar"  in pesan:
                time.sleep(30)
                await event.click(text=Mine)                
                print(time.asctime(), 'Menu')
                return

            elif 'Kamu tidak memiliki' in pesan:
                time.sleep(2)
                await event.respond('/restore')
                print(time.asctime(), 'Isi Ulang Energi')
                return
            
client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')
