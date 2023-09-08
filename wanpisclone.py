import time
import asyncio

from telethon.sync import TelegramClient
from telethon import events

from tqdm import tqdm
from rich.progress import Progress

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'

punyaku = [
  'Keisya',
  'Mio',
  'Jenia',
  'Cibu', 
  'Eunji', 
  'Fainry', 
  'Blu', 
  'Genya', 
  'Minu',
  'Einly',
  
]

bot_id = 'GrandPiratesBot'
adv = '/adventure'

async def my_function():
    while True:
        for aaa in punyaku:
            async with TelegramClient(aaa, api_id, api_hash) as client:
                await client.send_message(bot_id, adv)
                
                @client.on(events.NewMessage(from_users=adv))
                async def handler(event):
                    pesan = event.text
                      
                    if "100x!! Kamu mendapat" in pesan or "250x!! Sekarang ia" in pesan or "250x!! Kamu mendapat" in pesan:
                        time.sleep(2)
                        await event.respond(adv)
                        return
                      
                    if "Energi krumu telah habis" in pesan or "musuh kabur" in pesan:
                        time.sleep(2)
                        await event.respond('/restore')  
                        return
                    
                    
                    
                    
                    elif "Kalahkan musuh yang ada" in pesan or "Kalahkan semua musuh" in pesan:
                        time.sleep(2)
                        await event.click(0,0)
                        return
                      
                    elif "dan dihadang oleh 4 musuh:" in pesan:
                        time.sleep(2)
                        await event.click(1,0)
                        return
                    
                    elif "dan dihadang oleh 3 musuh:" in pesan:
                        time.sleep(2)
                        await event.click(1,0)
                        return
                    
                    elif "dan dihadang oleh 2 musuh:" in pesan:
                        time.sleep(2)
                        await event.click(1,0)
                        return
                        
                    elif "dan dihadang oleh 1 musuh:" in pesan:
                        time.sleep(2)
                        await event.click(0,0)
                        return
                     
                     
                        
                    elif "KAMU MENANG!!" in pesan:
                        
                        time.sleep(2)
                        await event.click(0,0)
                        return
                      
                    elif "Musuh menang" in pesan:
                        if "untuk mencapai kekuatan" in pesan:
                            time.sleep(2)
                            await event.respond('/restore')
                        else:
                            time.sleep(2)
                            await event.click(0,0)
                        return
                    
                        
                    elif "sedang tidak dalam kondisi" in pesan:
                        time.sleep(2)
                        await event.click(0,0)
                        return
                      
                      
                    elif "untuk bisa lanjut ke pulau" in pesan:
                        time.sleep(2)
                        await event.click(0,0)
                        return
                        
                    elif "Berhasil memulihkan" in pesan:
                        time.sleep(2)
                        await event.respond(adv)
                        return
                      
                    
                    
                        
                    elif "kekuatan kalian sebagai" in pesan:
                        time.sleep(2)
                        await event.click(0,0)
                        return
                    
                    #EastBlue: ShellsTown
                    elif 'Kota pinggir laut' in pesan:
                        time.sleep(2)
                        await event.click(0,0)
                        return
                    
                    #EastBlue: OrangeTown
                    elif 'Kota kecil yang ditumbuhi' in pesan:
                        time.sleep(2)
                        await event.click(0,0)
                        return
                    
                    #EastBlue: SyrupVillage
                    elif 'Desa sederhana yang indah' in pesan:
                        time.sleep(2)
                        await event.click(0,0)
                        return
                    
                    #EastBlue: Baratie
                    elif 'Sebuah restauran yang mengapung' in pesan:
                        time.sleep(2)
                        await event.click(0,0)
                        return
                    
                    #EastBlue: ArlongPark
                    elif 'Kastil manusia ikan' in pesan:
                        time.sleep(2)
                        await event.click(0,0)
                        return
                      
                    
                    #EastBlue: Loguetown
                    elif 'Dikenal sebagai kota awal mula' in pesan:
                        time.sleep(2)
                        await event.click(0,0)
                        return
                      
                    if "maksimal 100x tiap jamnya" in pesan or "sedang dalam perjalanan menuju" in pesan:
                        await asyncio.sleep(1)
                        await client.disconnect()
                        close()

                await client.run_until_disconnected()
            print(aaa, '- Complete -', time.asctime())
        for remaining in tqdm(range(120), desc="Waiting"):
            await asyncio.sleep(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(my_function())