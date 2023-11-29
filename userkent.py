import time
import asyncio
import sys
import random
import datetime
import os
import re
import logging
from telethon.sync import TelegramClient, events, utils, Button

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = 'Finnkent'

gbk = '/gbk_jelajah'
restore = '/restore_max_confirm'
bot_id = "KampungMaifamXBot"
#user = 5199147926
krj = '/gbk_keranjang'
tsk = '/gbk_Task'
tskg = '/gbk_task_G'

narasi_gbk = {
    "memang melelahkan",
    "Gunung ini terlihat tenang",
    "Semangat, perjalanan panjang",
    "Saat ini kamu masih berada",
    "Hal-hal ajaib yang ada",
    "Sudah mulai lelah?",
    "Ada banyak lokasi-lokasi",
    "menemukan sebuah"
}

narasi_1 = "Tempat ini dipenuhi tupai" 
narasi_2 = "Dulu sekali seorang petani tinggal" 
narasi_3 = "Di sini tidak benar-benar ada kelinci" 
narasi_4 = "Keberadaan tumbuhan-tumbuhan beracun" 
narasi_5 = "di sini mayoritas berwarna merah" 
narasi_6 = "Ikan-ikan kecil hidup di sini" 
narasi_7 = "Gua kecil di bagian dasar Gunung" 
narasi_8 = "di sini terdapat berbagai macam burung"
narasi_9 = "Taman bunga matahari di kaki Gunung"

area_tupai = {
    "BerryBiasa[A]", "BerryBiasa[B]", "BerryBiasa[C]", "BerryBiasa[D]", "BerryLiar[B]", "BerryLiar[C]", "KacangOak", "KacangOak[A]", "KacangOak[B]", "KacangOak[C]", "KacangOak[D]", "KacangOak[E]", "Pisang", "Pisang[A]", "Pisang[B]", "Pisang[C]", "Pisang[D]", "Pisang[E]"
}

kebun_terbengkalai = {
    "Apel[A]", "Apel[B]", "Apel[C]", "Apel[D]", "Apel[E]", "BerryBiasa", "BerryBiasa[E]", "BerryLiar", "BerryLiar[D]", "BerryLiar[E]", "JamurBiasa", "JamurBiasa[C]", "JamurBiasa[D]", "JamurBiasa[E]", "Tomat", "Tomat[A]", "Tomat[B]", "Tomat[C]", "Tomat[D]", "Tomat[E]", "Tomat[S]"
}

lubang_kelinci_raksasa = {
    "KacangTanah", "KacangTanah[A]", "KacangTanah[B]", "KacangTanah[C]", "KacangTanah[D]", "KacangTanah[E]", "KacangTanah[S]", "Kentang", "Kentang[A]", "Kentang[B]", "Kentang[C]", "Kentang[D]", "Kentang[E]", "Kentang[S]", "Mentimun", "Mentimun[A]", "Mentimun[B]", "Mentimun[C]", "Mentimun[D]", "Mentimun[E]", "Mentimun[S]", "Wortel", "Wortel[A]", "Wortel[B]", "Wortel[C]", "Wortel[D]", "Wortel[E]", "Wortel[S]"
}

gua_beracun = {
    "JamurBeracun", "JamurBeracun[C]", "JamurBeracun[D]", "JamurBeracun[E]"
}

kebun_merah = {
    "Apel", "Apel[B]", "Apel[C]", "Apel[D]", "Apel[E]", "Strawberry", "Strawberry[B]", "Strawberry[C]", "Strawberry[D]", "Strawberry[E]", "Tomat", "Tomat[B]", "Tomat[C]", "Tomat[D]", "Tomat[E]"
}

kolam_kecil = {
    "GuramiKecil", "GuramiKecil[C]", "GuramiKecil[D]", "GuramiKecil[E]", "KoiKecil", "MujairKecil", "MujairKecil[C]", "MujairKecil[D]", "MujairKecil[E]"
}

gua_gibi = {
    "Batu", "BatuBara", "BatuBara[D]", "BatuBara[E]", "Batu[D]", "Batu[E]", "BatuKerikil", "BatuKerikil[D]", "BatuKerikil[E]", "Nikel", "Nikel[D]", "Nikel[E]"
}

