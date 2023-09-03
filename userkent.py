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
sesi_file = 'Finnkent'
client = TelegramClient(sesi_file, api_id, api_hash)

mepam = "KampungMaifamBot"
mepamx = "KampungMaifamXBot"
mepamx4 = "KampungMaifamX4Bot"
one = 'GrandPiratesBot'

adv = '/adventure'

logging.basicConfig(level=logging.ERROR)

piggy = "/pelihara_BayiBabi_336"
cook = "/masak_minibacon_220"
chicken = "/beliternak_Ayam_Ayam_20"
alat = "Tarik Jala"
cmd = '/th_SlotMachine_SevenFish'
cmd1 = '/th_SlotMachine_add'
area = ""
slot = ""
user = 5199147926
grup = -1001946930100

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

slots_dict = {
    'Ikan': '/th_SlotMachine_SevenFish',
    'Daun': '/th_SlotMachine_SixLeaves',
}

async def bentar(w):
    await asyncio.sleep(w)
    
def stop_sesi():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def tunggu_hingga_menit_detik_00():
    saat_ini = time.localtime()
    menit_sekarang = saat_ini.tm_min
    detik_sekarang = saat_ini.tm_sec
    
    if menit_sekarang == 0 and detik_sekarang == 0:
        return  # Sudah 00:00, tidak perlu menunggu
    detik_yang_harus_ditunggu = (60 - menit_sekarang) * 60 - detik_sekarang
    print(f"Menunggu hingga 00:00.")
    time.sleep(detik_yang_harus_ditunggu)
    

@client.on(events.NewMessage(from_users=mepam))
async def handler_maifam(event):
    global respond_to_group
    if not respond_to_group:
        return
    
    pesan = event.raw_text
    
    
    #masak
    if "Berhasil memasak" in pesan:
        print(time.asctime(), pesan)
        await asyncio.sleep(2)
        await event.respond(cook)
        
    if 'Kamu tidak bisa memasak' in pesan:
        print(time.asctime(), 'Rehat')
        await asyncio.sleep(3240)
        await event.respond(cook)
    
    #slot
    if '10000000Qn' in pesan:
        time.sleep(2)
        await event.respond('/tamanHiburan_TembakTopeng')
        print('Mulai Dart')
            
                
    if 'CollectibleFragment SixLeaves!! Kamu memperoleh:' in pesan:
        time.sleep(2)
        await event.respond(cmd1)
      
                
    elif 'Ada tujuh jenis ikan' in pesan:
        time.sleep(2)
        await event.click(1,0)
            
    elif 'Ada enam jenis daun' in pesan:
        time.sleep(2)
        await event.click(1,0)
            
    elif 'Kamu memutar SlotMachine 10x' in pesan:
        time.sleep(2)
        await event.click(1,0)
            
    elif 'Koin untuk' in pesan:
        if 'SevenFish 🎰 SlotMachine' in pesan:
          time.sleep(2)
          await event.respond(cmd1)
          return
        else:
          time.sleep(2)
          await event.respond("/collectibleFragment_SixLeaves")
            
    elif 'Fragment dikumpulkan:  ✅' in pesan:
        time.sleep(2)
        await event.click(text="Get CollectibleItem")
        time.sleep(2)
        await event.respond(cmd1)
    
    elif 'Kumpulkan fragment untuk memperoleh' in pesan:
        time.sleep(2)
        await event.respond(cmd1)
                
            
    elif 'Apa kamu' in pesan:
        time.sleep(2)
        await event.click(text="Confirm")
            
    elif 'Berhasil membeli tambahan' in pesan:
        time.sleep(2)
        if slot in slots_dict:
            await event.respond(slots_dict[slot])
        print(pesan)
           
    elif 'Setiap harinya' in pesan:
        time.sleep(2)
        await event.click(text='Mulai')
 
    elif 'Pilih sasaran' in pesan:
        time.sleep(2)
        await event.click(0,1)
            
    elif 'Lemparanmu berhasil' in pesan:
        time.sleep(2)
        await event.click(text='Lanjut')
            
    elif 'Sayang sekali' in pesan:
        time.sleep(2)
        await event.click(text='Lanjut')
            
    elif 'Kesempatan' in pesan:
        time.sleep(2)
        await client.send_message(grup, 'Slot telah selesai di mainkan')
            
   
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
        await event.respond('/restore_max_confirm')
        print(time.asctime(), 'Isi Ulang Energi')
        
                
    elif 'Energi berhasil' in pesan:
        await asyncio.sleep(2)
        await event.click(text=alat)
        print('Lanjut Gan')
        
              
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
    
    #beliayam
    if "Kamu membeli 🐓Ayam" in pesan:
        print(time.asctime(), 'Beli ayam')
        await asyncio.sleep(2)
        await event.respond(chicken)
          
    if 'Kamu memerlukan 20' in pesan:
        await asyncio.sleep(2)
        await client.send_message(grup, 'Kandang sudah penuh')
    
    #bayibabi
    if "Berhasil menambahkan" in pesan or "Kandang ternak khusus penuh" in pesan:
        time.sleep(2)
        await event.respond('/ambilHewan')
        
        
    if "Kamu berhasil mendapat" in pesan:
        print(time.asctime(), pesan)
        time.sleep(2)
        await event.respond(piggy)
          
          
        
    if "Kamu tidak memiliki cukup energi" in pesan:
        print(time.asctime(), 'Isi Ulang Energi')
        time.sleep(2)
        await event.respond(restore)
            
                
    if "Energi berhasil" in pesan:
        print(time.asctime(), 'Energi pulih')
        time.sleep(2)
        await event.respond(piggy) 
            
          
    elif "Tidak ada yang bisa diambil" in pesan:
        print(time.asctime(), pesan)
        time.sleep(2)
        await event.respond(piggy)
            
        


