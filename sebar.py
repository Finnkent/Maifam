import time
import asyncio
from telethon.sync import TelegramClient, events, utils, Button

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = 'Finnkent'

group_list = [
    'BIO_RPP_30',
    'bio_lpm_rpps',
    'BIORPP55',
    'BIORPP4_S2',
]

message = """
**GW TAU LU SEMUA GABUT BANGET
SINI MENDING COBAIN BOT GAME ONE PIECE**

[GAS COBAIN GAS COBAIN GAS COBAIN](https://t.me/GrandPiratesBot?start=5199147926)

**MAU LANGSUNG DAPAT BANYAK KRU???
LANGSUNG AJA**

[SINI SINI SINI SINI SINI SINI](https://t.me/GrandPiratesGroup/124810)

"""

async def send_message_to_groups():
    async with TelegramClient(sesi_file, api_id, api_hash) as client:
        print(time.asctime(), "- Userbot Started")
        while True:
            for group_username in group_list:
                try:
                    await client.send_message(group_username, message, link_preview=False)
                    print(f"Pesan berhasil dikirim ke {group_username}")
                except Exception as e:
                    print(f"Terjadi kesalahan saat mengirim pesan ke {group_username}: {e}")
                await asyncio.sleep(2)
            await asyncio.sleep(30)

asyncio.run(send_message_to_groups())