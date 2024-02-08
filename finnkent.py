import time, os, asyncio, sys, re, random, datetime
from time import sleep
from random import randint
from datetime import datetime
from telethon import TelegramClient, events, utils, Button
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_fil = 'Finnkent'

bot = ['danaudalamhutan', 'KampungMaifamXBot', 'KampungMaifamX4Bot', 'KampungMaifamBot']
result = "/casino_hasil"
mode = "/casino_UltraLuck_"
judi = mode+str(random.randint(1,50))+"_5e12"
ch = 'inMaifam'
hapus = 'Hapus menggunakan Uang'
masak = '/masak_minibacon_220' 
total = 0

narasi = {
    "Bahasa diubah ke Bahasa Indonesia",
    "Berhasil bertaruh",
    "Energi berhasil dipulihkan",
    "Sekarang kamu bebas",
    "Hasil akan keluar",
    "tidak bisa memasak",
}

ncasino = {
    "Belum ada taruhan",
    "Kamu bertaruh untuk angka",
    "Tulis angka",
}

nlanjut = {
    "Rumah yang kamu kunjungi",
    "Keamanan rumah yang mau",
    "tidak punya barang untuk dicuri",
    "Alamat yang sama",
    "Oh tidak!!",
}

async def bentar(w):
    await asyncio.sleep(w)

async def mancingddh(client,w):
    while True:
        await client.send_message(bot[0], "/fish")
        await bentar(w)

async def lanjut(tmp, event, buron):
    await asyncio.sleep(1.8)
    if tmp == 5:
        await event.respond(buron)
    else:
        await client.send_message(bot[1], maling[tmp])
    return tmp
    
with TelegramClient(sesi_fil, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot[1], masak))
    @client.on(events.NewMessage(incoming=True, from_users=bot[1]))
    async def handler(event):
        global maling
        global total 
        global tmp
        
        teks = event.text
        
        if any(nar in teks for nar in narasi):
            sleep(2)
            await event.respond('/homesx')
            return
          
        if any(nca in teks for nca in ncasino):
            sleep(2)
            await event.respond(judi)
            return
          
        if "Rumah Kosong Warga" in teks:
            tmp = 0
            maling = [x for x in teks.split() if '/curibarang' in x]
            sleep(1.8)
            await event.respond(maling[tmp])
            return
          
        if any(nlan in teks for nlan in nlanjut):
            tmp += 1
            await lanjut(tmp, event, hapus)
            return
    
        if "Kamu berhasil mencuri" in teks:
            total += 40
            print('Skill = ', total)
            await lanjut(tmp, event, hapus)
                
        if 'Bagus!!' in teks or 'Uuuh rasanya enak' in teks:
            sleep(1.8)
            await event.respond(result)
            return
            
        if  'Selesaikan permainan' in teks or 'Tidak ada harga buronan' in teks:
            sleep(1.8)
            await event.respond(result)
            return
            
        if 'Kamu terkurung' in teks:
            sleep(1.8)
            await event.respond('/release_denganKartu')
            return
        
        if 'Berhasil memasak' in teks:
            sleep(1.8)
            await event.respond(masak)
            return
            
        if 'Apa kamu yakin' in teks:
            sleep(1.8)
            await event.click(text="Confirm")
            return
          
        if 'Kamu tidak memiliki cukup energi' in teks:
            sleep(1.8)
            await event.respond("/restore_max_confirm")
            return

    client.start()
    print(time.asctime(), '-', 'Start')
    client.loop.create_task(mancingddh(client,245))
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stop')