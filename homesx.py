from telethon import TelegramClient, events, sync, utils
from time import sleep
from datetime import datetime
import asyncio, random


loop = asyncio.get_event_loop()

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'

akun1 = input("Akun : ")
client = TelegramClient(akun1, api_id, api_hash).start()

total = 0
judi = '/casino_FiftyFifty_2_1e12'
chat = 'kampungmaifamxbot'
hapus = '/makan_KudapanSuci'
result = '/casino_result'
cmd = '/th_SlotMachine_SevenFish'
cmd1 = '/th_SlotMachine_add'
chatx4 = 'KampungMaifamX4Bot'
me = 'Finnkent'
invest = '/invest_Helikopter_beli_100'
ch = 'inMaifam'

jackpot = 0
gems = 0
tiket = 0 
poin = 0
skill = 0
cv = 0
sk = 0


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

def deteksi_pukul_20_00():
    # Dapatkan waktu saat ini
    sekarang = datetime.now()

    # Ambil jam, menit, dan detik saat ini
    jam = sekarang.hour
    menit = sekarang.minute
    detik = sekarang.second

    if jam == 7 and menit == 15 and detik == 0:
        return True
    else:
        return False

# Panggil fungsi untuk mendeteksi
slot_20_00 = deteksi_pukul_20_00()

@client.on(events.NewMessage(chat))
async def handler(event):
    global maling
    global total 
    global tmp
    
    teks = event.text
    
    if slot_20_00:
        time.sleep(2)
        await client.send_message(chatx4, 'Bahasa Indonesia')
        return
    
    if any(nar in teks for nar in narasi):
        time.sleep(2)
        await event.respond('/homesx')
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
            
    
      
    if 'Yummy mummy it' in teks:
        sleep(1.8)
        await event.respond(result)
        #print(tmp)
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
    
    if 'stuck in bloody' in teks:
        sleep(1.8)
        await event.respond('/release')
        return
        
    if 'Great!!' in teks:
        sleep(1.8)
        await event.respond(result)
        return
        
    if 'Successfully cooked' in teks:
        sleep(1.8)
        await event.respond('/masak_minibacon_220')
        return
        
    if '60 times' in event.raw_text:
        sleep(1.8)
        await event.respond(judi)
        return
        
    if "End previous game" in teks:
        sleep(1.8)
        await event.respond(result)
        return
        
       
    if "You bet on" in teks:
        sleep(1.8)
        await event.respond(judi)
        return
        
    if "No bet placed" in teks:
        sleep(1.8)
        await event.respond(judi)
        return
        
    if "You won" in teks:
        sleep(1.8)
        await event.respond(judi)
        return
        
    if 'Are you sure' in teks:
        sleep(1.8)
        await event.click(text="Confirm")
        return
      
    if 'Your energy is too low' in teks:
        sleep(1.8)
        await event.respond("/restore_max_confirm")
        return

@client.on(events.NewMessage(chatx4))
async def handler(event):
    global jackpot
    global gems
    global tiket
    global poin 
    global skill
    global cv
    global sk
    
    me = await client.get_me()
    
    dn = me.first_name
    usn = me.username
    
    if 'Bahasa diubah ke Bahasa Indonesia' in event.raw_text:
        time.sleep(2)
        await client.send_message(chatx4, cmd)
        print('Mulai Slot')
        return
    
    if '10000000Qn' in event.raw_text:
        time.sleep(2)
        await event.respond('/tamanHiburan_TembakTopeng')
        print('Mulai Dart')
        return
    
    if 'kemampuan+1' in event.raw_text:
        sk += 1
    
    if 'PoinSlot' in event.raw_text:
        poin_match = re.search(r'(\d+)\s*PoinSlot', event.raw_text)
        if poin_match:
           poin += int(poin_match.group(1))

    if 'PoinJackpot' in event.raw_text:
        jackpot_match = re.search(r'(\d+)\s*PoinJackpot', event.raw_text)
        if jackpot_match:
           jackpot += int(jackpot_match.group(1))

    if '💎' in event.raw_text:
       gems_match = re.search(r'(\d+)\s*💎', event.raw_text)
       if gems_match:
          gems += int(gems_match.group(1))

    if '🎫Tiket' in event.raw_text:
        tiket_match = re.search(r'(\d+)\s*🎫Tiket', event.raw_text)
        if tiket_match:
           tiket += int(tiket_match.group(1))

    if 'KemampuanMemancing' in event.raw_text:
        skill_match = re.search(r'(\d+)\s*KemampuanMemancing', event.raw_text)
        if skill_match:
           skill += int(skill_match.group(1))


    if '🏵' in event.raw_text:
        cv_match = re.search(r'(\d+)\s*🏵', event.raw_text)
        if cv_match:
           cv += int(cv_match.group(1))
        
    elif 'Ada tujuh jenis ikan' in event.raw_text:
        time.sleep(2)
        await event.click(1,0)
        return

    
    elif 'Kamu memutar SlotMachine 10x' in event.raw_text:
        time.sleep(2)
        await event.click(1,0)
        return
    
    elif 'Koin untuk' in event.raw_text:
        time.sleep(2)
        await event.respond(cmd1)
        return
        
    
    
    elif 'Apa kamu' in event.raw_text:
        time.sleep(2)
        await event.click(text="Confirm")
        return
    
    elif 'Berhasil membeli tambahan' in event.raw_text:
        time.sleep(2)
        await event.respond(cmd)
        return
    
    elif 'Setiap harinya' in event.raw_text:
        time.sleep(2)
        await event.click(text='Mulai')
        return

    elif 'Pilih sasaran' in event.raw_text:
        time.sleep(2)
        await event.click(0,1)
        return
    
    elif 'Lemparanmu berhasil' in event.raw_text:
        time.sleep(2)
        await event.click(text='Lanjut')
        return
    
    elif 'Sayang sekali' in event.raw_text:
        time.sleep(2)
        await event.click(text='Lanjut')
        return
      

    elif 'Kesempatan untuk melempar' in event.raw_text or 'dibuka setiap hari' in event.raw_text:
        
        finalresult = """

🎰 <b>Final Slot Result:</b> {} - @{}

- 🌟 <b>PoinJackpot:</b> <i>+{}</i>
- 💎 <b>Gems:</b> <i>+{}</i>
- 🎫 <b>Tiket:</b> <i>+{}</i>
- 🎖 <b>PoinSlot:</b> <i>+{}</i>
- 🐟 <b>Skill:</b> <i>+{}</i>
- 🏵 <b>CarnivalPoin:</b> <i>+{}</i>
- 🎯 <b>DartSkill:</b> <i>+{}</i>

⏰: <code>{}</code>
"""
        
        time.sleep(2)
        await event.respond(invest)
        time.sleep(2)
        await client.send_message(ch, ''
        + str(finalresult).format(dn,usn,jackpot, gems, tiket, poin, skill, cv, sk, time.asctime()) + '',parse_mode='html')
        return
        
    
    elif 'investasi termahal' in event.raw_text or 'Tiap petani hanya bisa' in event.raw_text or 'Saldo WorldBank tidak mencukupi' in event.raw_text:
        time.sleep(2)
        print('--Selesai--')
        await client.send_message(chat, 'English')
        return
   
client.send_message(chat,'/homesx')

client.run_until_disconnected()
