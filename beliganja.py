#!/usr/bin/env python3
import time, asyncio, sys


from telethon import TelegramClient, events, utils, Button

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input('Akun : ')

Beli = '/beli_ganja_1e6'
Release = '/release_denganKartu'
Alamat = '/newaddressx_confirm'
bot_id = 'KampungMaifamXBot'
Act = '/act_FulltimeCriminal'

with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot_id, Beli))

    @client.on(events.NewMessage(from_users=bot_id))
    async def handler(event):
        pesan = event.raw_text
        
        if 'Berhasil membeli' in pesan:
            print(time.asctime(), 'Berhasil membeli ganja')
            time.sleep(2)
            await event.respond(Beli)
            return
          
        if 'Oh tidak!!' in pesan or 'ganti alamat kamu' in pesan:
            print(time.asctime(), pesan)
            time.sleep(2)
            #await event.respond(Beli)
            #await event.respond(Alamat)
            return
          
        if 'Kamu terkurung dalam penjara menjijikkan' in pesan:
            print(time.asctime(), 'Yah di penjara')
            time.sleep(2)
            await event.respond(Release)
            return
          
        if 'Apa kamu yakin ingin menggunakan' in pesan:
            print(time.asctime(), 'Sogok polisi dlu')
            time.sleep(2)
            await event.click(text="Confirm")
            return
          
        if 'Sekarang kamu bebas sebebas bebasnya' in pesan:
            print(time.asctime(), pesan)
            #time.sleep(2)
            #await event.respond(Alamat)
            #time.sleep(2)
            #await event.respond(Beli)
            time.sleep(2)
            await event.respond(Act)
            return
          
        if 'FulltimeCriminal' in pesan:
            time.sleep(5)
            print(pesan)
            await event.click(text="Claim")
            time.sleep(5)
            await event.respond(Beli)
            return
        
        
    client.start() 
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	