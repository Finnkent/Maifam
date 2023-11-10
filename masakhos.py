import time
import asyncio

from telethon.sync import TelegramClient
from telethon import events

from tqdm import tqdm
from rich.progress import Progress

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'

punyaku = [
  'AAA', 
  'BBB', 
  'CCC', 
  'DDD', 
  'EEE', 
  
]

mepam = 'KampungMaifamBot'
masak = '/masak_MiniBacon_220'


async def my_function():
    while True:
        for aaa in punyaku:
            async with TelegramClient(aaa, api_id, api_hash) as client:
                await client.send_message(mepam, masak)
                
                @client.on(events.NewMessage(from_users=mepam))
                async def handler(event):
                    pesan = event.text

                    if 'Berhasil memasak' in pesan:
                        await asyncio.sleep(2)
                        await event.respond(masak)
                        
                    
                    if 'Kamu tidak memiliki' in pesan:
                        time.sleep(2)
                        await event.respond('/restore_max_confirm')
                        
                    if 'Energi berhasil' in pesan:
                        time.sleep(2)
                        await event.respond(masak)
                        
                    if 'Kamu tidak bisa memasak' in pesan or 'Tidak cukup bahan' in pesan:
                        await asyncio.sleep(1)
                        await client.disconnect()
                        close()

                await client.run_until_disconnected()
            print(aaa, '- Complete -', time.asctime())
        for remaining in tqdm(range(2340), desc="Waiting"):
            await asyncio.sleep(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(my_function())