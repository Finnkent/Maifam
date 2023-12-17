import time, asyncio, sys, random
from telethon import TelegramClient

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = 'Ladophi'

alamat = [
    '391257263751',
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
    '352114283538',
    '292374509522',
    '911551304540',
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
    '941298225021',
    '641932423025',
]

bot = 'kampungmaifamxbot'
hapus = '/makan_KudapanSuci'
turu = 3
batch_size = 39

async def send_address_messages():
    client = TelegramClient(sesi_file, api_id, api_hash)
    await client.start()

    while True:  # Add an infinite loop to repeat the process
        for i in range(0, len(alamat), batch_size):
            batch = alamat[i:i+batch_size]
            progress_count = 0

            for address in batch:
                message = f"/curiUang_{address}"
                await client.send_message(bot, message)
                print(f"Sent address: {address}")
                await asyncio.sleep(turu)
                progress_count += 1

            print("Removing Bounty")
            await client.send_message(bot, hapus)
            time.sleep(2)
            print("All addresses sent in this batch. Waiting...")


            for remaining in range(2):
                print(f"Waiting: {remaining} seconds")
                await asyncio.sleep(1)

            print(f"Processed {progress_count} addresses in this batch.")
        
            
        print("All addresses sent. Restarting from the beginning.")

    await client.disconnect()

asyncio.run(send_address_messages())