@client.on(events.NewMessage(from_users=one))
async def handler_one(event):
    global respond_to_group
    if not respond_to_group:
        return
      
    pesan = event.raw_text
            
            
    if "Kalahkan semua musuh yang ada" in pesan or "Kalahkan musuh yang ada" in pesan:
        time.sleep(2)
        await event.click(0,0)
                
              
    if "dan dihadang oleh 4 musuh:" in pesan:
        time.sleep(2)
        await event.click(0,0)
                
            
    if "dan dihadang oleh 3 musuh:" in pesan:
        time.sleep(2)
        await event.click(0,0)
               
            
    if "dan dihadang oleh 2 musuh:" in pesan:
        time.sleep(2)
        await event.click(0,0)
                
                
    if "dan dihadang oleh 1 musuh:" in pesan:
        time.sleep(2)
        await event.click(0,0)
                
                
    if "KAMU MENANG!!" in pesan:
        time.sleep(2)
        await event.click(0,0)
                
              
    if "Musuh menang" in pesan:
        if "untuk mencapai kekuatan" in pesan:
           time.sleep(2)
           await event.respond('/restore')
        else:
           time.sleep(2)
           await event.click(0,0)
        return
            
    elif "Energi krumu telah habis" in pesan:
        time.sleep(2)
        await event.respond('/restore')  
                
                
    elif "kelompok musuh kabur" in pesan:
        time.sleep(2)
        await event.click(0,0)
                
              
    elif "100x!! Kamu mendapat" in pesan or "250x!! Sekarang ia" in pesan:
        time.sleep(2)
        await event.click(0,0)
                
              
    elif "Tidak ada lawan yang bisa dilawan" in pesan:
        time.sleep(2)
        await event.click(0,0)
        
    elif "tidak dalam kondisi yang prima" in pesan:
        time.sleep(2)
        await event.click(0,0)
        
                
    elif "Berhasil memulihkan" in pesan:
        time.sleep(2)
        await event.respond('/adventure')
        
              
    elif "sudah mencapai batas maksimal" in pesan:
        await client.send_message(grup, 'Kuota habis silahkan menunggu sampai 00.00')
        tunggu_hingga_menit_detik_00()
        await event.respond('/adventure')
        
        
@client.on(events.NewMessage(from_users=user))
async def handler_user(event):
    global respond_to_group, area, slot
    pesan = event.raw_text
    
    if '/ceklist' in pesan:
        await asyncio.sleep(2)
        pesan_list = """Daftar perintah :
        
!cook (masak minibacon)(alpha)
!gasmancing_area (botx)
!beliayam (botx4)
!pancingan (list area mancing)
!mainslot (list jenis slot)
!slot_mode (alpha)
!piggy (ternak babi) (botx4)
!wanpis (Grand Pirates)
!stop_makro
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
        
    if '/mainslot' in pesan:
        await asyncio.sleep(2)
        mainslot_list = """Kata kunci mode slot : 
Ikan = SlotMachine_SevenFish
Daun = SlotMachine_SixLeaves
"""    
        await event.reply(mainslot_list)
       
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

    
    if '/cook' in pesan:
        await asyncio.sleep(2)
        await event.reply("Mulai memasak...!")
        await asyncio.sleep(2)
        await client.send_message(mepam, cook)
        respond_to_group = True

        
    if '/beliayam' in pesan:
        await asyncio.sleep(2)
        await event.reply("Mulai membeli ayam...!")
        await asyncio.sleep(2)
        await client.send_message(mepamx4, chicken)
        respond_to_group = True
        
        
    if '/slot' in pesan:
        await asyncio.sleep(2)
        split_result = pesan.split('/slot_')
        if len(split_result) > 1:
            slot = split_result[1]
            if slot in slots_dict:
                time.sleep(2)
                await event.respond(f"Mulai bermain di {slots_dict[slot]}")
                time.sleep(2)
                await client.send_message(mepam, slots_dict[slot])
                
            else:
                await event.reply("Maaf, jenis slot tersebut tidak ada dalam daftar")
            respond_to_group = True
        else:
            await event.reply("Anda harus menyertakan jenis slot")

    if '/wanpis' in pesan:
        await asyncio.sleep(2)
        await event.reply("Mulai berlayar...!")
        await asyncio.sleep(2)
        await client.send_message(one, adv)
        respond_to_group = True
        
    if '/piggy' in pesan:
        await asyncio.sleep(2)
        await event.reply("Mulai menernak babi...!")
        await asyncio.sleep(2)
        await client.send_message(mepamx4, piggy)
        respond_to_group = True


with client:
    print(time.asctime(), "- Userbot Dimulai")
    client.run_until_disconnected()