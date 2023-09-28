import time
import asyncio
import datetime
from tqdm import tqdm
from telethon import TelegramClient, events
from rich.progress import Progress

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = 'Helio'

alamat = [
    '391257263751',
    '262316242208',
    '341543332554',
    '471584354122',
    '800947317803',
    '910967339315',
    '710915339722',
    '850980337629',
    '340944332535',
    '310934331546',
    '310922331452',
    '920935336658',
    '370988345304',
    '240998347711',
    '800934347619',
    '740940349826',
    '121076542903',
    '961089537415',
    '831074529440',
    '191065513457',
    '172118295136',
    '352114283538',
    '292374509522',
    '911551304540',
    '501530319712',
    '172118295136',
    '531553312557',
    '891589326537',
    '940776279704',
    '571820288844',
    '331251158135',
    '670639242838',
    '421325453322',
    '260960577212',
    '851156114456',
    '560668137555',
    '571840135711',
    '581357305752',
    '480577138034',
    '181988138717',
    '111965147433',
    '360996181946',
    '640653083028',
    '360099039056',
    '970811486725',
    '321037104938',
    '391257263751',
]

bot = 'kampungmaifamxbot'
hapus = 'Hapus menggunakan Uang'
turu = 3

async def send_address_messages():
    client = TelegramClient(sesi_file, api_id, api_hash)
    await client.start()

    while True:
        progress = tqdm(total=len(alamat), desc="Sending addresses")

        for i, address in enumerate(alamat):
            message = f"/curiUang_{address}"
            await client.send_message(bot, message)
            print(f"Sent address: {address}")
            await asyncio.sleep(turu)
            progress.update(1)
            
            # Setelah mengirim dua alamat, hapus buronan
            if (i + 1) % 47 == 0:
                await asyncio.sleep(turu)
                await client.send_message(bot, hapus)
                print("Remove Bounty")

        progress.close()

        print("All addresses sent. Waiting 1 hour...")
        for remaining in tqdm(range(3300, desc="Waiting")):
            await asyncio.sleep(1)

    await client.disconnect()

asyncio.run(send_address_messages())