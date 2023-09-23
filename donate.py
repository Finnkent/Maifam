#by Aditz
from telethon import TelegramClient,events
import time, re
import random
api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input("Mau akun mana = ")


#bot
print("\ncontoh: Angka = 2")
print("Pilih bot yng digunakan")
mpm = input("\tKetik 1 untuk Bot Alpha\n\tKetik 2 untuk Bot X\n\tKetik 3 untuk Bot X4\n   Angka = ")
if mpm == '1':
    bot_id = 'KampungMaifamBot'
elif mpm == '2':
    bot_id = 'KampungMaifamXBot'
elif mpm == '3':
    bot_id = 'KampungMaifamX4Bot'

#Donasinya
print("\nPilih mau donasi apa")
pilih = input("\tKetik 1 untuk Donasi Guild (Barang)\n\tKetik 2 untuk Donasi Guild (Uang)\n\tKetik 3 untuk Ambil barang Guild\n\tKetik 4 untuk Donasi Barang ke alamat\n   Angka = ")

print()
item = input("Mau item apa = ")

if pilih == '1':
    jmlh = input("berapa jumlahnya = ")
    nunggu = 4
    guild = f"/donasiguild_{item}_{jmlh}"
    tempat = guild
elif pilih == '2':
    jmlh = input("berapa jumlahnya = ")
    nunggu = 4
    guild = f"/donasiguild_{jmlh}"
    tempat = guild
elif pilih == '3':
    jmlh = input("berapa jumlahnya = ")
    nunggu = 4
    guild = f"/donasiguild_{item}_ambil_{jmlh}"
    tempat = guild
elif pilih == '4':
    nunggu = 20
    alamat = input("Apa alamatnya = ")
    barang = f"/donasibarang_{alamat}_{item}"
    tempat = barang
    
print()
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot_id, tempat))
    @client.on(events.NewMessage(from_users=bot_id))
    async def handler(event):
        message = event.raw_text
    
        if "Successfully donated" in message or "Berhasil mendonasikan" in message:
            print(message)
            time.sleep(nunggu)
            await event.respond(tempat)
            return
        
        if "Spasi penyimpanan barang" in message:
            print(message)
            time.sleep(nunggu)
            await event.respond(tempat)
            return
          
        if "Tidak bisa mendonasikan uang lebih" in message:
            print(message)
            time.sleep(nunggu)
            await event.respond(tempat)
            return
          
        if "Not enough" in message:
            print(message)
            time.sleep(4)
            await event.respond(tempat)
            return

        if "Guild tidak memiliki" in message or "Berhasil mengambil" in message:
            print(message)
            time.sleep(4)
            await event.respond(tempat)
            return
            
        if "No" in message:
            print(message)
            time.sleep(4)
            await event.respond(tempat)
            return
            
        if "just donated" in message or "baru saja" in message:
            sl = re.findall('\d+', message)
            nn = int(sl[0])
            print(time.asctime(), f'Tunggu {90-nn} detik')
            time.sleep(int(90-nn))
            await event.respond(tempat)
            return
            
            
    client.start()
    print(time.asctime(), '-', tempat)
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Berhenti')
   
