import os
import subprocess
from telegram import Update, User
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv
import signal

# Menyimpan informasi script yang sedang berjalan
running_script_process = None
updater = None
sudo_user_ids = set()


# Load environment variables from .env
load_dotenv()

OWNER_ID = os.getenv('OWNER_ID')
START_LOGS = os.getenv('START_LOGS')
EVENT_LOGS = os.getenv('EVENT_LOGS')

def send_start_logs(updater: Updater, user: User):
    log_message = f'Pengguna memulai bot\nID: {user.id}\nFirst Name: {user.first_name}\nUsername: @{user.username}'
    # Kirim log_message ke START_LOGS (misalnya, sebuah grup atau chat khusus)
    updater.bot.send_message(START_LOGS, log_message)

# Fungsi untuk menangani perintah /start
def start(update: Update, context: CallbackContext):
    user = update.effective_user
    if user.id == int(OWNER_ID) or user.id in sudo_user_ids:
        update.message.reply_text(f'Selamat datang, {user.first_name}! Silakan kirimkan perintah untuk saya.')
    else:
        update.message.reply_text('Anda tidak memiliki izin untuk bot ini.')
        # Panggil send_start_logs dengan updater dan user
        send_start_logs(updater, user)

# Fungsi untuk menjalankan script dari file
def run_script(update: Update, context: CallbackContext):
    global running_script_process

    user = update.effective_user
    if user.id != int(OWNER_ID) or user.id in sudo_user_ids:
        update.message.reply_text('Anda tidak memiliki izin untuk bot ini.')
        return

    if len(context.args) == 0:
        update.message.reply_text('Gunakan: /run <nama_file>')
        return

    script_filename = context.args[0]
    
    if not os.path.exists(script_filename):
        update.message.reply_text('File tidak ditemukan.')
        return

    try:
        update.message.reply_text(f'Mulai menjalankan {script_filename}')
        running_script_process = subprocess.Popen(['python', script_filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=os.setsid)
        update.message.reply_text('Script sedang berjalan.')
    except Exception as e:
        update.message.reply_text('Terjadi kesalahan saat menjalankan script: {}'.format(str(e)))

# Fungsi untuk menghentikan script yang sedang berjalan
def stop_script(update: Update, context: CallbackContext):
    global running_script_process

    if running_script_process is None:
        update.message.reply_text('Tidak ada script yang sedang berjalan.')
        return

    try:
        os.killpg(os.getpgid(running_script_process.pid), signal.SIGTERM)
        update.message.reply_text('Berhasil menghentikan script.')
        running_script_process = None
    except Exception as e:
        update.message.reply_text('Terjadi kesalahan saat menghentikan script: {}'.format(str(e)))

# Fungsi untuk menangani perintah /addsudo
def add_sudo(update: Update, context: CallbackContext):
    global updater, sudo_user_ids

    user = update.effective_user
    if user.id == int(OWNER_ID):
        if len(context.args) == 0:
            update.message.reply_text('Gunakan: /addsudo <user_id>')
            return

        new_sudo_user_id = int(context.args[0])

        # Tambahkan ID sudo user ke dalam set
        sudo_user_ids.add(new_sudo_user_id)

        # Kirim pesan konfirmasi
        update.message.reply_text(f'Pengguna dengan ID {new_sudo_user_id} ditambahkan sebagai sudo.')

        # Kirim informasi pengguna yang ditambahkan ke START_LOGS
        sudo_user = context.bot.get_chat(new_sudo_user_id)
        log_message = f'Owner menambahkan izin akses kepada pengguna baru:\nID: {sudo_user.id}\nFirst Name: {sudo_user.first_name}\nUsername: {sudo_user.username}'
        updater.bot.send_message(EVENT_LOGS, log_message)
    else:
        update.message.reply_text('Anda tidak memiliki izin untuk perintah ini.')


    
def rmsudo(update: Update, context: CallbackContext):
    global sudo_user_ids

    user = update.effective_user
    if user.id == int(OWNER_ID):
        if len(context.args) == 0:
            update.message.reply_text('Gunakan: /rmsudo <user_id>')
            return

        user_to_remove_id = int(context.args[0])

        if user_to_remove_id in sudo_user_ids:
            # Hapus ID sudo user dari set
            sudo_user_ids.remove(user_to_remove_id)

            # Kirim pesan konfirmasi
            update.message.reply_text(f'Pengguna dengan ID {user_to_remove_id} telah dihapus dari akses sudo.')
        else:
            update.message.reply_text(f'Pengguna dengan ID {user_to_remove_id} bukan sudo.')

        # Tambahkan log pengguna yang dihapus dari sudo ke EVENT_LOGS
        log_message = f'Owner menghapus izin akses dari pengguna:\nID: {user_to_remove_id}'
        updater.bot.send_message(EVENT_LOGS, log_message)
    else:
        update.message.reply_text('Anda tidak memiliki izin untuk perintah ini.')
    
def main():
    global updater  # Deklarasikan updater sebagai global
    # Token bot Telegram
    token = os.getenv('TOKEN')

    # Inisialisasi bot
    updater = Updater(token)

    # Daftarkan handler perintah /start
    updater.dispatcher.add_handler(CommandHandler('start', start))
    
    # Daftarkan handler perintah /run
    updater.dispatcher.add_handler(CommandHandler('run', run_script))

    # Daftarkan handler perintah /stop
    updater.dispatcher.add_handler(CommandHandler('stop', stop_script))

    # Daftarkan handler perintah /addsudo
    updater.dispatcher.add_handler(CommandHandler('addsudo', add_sudo))

    # Jalankan bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()