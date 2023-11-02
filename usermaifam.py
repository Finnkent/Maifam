import time
import asyncio
import sys
import random
import datetime
import os
import re
import logging
from telethon.sync import TelegramClient, events, utils, Button

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = 'King'
client = TelegramClient(sesi_file, api_id, api_hash)

mepam = "KampungMaifamBot"
mepamx = "KampungMaifamXBot"
mepamx4 = "KampungMaifamX4Bot"


logging.basicConfig(level=logging.ERROR)

restore = "/restore_max_confirm"
alat = "Tarik Jala"
area = ""
user = [1222376950,5199147926]
grup = 1522767385

respond_to_group = False


areas_dict = {
    'SL': 'Sungai Lala',
    'SM': 'Sungai Mimi',
    'SB': 'Sungai Badabu',
    'DS': 'Danau Soprano',
    'TB': 'Teluk Bulari',
    'LS': 'Laut Sempit',
    'LG': 'Laut Gabagaba',
    'LP': 'Laut Purba',
    'LB': 'Laut Berhantu',
    'DP': 'Danau Penjara',
    'AS': 'All Sea',
}


async def bentar(w):
    await asyncio.sleep(w)
    
def stop_sesi():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    

@client.on(events.NewMessage(from_users=mepam))
async def handler_maifam(event):
    global respond_to_group
    if not respond_to_group:
        return
    
    pesan = event.raw_text
    
    
   
@client.on(events.NewMessage(from_users=mepamx))
async def handler_memancing(event):
    global respond_to_group
    if not respond_to_group:
        return
    
    pesan = event.raw_text
    
    if "Kamu berhasil" in pesan or "Kamu mendapat" in pesan:
        await asyncio.sleep(2)
        if area in areas_dict:
            await event.respond(areas_dict[area])
        print(pesan)
        
    elif 'tidak memiliki cukup energi' in pesan:
        await asyncio.sleep(2)
        await event.respond(restore)
        print(time.asctime(), 'Isi Ulang Energi')
        
                
    elif 'Energi berhasil' in pesan:
        time.sleep(2)
        if area in areas_dict:
            await event.respond(areas_dict[area])
        print(time.asctime(), 'Lanjut')
              
    elif '==' in pesan:
        await asyncio.sleep(2)
        await event.click(text=alat)
    
    elif 'Sungai dangkal' in pesan:
        await asyncio.sleep(2)
        await event.click(text=alat)
        
    elif 'Legenda mengatakan' in pesan:
        await asyncio.sleep(2)
        await event.click(text=alat)
        
    elif 'Hanya ikan besar' in pesan:
        await asyncio.sleep(2)
        await event.click(text=alat)
        
    elif 'Ikan langka' in pesan:
        await asyncio.sleep(2)
        await event.click(text=alat)
        
    elif 'Terletak di bagian' in pesan:
        await asyncio.sleep(2)
        await event.click(text=alat)
        
    elif 'Orang-orang mengklaim' in pesan:
        await asyncio.sleep(2)
        await event.click(text=alat)
        
    elif 'Bertahun-tahun yang' in pesan:
        await asyncio.sleep(2)
        await event.click(text=alat)
        
    elif 'Laut aneh berbahaya' in pesan:
        await asyncio.sleep(2)
        await event.click(text=alat)
        
    elif 'Laut terkutuk' in pesan:
        await asyncio.sleep(2)
        await event.click(text=alat)
        
    elif 'Bagian kecil' in pesan:
        await asyncio.sleep(2)
        await event.click(text=alat)
        
    elif 'Pemerintah Maikantri' in pesan:
        await asyncio.sleep(2)
        await event.click(text=alat)
       
                
    elif 'Kamu tidak sedang' in pesan:
        await asyncio.sleep(2)
        if area in areas_dict:
            await event.respond(areas_dict[area])
        print(pesan)
    
        
        
@client.on(events.NewMessage(from_users=mepamx4))
async def handler_ayam(event):
    global respond_to_group
    if not respond_to_group:
        return
    
    pesan = event.raw_text
    
        
        
@client.on(events.NewMessage(from_users=user))
async def handler_user(event):
    global respond_to_group, area, slot
    pesan = event.raw_text
    
    if '/ceklist' in pesan:
        await asyncio.sleep(2)
        pesan_list = """Daftar perintah :
cmd :
!gasmancing_area (botx)
!stop_makro

key :
!pancingan (list area mancing)
"""
        await event.reply(pesan_list)
        
    if '/pancingan' in pesan:
        await asyncio.sleep(2)
        pancingan_list = """Daftar kata kunci area :
        
SL = Sungai Lala
SM = Sungai Mimi
SB = Sungai Badabu
DS = Danau Soprano
TB = Teluk Bulari
LS = Laut Sempit
LG = Laut Gabagaba
LP = Laut Purba
LB = Laut Berhantu
DP = Danau Penjara
AS = All Sea
"""
        await event.reply(pancingan_list)
        
    
    if '/stop_makro' in pesan:
        await asyncio.sleep(2)
        await event.reply("Gas lagi bg!")
        stop_sesi()
        respond_to_group = False


    if '/gasmancing' in pesan:
        await asyncio.sleep(2)
        split_result = pesan.split('/gasmancing_')
        if len(split_result) > 1:
            area = split_result[1]
            if area in areas_dict:
                time.sleep(2)
                await event.respond(f"Mulai memancing di {areas_dict[area]}")
                time.sleep(2)
                await client.send_message(mepamx, areas_dict[area])
                
            else:
                await event.reply("Maaf, area tersebut tidak ada dalam daftar")
            respond_to_group = True
        else:
            await event.reply("Silahkan kirimkan beserta area")
        
        

with client:
    print(time.asctime(), "- Userbot Dimulai")
    client.run_until_disconnected()