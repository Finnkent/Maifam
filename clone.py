import time, asyncio, sys, random

import logging

from telethon import TelegramClient, events, utils, Button

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input("Akun : ")

bot_id = 'KampungMaifamBot'
grup = -1001611827546
gudang = '/xm2023_SantaWarehouse'

logging.basicConfig(level=logging.ERROR)
    
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot_id, gudang))

    @client.on(events.NewMessage(from_users=bot_id))
    async def handler(event):
        global gas

        if "Hadiah akan direset" in event.raw_text:
            gas = await client.get_messages(bot_id, ids=event.message.id)
            time.sleep(6)
            await gas.click(text='Cari Hadiah')
            return
        
        if 'ingin mencuri hadiah' in event.raw_text:
            gas = await client.get_messages(bot_id, ids=event.message.id)
            time.sleep(6.2)
            await gas.click(text='Curi')
            return
        
        if "dan menemukan sebuah" in event.raw_text:
            gas = await client.get_messages(bot_id, ids=event.message.id)
            time.sleep(5.2)
            await gas.click(text='Ambil')
            return
        
        if 'Berhasil mengambil' in event.raw_text:
            gas = await client.get_messages(bot_id, ids=event.message.id)
            time.sleep(6.5)
            await gas.click(text='Cari Hadiah')
            return

        if 'Pelan-pelan,' in event.raw_text:
            gas = await client.get_messages(bot_id, ids=event.message.id)
            time.sleep(6)
            await gas.click(text='Cari Hadiah')
            return

        if 'Kamu mencuri dari' in event.raw_text:
            gas = await client.get_messages(bot_id, ids=event.message.id)
            time.sleep(6)
            await gas.click(text='Cari Hadiah')
            return

        if 'namun ia telah kabur' in event.raw_text:
            gas = await client.get_messages(bot_id, ids=event.message.id)
            time.sleep(6)
            await gas.click(text='Cari Hadiah')
            return
          
    client.start()
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Berhenti')