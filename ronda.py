import time
import asyncio
import sys
import threading
import telethon
import re
from telethon import TelegramClient, events, utils
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_fil = 'Helio'

alamat = [
'/curiuang_940776279704',
'/curiuang_571820288844',
'/curiuang_331251158135',
'/curiuang_670639242838',
'/curiuang_421325453322',
'/curiuang_260960577212',
'/curiuang_851156114456',
'/curiuang_560668137555',
'/curiuang_571840135711',
'/curiuang_581357305752',
'/curiuang_480577138034',
'/curiuang_421325453322',
'/curiuang_111965147433',
'/curiuang_360996181946',
'/curiuang_640653083028',
'/curiuang_661284389931',
'/curiuang_360099039056',
'/curiuang_970811486725',
'/curiuang_321037104938',
'/curiUang_391257263751',
'/makan_kudapansuci',
'/levelupguild',
]

Grade = [
'',]

mese = '/masak_minibacon_220'
thebot = "KampungMaifamxBot"
mer = 0

def Maling():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with TelegramClient(sesi_fil, api_id, api_hash, loop=loop) as clien:
        clien.loop.run_until_complete(clien.send_message('KampungMaifamxBot', mese))

        @clien.on(events.NewMessage(from_users='KampungMaifamxBot'))
        async def handler(event):
            global mer
            global idMer
            global gradenum

            if "Berhasil memasak" in event.raw_text:
                time.sleep(2)
                await event.respond(mese)
                return

            if "Energi tidak mencukupi" in event.raw_text:
                time.sleep(2)
                await event.respond('restore')
                return

            if "Energi berhasil" in event.raw_text:
                time.sleep(2)
                await event.respond(mese)
                return

            if "Tidak cukup bahan" in event.raw_text:
                time.sleep(2)
                await event.respond('/dapur_restock_MAX_confirm')
                return

            if "Bahan-bahan direstock" in event.raw_text:
                time.sleep(2)
                await event.respond(mese)
                return

            if "Kamu tidak bisa memasak" in event.raw_text:
                mer += 0
                time.sleep(2)
                await event.respond(''+alamat[mer])
                return

            if "berhasil mencuri" in event.raw_text:
                mer += 1
                time.sleep(2)
                await event.respond(''+alamat[mer])
                return

            if "Alamat yang sama" in event.raw_text:
                mer += 1
                time.sleep(2)
                await event.respond(''+alamat[mer])
                return

            if "Keamanan rumah" in event.raw_text:
                mer += 1
                time.sleep(2)
                await event.respond(''+alamat[mer])
                return

            if "Rumah yang kamu kunjungi" in event.raw_text:
                mer += 1
                time.sleep(2)
                await event.respond(''+alamat[mer])
                return

            if "Uuuh rasanya" in event.raw_text:
                time.sleep(2)
                mer += 1
                await event.respond(mese)
                return

            if alamat[mer] == alamat[-1]:
                mer = 0
                print('Selesai Semua')
                time.sleep(3)
                await event.respond(''+alamat[mer])
                return
            else:
                time.sleep(2)
                mer += 0
                await event.respond(''==alamat[mer])
            
        clien.run_until_disconnected()
        print(time.asctime(), '-', 'Stop')

threading.Thread(target=Maling).start()
print(time.asctime(), '-', 'Start')

#if abis == 2 :
#    client.disconnect()
#    clien.disconnect()
