import asyncio
from telethon import TelegramClient

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
client = TelegramClient('Finnkent', api_id, api_hash)
chat ='kampungmaifamxbot'

async def main():
    async with client:
        while True:
            await client.send_message(chat,'⛏⛏⛏⛏⛏')
            await asyncio.sleep(2)
        

client.loop.run_until_complete(main())