surga_burung = {
    "Apel[A]", "Apel[B]", "Apel[S]", "Avokad[A]", "Avokad[B]", "Avokad[S]", "Pisang[A]", "Pisang[B]", "Pisang[S]", "TelurBurungHantu", "TelurBurungUnta", "TelurElang", "TelurGagak", "TelurKakakTua", "TelurMerak", "TelurPhoenix", "TelurPuyuh"
}

taman_matahari = {
    "BungaMatahari", "BungaMatahari[A]", "BungaMatahari[B]", "BungaMatahari[C]", "BungaMatahari[D]", "BungaMatahari[E]", "BungaMatahari[S]", "BungaMatahari[SS]", "BungaMatahari[SSS]"
}

jalan = narasi_gbk

ongoing_tasks = []

emoji_list = ['🍎','🍓', '🌰', '🍅', '🥜', '▪️', '🍌', '🍄'] #Daftar emoji yang mungkin muncul

jumlah = 0
misi = []
narasi = []
tugas = []
klem = []
jenis_tugas = []
grup = -1001946930100
ch = 'inMaifam'

total = 0
judi = '/casino_FiftyFifty_2_1e12'
chat = 'kampungmaifamxbot'
hapus = '/makan_KudapanSuci'
result = '/casino_result'
curi = '/homesx'

cmd = '/th_SlotMachine_SevenFish'
cmd1 = '/th_SlotMachine_add'
bot = 'KampungMaifamX4Bot'
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
fp = 0 
mm = 0 
hw = 0 
af = 0 
bd = 0
cc = 0
md = 0
mp = 0

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

area = ""
slot = ""

slots_dict = {
    'Ikan': '/th_SlotMachine_SevenFish',
    'Daun': '/th_SlotMachine_SixLeaves',
}

client = TelegramClient(sesi_file, api_id, api_hash)

mepam = "KampungMaifamBot"
mepamx = "KampungMaifamXBot"
mepamx4 = "KampungMaifamX4Bot"


respond_to_group = False

user = 5199147926

async def bentar(w):
    await asyncio.sleep(w)
    
def stop_sesi():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
    
