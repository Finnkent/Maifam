import time
import asyncio
from telethon.sync import TelegramClient, events, utils, Button

# Ganti dengan informasi akun Telegram Anda
api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = 'Xeroz'

group_list = [
    'BIO_RPP_30',
    'bio_lpm_rpps',
    'BIORPP55',
    'BIORPP4_S2',
    'BIO_RPPO2',
]

message = """
**JOIN LPM 76**
https://t.me/+YR8Di7zB4uFiY2Y1
https://t.me/+YR8Di7zB4uFiY2Y1

**BEBAS NO TIMER**
https://t.me/+YR8Di7zB4uFiY2Y1
https://t.me/+YR8Di7zB4uFiY2Y1

**ADA YANG LAGI BAGI UPSUBS GRATIS!!! LANGSUNG JOIN DAN CEK PESAN TERSEMAT**
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
            await asyncio.sleep(120)

asyncio.run(send_message_to_groups())