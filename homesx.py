from telethon import TelegramClient, events, sync, utils
from time import sleep
import asyncio, random

loop = asyncio.get_event_loop()

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'

akun1 = input("Akun : ")
client = TelegramClient(akun1, api_id, api_hash).start()

total = 0
judi = '/casino_FiftyFifty_2_1e12'
chat = 'kampungmaifamxbot'
hapus = 'Hapus menggunakan Uang'
result = '/casino_result'

narasi = {
    "No bounty",
    "Successfully bet",
    "You can see",
    "EXP Target is reached",
    "as free as",
    "Address code changed",
    "Energy Successfully restored",
    "Language changed to English",
}

ncasino = {
    "You won",
    "No bet placed",
    "You bet on",
    "60 times",
}

@client.on(events.NewMessage(chat))
async def handler(event):
    global maling
    global total 
    global tmp
    
    teks = event.text
    

    if any(nar in teks for nar in narasi):
        sleep(2)
        await event.respond('/homesx')
        return
      
    if any(nca in teks for nca in ncasino):
        sleep(2)
        await event.respond(judi)
        return

    if "Villager's Abandoned" in teks:
        tmp = 0
        rem = 0
        maling = [x for x in teks.split() if '/stealitem' in x]
        sleep(1.8)
        await event.respond(maling[tmp])
        return
        
    if "The house you are trying to" in event.raw_text:
        sleep(1.8)
        tmp +=1
        total += 40
        print('Skill = ', total)
        
        if tmp == 5:
            await event.respond(hapus)
            return 
        if tmp == 5:
            await event.respond(hapus)
            return 
        else:
            await client.send_message(chat, maling[tmp])
            return
        return
        
    if "ve stolen" in event.raw_text:
        sleep(1.8)
        tmp +=1
        total += 40
        print('Skill = ', total)
        
        if tmp == 5:
            await event.respond(hapus)
            return
        if tmp == 5:
            await event.respond(hapus)
            return 
        else:
            await client.send_message(chat, maling[tmp])
            return
        return
            
      
    if 'Oh snap' in teks:
        sleep(1.8)
        tmp += 1
        
        if tmp == 5:
            await event.respond(hapus)
            return
        if tmp == 5:
            await event.respond(hapus)
            return 
        else:
            await client.send_message(chat, maling[tmp])
            return
        return
        
    if 'has no item to steal' in teks:
        sleep(1.8)
        tmp += 1
        
        if tmp == 5:
            await event.respond(hapus)
            return
        if tmp == 5:
            await event.respond(hapus)
            return 
        else:
            await client.send_message(chat, maling[tmp])
            return
        return
    
    if 'The house you visited' in teks:
        sleep(1.8)
        tmp += 1
        if tmp == 5:
            await event.respond(hapus)
            return
        if tmp == 5:
            await event.respond(hapus)
            return 
        else:
            await client.send_message(chat, maling[tmp])
            return
        return

    if 'Same address' in teks:
        sleep(1.8)
        tmp += 1
        
        if tmp == 5:
            await event.respond(hapus)
            return
        if tmp == 5:
            await event.respond(hapus)
            return 
        else:
            await client.send_message(chat, maling[tmp])
            return
        
        return
    
    if 'Great!!' in teks or 'Yummy mummy it' in teks or 'End previous game' in teks:
        sleep(1.8)
        await event.respond(result)
        return
      
    if 'stuck in bloody' in teks:
        sleep(1.8)
        await event.respond('/release')
        return
    
    if 'Successfully cooked' in teks:
        sleep(1.8)
        await event.respond('/masak_minibacon_220')
        return
        
    if 'Are you sure' in teks:
        sleep(1.8)
        await event.click(text="Confirm")
        return
      
    if 'Your energy is too low' in teks:
        sleep(1.8)
        await event.respond("/restore_max_confirm")
        return

client.send_message(chat,'/homesx')
client.run_until_disconnected()