@client.on(events.NewMessage(from_users=mepam))
async def handler_maifam(event):
    global respond_to_group
    global misi, jumlah, tugas, klem, narasi, jenis_tugas
    if not respond_to_group:
       return
    
    pesan = event.raw_text
    
    if "Selesaikan tugas-tugas" in pesan:
        if "Tidak ada tugas" in pesan:
            print("Tidak ada tugas yang sedang diambil. Menanggapi dengan tugas baru.")
            time.sleep(2)
            await event.respond(tskg)
        if "Ongoing Task" in pesan:
            print("Kondisi Ongoing Task terpenuhi.")
            jenis_tugas = None
            narasi = None
            for emoji in emoji_list:
                if emoji in pesan:
                    jenis_tugas = pesan.split(emoji, 1)[1].split()[0]
                    tgs = pesan.splitlines()[12].split()
                    tugas = str(tgs[0]+tgs[1])
                    klem = int(pesan.splitlines()[12].split('/')[1].split(')')[0])
                    jumlah = int(pesan.splitlines()[12].split('(')[1].split('/')[0])
                    break
            if jenis_tugas:
                time.sleep(2)
                await event.respond(gbk)
                if jenis_tugas in area_tupai:
                    narasi = narasi_1
                elif jenis_tugas in kebun_terbengkalai:
                    narasi = narasi_2
                elif jenis_tugas in lubang_kelinci_raksasa:
                    narasi = narasi_3
                elif jenis_tugas in gua_beracun:
                    narasi = narasi_4
                elif jenis_tugas in kebun_merah:
                    narasi = narasi_5
                elif jenis_tugas in kolam_kecil:
                    narasi = narasi_6
                elif jenis_tugas in gua_gibi:
                    narasi = narasi_7
                elif jenis_tugas in surga_burung:
                    narasi = narasi_8
                elif jenis_tugas in taman_matahari:
                    narasi = narasi_9
                else:
                    print("Jenis item tidak di temukan di dalam area")
                    time.sleep(2)
                    await event.click(1,0)
                    return
            print('-'*30+f"\nTersedia tugas\njenis_tugas = {tugas}\njumlah = {klem}x\nprogres = {jumlah}\nnarasi = {narasi}\nSelamat menyelesaikan tugas!!\n"+'-'*30)
        return
    
    if "Berikut adalah daftar Tugas" in pesan:
        misi = []
        z = [i for i in pesan.split("\n\n") if any(loc in i for loc in emoji_list)]
        for x in z:
            koin = [i for i in [i for i in x.split("\n") if "🎁 Koin:" in i][0].split()][2]
            koin_list = int(koin.replace("🪙", ""))
            print(koin)
            exp = [i for i in [i for i in x.split("\n") if "🎁 EXP:" in i][0].split()][2]
            exp_list = int(exp.replace("❇️", ""))
            print(exp)
            misi_list = [i for i in [i for i in x.split("\n") if "🗒" in i][0].split()][1]
            print(misi_list)
            print()
            misi.append({"koin_list": koin_list, "exp_list": exp_list, "misi_list": misi_list})
        #def get_koin(misi):
            #return misi.get("koin_list")
        #misi.sort(key=get_koin, reverse=True)
        def get_exp(misi):
            return misi.get("exp_list")
        misi.sort(key=get_exp, reverse=False)
        time.sleep(2)
        await event.respond(misi[0].get("misi_list"))
        return
    
    if "Berhasil mengambil tugas" in pesan:
        jenis_tugas = None
        for emoji in emoji_list:
            if emoji in pesan:
                jenis_tugas = pesan.split(emoji,1)[1].split()[0]
                break
        tugass = re.findall(r'dapatkan (\D+) sebanyak', pesan)
        klems = re.findall(r'sebanyak (\d+) kali', pesan)
        for tugas in tugass:
            tugas=str(tugass[0])
        for klem in klems:
            klem=int(klems[0])
        if jenis_tugas:
            time.sleep(2)
            await event.respond(gbk)
            if jenis_tugas in area_tupai:
                narasi = narasi_1
            elif jenis_tugas in kebun_terbengkalai:
                narasi = narasi_2
            elif jenis_tugas in lubang_kelinci_raksasa:
                narasi = narasi_3
            elif jenis_tugas in gua_beracun:
                narasi = narasi_4
            elif jenis_tugas in kebun_merah:
                narasi = narasi_5
            elif jenis_tugas in kolam_kecil:
                narasi = narasi_6
            elif jenis_tugas in gua_gibi:
                narasi = narasi_7
            elif jenis_tugas in surga_burung:
                narasi = narasi_8
            elif jenis_tugas in taman_matahari:
                narasi = narasi_9
            else:
                print("Jenis item tidak di temukan di dalam area")
                time.sleep(2)
                await event.click(1,0)
        print('-'*30+f"\nBerhasil mengambil tugas\njenis_tugas = {tugas}\njumlah = {klem}x\nprogres = {jumlah}\nnarasi = {narasi}\nSelamat menyelesaikan tugas!!\n"+'-'*30)
        return
    
    if any(loc in pesan for loc in jalan):
        time.sleep(2)
        await event.click(0,0)
        return
    
    if "Berhasil menyelesaikan tugas" in pesan:
        print('-'*30+f"\nTugas sudah di selesaikan\n"+'-'*30)
        time.sleep(2)
        await client.forward_messages(grup, event.message)
        time.sleep(5)
        await event.respond(tsk)
        return
            
    if "Gunung dipenuhi" in pesan:
        time.sleep(2)
        await event.respond(krj)
        return
      
    if "Kamu tidak memiliki cukup energi" in pesan:
        time.sleep(2)
        await event.respond(restore)
        return
    
    if "Energi berhasil dipulihkan" in pesan:
        time.sleep(2)
        await event.respond(tsk)
        return
    
    if "tidak bisa mengambil tugas" in pesan:
        time.sleep(2)
        await event.click(text="Turun")
        return
    
    if 'ingin turun gunung' in pesan:
        time.sleep(2)
        await event.click(text="Turun")
        return
      
    if "Keranjang kamu sudah penuh!!" in pesan:
        time.sleep(2)
        await event.respond(krj)
        return
    
    if "🧺 Keranjang - GunungBelakangKebun" in pesan:
        if "Silakan turun gunung terlebih dahulu" in pesan:
            time.sleep(2)
            await event.respond('/gbk')
        if "Berhasil mengirim ke barang:" in pesan:
            time.sleep(2)
            await event.respond(tsk)
        else:
            time.sleep(2)
            await event.click(0,0)
        return
    
    if 'berhasil mendapat' in pesan:
        if f'berhasil mendapat {tugas}' in pesan:
            jumlah+=1
            print(f'Progres {tugas} = {jumlah}')
            if jumlah %klem == 0:
                time.sleep(2)
                await event.respond('/gbk_task')
                jumlah = 0
            elif jumlah == 0
                time.sleep(2)
                await event.click(text="Keluar")
        else:
            time.sleep(2)
            await event.click(0,0)
        return
    
    #elif "tidak ada permata berharga" in pesan:
        #time.sleep(2)
        #await event.click(0,0)
        #return
      
    if "belum menemukan apa-apa" in pesan:
        time.sleep(2)
        await event.click(0,0)
        return
      
    elif "hanya bisa mendaki" in pesan:
        time.sleep(2)
        await event.click(0,0)
        return
       
    if '- GBK ⛰' in pesan:
        if narasi in pesan:
            print('-'*30+f"\nNarasi {narasi} ditemukan di dalam pesan\n"+'-'*30)
            time.sleep(2)
            await event.click(0,0)
            return
        else:
            time.sleep(2)
            await event.click(1,0)
            return
        return
        
        
            
