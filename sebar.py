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
]

message = """
LPM BEBAS SPAM!!!
https://t.me/+n4vEO3h3ZI1iMGU1
https://t.me/+n4vEO3h3ZI1iMGU1

BEBAS PROMOTE
BANTU RAMEIN
https://t.me/+n4vEO3h3ZI1iMGU1
https://t.me/+n4vEO3h3ZI1iMGU1

NEED ALL? GF BF DLL
https://t.me/+n4vEO3h3ZI1iMGU1
https://t.me/+n4vEO3h3ZI1iMGU1

JUALAN? BOLEH!
https://t.me/+n4vEO3h3ZI1iMGU1
https://t.me/+n4vEO3h3ZI1iMGU1
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