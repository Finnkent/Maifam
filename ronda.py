import asyncio
from telethon import TelegramClient, events

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
session_name = 'Helio'

addresses = [
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
'/curiuang_181988138717',
'/curiuang_111965147433',
'/curiuang_360996181946',
'/curiuang_640653083028',
'/curiuang_360099039056',
'/curiuang_970811486725',
'/curiuang_321037104938',
'/curiUang_391257263751',
]

current_address_index = 0

async def handle_event(event):
    global current_address_index

    if 'berhasil mencuri' in event.raw_text:
        current_address_index += 1
        await event.respond(addresses[current_address_index])
    elif 'Alamat yang sama' in event.raw_text:
        current_address_index += 1
        await event.respond(addresses[current_address_index])
    elif 'Keamanan rumah' in event.raw_text:
        current_address_index += 1
        await event.respond(addresses[current_address_index])
    elif 'Rumah yang kamu kunjungi' in event.raw_text:
        current_address_index += 1
        await event.respond(addresses[current_address_index])

    if current_address_index == len(addresses) - 1:
        current_address_index = 0
        print('Selesai Semua')
        await event.respond(addresses[current_address_index])
    else:
        current_address_index += 1
        await event.respond(addresses[current_address_index])

async def main():
    async with TelegramClient(session_name, api_id, api_hash) as client:
        while True:
            await client.send_message('KampungMaifamxBot', addresses[0])
            client.add_event_handler(handle_event, events.NewMessage(from_users='KampungMaifamxBot'))
            await asyncio.sleep(2)  # Adjust the sleep time as needed

loop = asyncio.get_event_loop()
loop.run_until_complete(main())