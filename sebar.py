import time
import asyncio
from telethon.sync import TelegramClient, events, utils, Button

# Ganti dengan informasi akun Telegram Anda
api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = 'Heliopausa'

group_list = [
    #'BIO_RPP_1',
    #'BIO_RPPO1',
    #'BIO_RPPO2',
    'BIO_RPP_30',
    #'bio_lpm_rpps',
]

message = """
==============================
🏴‍☠️ GrandPiratesBot 🏴‍☠️
==============================

Hallo Nakama!! Game One Piece sekarang tersedia di Telegram!! Mainkan dan bentuk kelompok bajak laut terkuat selautan!!

Gunakan link : https://t.me/GrandPiratesBot?start=6112502967

Ikuti arahan lalu kirim 

/claim_KINGOFTHEKING
/claim_NINENINECPNINE
/claim_TWOTWOWAYO
/claim_JUSTICEOVERALL
/claim_ROOKIEONTHEWAY
/claim_STRONGESTMANINTHEWORLD
/claim_FIVE
/claim_ONE2THREE
/claim_CONTESTANTNO556
/claim_6ERMA66

=======================

/claim_SEAOFPIRATES (waktu udah masuk grandline) 
/claim_OTWGRANDLINE (minimal sudah sampai di loguetown) 

Kirim ke bot satu persatu untuk mendapatkan kru tambahan

==============================
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
            await asyncio.sleep(2)

asyncio.run(send_message_to_groups())