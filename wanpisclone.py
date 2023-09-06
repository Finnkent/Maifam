import time, asyncio, sys, random
import logging
from telethon import TelegramClient, events, utils, Button

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input("Akun : ")

bot_id = 'GrandPiratesBot'
adv = '/adventure'

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
        client.loop.run_until_complete(client.send_message(bot_id, adv))
        @client.on(events.NewMessage(from_users=bot_id))
        async def handler(event):
            pesan = event.raw_text
            
            if "sudah mencapai batas maksimal" in pesan:
                tunggu_hingga_menit_detik_00()
                await event.respond('/adventure')
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
            
            elif "Energi krumu telah habis" in pesan:
                time.sleep(2)
                await event.respond('/restore')  
                return
                
            elif "anggota kelompokmu" in pesan or "musuh kabur" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
              
            elif "100x!! Kamu mendapat" in pesan or "250x!! Kamu mendapat" in pesan:
                time.sleep(2)
                await event.respond(adv)
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
            
            
client.start()
print('Started')
client.run_until_disconnected()