@client.on(events.NewMessage(from_users=mepamx))
async def handler_mencuri(event):
    global respond_to_group
    if not respond_to_group:
       return
        
    pesan = event.raw_text

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
        
@client.on(events.NewMessage(from_users=mepamx4))
async def handler_ayam(event):
    global respond_to_group
    if not respond_to_group:
       return
    
    pesan = event.raw_text
    
    global jackpot
    global gems
    global tiket
    global poin 
    global skill
    global cv
    global sk
    global af
    global fp
    global hw
    global mm
    global bd
    global cc
    global md
    global mp
    
    me = await client.get_me()
    
    dn = me.first_name
    usn = me.username
            
              
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
           
    if 'Kamu memperoleh: 🧌ActionFigure' in event.raw_text:
        af += 1
        
    if 'Kamu memperoleh: 🏎HotWheels' in event.raw_text:
        hw += 1
        
    if 'Kamu memperoleh: 👾FunkoPop' in event.raw_text:
        fp += 1
        
    if 'Kamu memperoleh: 🤖MechaModel' in event.raw_text:
        mm += 1
        
    if 'Kamu memperoleh: 👱‍♀️BarbieDoll' in event.raw_text:
        bd += 1
        
    if 'Kamu memperoleh: 📕ClassicalComic' in event.raw_text:
        cc += 1
        
    if 'Kamu memperoleh: 🏎Mini4WD' in event.raw_text:
        md += 1
        
    if 'Kamu memperoleh: 🦄MyLittlePony' in event.raw_text:
        mp += 1
        
        
    elif 'Ada tujuh jenis ikan' in event.raw_text:
        time.sleep(2)
        await event.click(1,0)
        return
    
    elif 'Ada enam jenis daun' in event.raw_text:
        if 'Gunakan gelar SlotKing' in event.raw_text:
            time.sleep(2)
            await event.respond('/addtitle_SlotKing')
        else: 
            time.sleep(2)
            await event.click(1,0)
        return
      
    elif 'Berhasil menambahkan gelar' in event.raw_text:
        time.sleep(2)
        if slot in slots_dict:
            await event.respond(slots_dict[slot])
        return
                
    elif 'Kamu memutar SlotMachine 10x' in event.raw_text:
        time.sleep(2)
        await event.click(1,0)
        return
    
    elif 'Koin untuk' in event.raw_text:
        if slot in slots_dict:
            await event.respond(slots_dict[slot])
            return
        else:
            time.sleep(2)
            await event.respond("/collectibleFragment_SixLeaves")
            return
    
    elif 'CollectibleFragment SixLeaves untuk memperoleh' in event.raw_text:
        time.sleep(2)
        await event.click(text="Get CollectibleItem")
        time.sleep(2)
        if slot in slots_dict:
            await event.respond(slots_dict[slot])
        return
    
    elif 'Apa kamu' in event.raw_text:
        time.sleep(2)
        await event.click(text="Confirm")
        return
    
    elif 'Berhasil membeli tambahan' in event.raw_text:
        time.sleep(2)
        if slot in slots_dict:
            await event.respond(slots_dict[slot])
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
        for slot in slots_dict:
            if slot == 'Daun':
                cmd = slots_dict[slot]
            elif slot == 'Ikan':
                cmd = slots_dict[slot]
        finalresult = """

🎰 <b>Final Slot Result:</b> {} - @{}

- 🌟 <b>PoinJackpot:</b> <i>+{}</i>
- 💎 <b>Gems:</b> <i>+{}</i>
- 🎫 <b>Tiket:</b> <i>+{}</i>
- 🎖 <b>PoinSlot:</b> <i>+{}</i>
- 🐟 <b>Skill:</b> <i>+{}</i>
- 🏵 <b>CarnivalPoin:</b> <i>+{}</i>
- 🎯 <b>DartSkill:</b> <i>+{}</i>
- 🧌 <b>Action Figure:</b> <i>+{}</i>
- 🤖 <b>Mecha Model:</b> <i>+{}</i>
- 👾 <b>Funko Pop:</b> <i>+{}</i>
- 🏎 <b>Hot Wheels:</b> <i>+{}</i>
- 👱‍♀️ <b>BarbieDoll:</b> <i>+{}</i>
- 📕 <b>ClassicalComic:</b> <i>+{}</i>
- 🏎 <b>Mini4WD:</b> <i>+{}</i>
- 🦄 <b>MyLittlePony:</b> <i>+{}</i>

🎮 <b>Mode:</b> <code>{}</code> 
⏰: <code>{}</code>
"""
        
        time.sleep(2)
        await event.respond(invest)
        time.sleep(2)
        await client.send_message(ch, ''
        + str(finalresult).format(dn,usn,jackpot, gems, tiket, poin, skill, cv, sk, af, mm, fp, hw, bd, cc, md, mp, slot, time.asctime()) + '',parse_mode='html')
        return
        
    
    elif 'investasi termahal' in event.raw_text or 'Tiap petani hanya bisa' in event.raw_text or 'Saldo WorldBank tidak mencukupi' in event.raw_text:
        time.sleep(2)
        print('--Selesai--')
         
        
