import time, asyncio, sys, random
import logging
from telethon import TelegramClient, events, utils, Button

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = "Finnkent"

bot_id = 'GrandPiratesBot'
adv = '/adventure'
kill = 0
ex = '/use_EXPPill'

logging.basicConfig(level=logging.ERROR)

def tunggu_hingga_menit_detik_00():
    saat_ini = time.localtime()
    menit_sekarang = saat_ini.tm_min
    detik_sekarang = saat_ini.tm_sec
    
    if menit_sekarang == 0 and detik_sekarang == 0:
        return  # Sudah 00:00, tidak perlu menunggu
    
    detik_yang_harus_ditunggu = (60 - menit_sekarang) * 60 - detik_sekarang
    print(f"Menunggu hingga 00:00.")
    time.sleep(detik_yang_harus_ditunggu)


with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot_id, ex))
        @client.on(events.NewMessage(from_users=bot_id))
        async def handler(event):
            pesan = event.raw_text
            global kill
            
            if "maksimal 100x tiap jamnya" in pesan or "sedang dalam perjalanan menuju" in pesan:
                tunggu_hingga_menit_detik_00()
                await event.respond('/adventure')
                return
              
            if "100x!! Kamu mendapat" in pesan or "250x!! Sekarang ia" in pesan or "250x!! Kamu mendapat" in pesan:
                time.sleep(2)
                await event.respond(adv)
                return
              
            if "Energi krumu telah habis" in pesan or "musuh kabur" in pesan:
                time.sleep(2)
                await event.respond('/restore')  
                return
            
            if kill >= 10:
                time.sleep(2)
                await event.respond(ex)  
                kill = 0
                return
            
            
            elif "Kalahkan musuh yang ada" in pesan or "Kalahkan semua musuh" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
              
            elif "dan dihadang oleh 4 musuh:" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
            
            elif "dan dihadang oleh 3 musuh:" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
            
            elif "dan dihadang oleh 2 musuh:" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
                
            elif "dan dihadang oleh 1 musuh:" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
             
             
                
            elif "KAMU MENANG!!" in pesan:
                kill += 1
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
                await event.respond(ex)
                return
              
            elif "Berhasil menggunakan 💊EXPPill" in pesan:
                time.sleep(2)
                await event.respond(ex)
                return
              
            elif "maksimal 10 item buff" in pesan or "Kamu tidak memiliki 💊EXPPill" in pesan:
                time.sleep(2)
                await event.respond(adv)
                return
              
            
                
            elif "kekuatan kalian sebagai" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
            
            #EastBlue: ShellsTown
            elif "Kota pinggir laut" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
            
            #EastBlue: OrangeTown
            elif "Kota kecil yang ditumbuhi" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
            
            #EastBlue: SyrupVillage
            elif "Desa sederhana yang indah" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
            
            #EastBlue: Baratie
            elif "Sebuah restauran yang mengapung" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
            
            #EastBlue: ArlongPark
            elif "Kastil manusia ikan" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
              
            
            #EastBlue: Loguetown
            elif "Dikenal sebagai kota awal mula" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
            
            #EastBlue: TwinCapes
            elif "Lewati Laboon si paus" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
            
            #GrandLine: WhiskyPeak
            elif "Di balik keramahtamahan warganya" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
            
            #GrandLine: LittleGarden
            elif "Sebuah pulau di GrandLine" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
              
            #GrandLine: WinterSea
            elif "sebuah area laut bersalju" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
              
            #GrandLine: DrumIsland 
            elif "Pulau dingin yang ditutupi salju" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
            
            #Alabasta: Nanohana
            elif "pertama di Kerajaan Alabasta" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
            
            
            
client.start()
print('Started')
client.run_until_disconnected()