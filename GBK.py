import time, asyncio, sys, random, re
from telethon import TelegramClient, events, utils, Button
import time, os, asyncio, sys, re, random, logging
logging.basicConfig(level=logging.ERROR)

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input('Akun : ')

gbk = '/gbk_jelajah'
restore = '/restore_max_confirm'
bot_id = "KampungMaifamXBot"
#bot_id = 5199147926
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
ch = -1001946930100

with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot_id, tsk))
    @client.on(events.NewMessage(from_users=bot_id))
    async def handler(event):
        pesan = event.raw_text
        global misi, jumlah, tugas, klem, narasi, jenis_tugas
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
                        klem = pesan.splitlines()[12].split('/')[1].split(')')[0]
                        jumlah = pesan.splitlines()[12].split('(')[1].split('/')[0]
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
                    elif jenis_tugas in kolam_kecil:
                        narasi = narasi_5
                    elif jenis_tugas in gua_gibi:
                        narasi = narasi_6
                    elif jenis_tugas in taman_matahari:
                        narasi = narasi_7
                    elif jenis_tugas in kebun_merah:
                        narasi = narasi_8
                    elif jenis_tugas in surga_burung:
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
                elif jenis_tugas in kolam_kecil:
                    narasi = narasi_5
                elif jenis_tugas in gua_gibi:
                    narasi = narasi_6
                elif jenis_tugas in taman_matahari:
                    narasi = narasi_7
                elif jenis_tugas in kebun_merah:
                    narasi = narasi_8
                elif jenis_tugas in surga_burung:
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
            print('-'*30+f"\nTugas {tugas} sudah di selesaikan\n"+'-'*30)
            time.sleep(2)
            await client.forward_messages(ch, event.message)
            time.sleep(10)
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
                    print('Misi selesai. Yuk cari misi lagi!')
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
        
    client.start()
    print(time.asctime(), '-', 'Mulai')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Berhenti')
    