import re, time, asyncio, sys, random
from telethon import TelegramClient, events, utils, Button

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = 'Finnkentz'

#bot_id = "kampungmaifamxbot"
bot_id = -1001654288969

with TelegramClient(sesi_file, api_id, api_hash) as client:
        @client.on(events.NewMessage(from_users=bot_id))
        async def handler(event):
            pesan = event.raw_text
            
            if "🔤 Kata baru" in pesan:
                print(time.asctime(), 'Kata Baru Muncul')
                kata_match = re.findall(r'🔤 Kata: (.+)', pesan)
                if kata_match:
                    kata = kata_match[0]
                    await event.respond(kata)
                    
client.start()
print(time.asctime(), '-', 'Started')
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')
