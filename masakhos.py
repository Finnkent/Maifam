import time
import asyncio

from telethon.sync import TelegramClient
from telethon import events

from tqdm import tqdm

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'

punyaku = [
    'Cibu',
    'Eunji',
    'Fainry',
    'Blu',
    'Genya',
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
                        await asyncio.sleep(2)
                        await event.respond('/restore_max_confirm')
                        
                    if 'Energi berhasil' in pesan:
                        await asyncio.sleep(2)
                        await event.respond(masak)
                        
                    if 'Kamu tidak bisa memasak' in pesan or 'Tidak cukup bahan' in pesan:
                        await asyncio.sleep(1)
                        await client.disconnect()
                        close()
                
                await client.run_until_disconnected()
            print(aaa, '- Complete -', time.asctime())
        saat_ini = time.localtime()
        menit_sekarang = saat_ini.tm_min
        detik_sekarang = saat_ini.tm_sec
        detik_yang_harus_ditunggu = (60 - menit_sekarang) * 60 - detik_sekarang
        
        for remaining in tqdm(range(detik_yang_harus_ditunggu), desc=f"Waiting until 00:00 ({menit_sekarang}:{detik_sekarang})"):
            await asyncio.sleep(1)

def tunggu_hingga_menit_detik_00():
    saat_ini = time.localtime()
    menit_sekarang = saat_ini.tm_min
    detik_sekarang = saat_ini.tm_sec
    
    if menit_sekarang == 0 and detik_sekarang == 0:
        return  # Sudah 00:00, tidak perlu menunggu
    
    detik_yang_harus_ditunggu = (60 - menit_sekarang) * 60 - detik_sekarang
    print(f"Menunggu hingga 00:00.")
    time.sleep(detik_yang_harus_ditunggu)

# Menjalankan kode secara langsung tanpa if __name__ == "__main__"
tunggu_hingga_menit_detik_00()
loop = asyncio.get_event_loop()
loop.run_until_complete(my_function())