@client.on(events.NewMessage(from_users=user))
async def handler_user(event):
    global respond_to_group
    pesan = event.raw_text
    
    if '/ceklist' in pesan:
        await asyncio.sleep(2)
        pesan_list = """Daftar perintah :
        
cmd :
!slot_mode (X4)
!gasmaling (X)
!gasnanjak (alpha)
!stop_makro (untuk stop)

key :
!mainslot (list jenis slot)
"""
        await event.reply(pesan_list)
        
        
    if '/stop_makro' in pesan:
        await event.reply("Reload ✅")
        stop_sesi()
        respond_to_group = False
    
    if '/mainslot' in pesan:
        await asyncio.sleep(2)
        mainslot_list = """Kata kunci mode slot : 
Ikan = SlotMachine_SevenFish
Daun = SlotMachine_SixLeaves
"""    
        await event.reply(mainslot_list)

    if '/gasnanjak' in pesan:
        await event.reply("Main GBK nih")
        await asyncio.sleep(2)
        await client.send_message(mepam, tsk)
        respond_to_group = True
        
    if '/gasmaling' in pesan:
        bhs = 'English'
        await event.reply("Nyuri Bang")
        await asyncio.sleep(2)
        await client.send_message(mepamx, bhs)
        respond_to_group = True
       
    if '/slot' in pesan:
        await asyncio.sleep(2)
        split_result = pesan.split('/slot_')
        if len(split_result) > 1:
            slot = split_result[1]
            if slot in slots_dict:
                time.sleep(2)
                await event.respond(f"Mulai bermain di {slots_dict[slot]}")
                time.sleep(2)
                await client.send_message(mepamx4, slots_dict[slot])
                
            else:
                await event.reply("Maaf, jenis slot tersebut tidak ada dalam daftar")
            respond_to_group = True
        else:
            await event.reply("Anda harus menyertakan jenis slot")
            
with client:
    print(time.asctime(), "- Userbot Dimulai")
    client.run_until_disconnected()