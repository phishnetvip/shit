import pygetwindow as gw
import pyautogui
import time

# Nama jendela aplikasi RF Online
window_title = "RF Online"
file_path = 'kata.txt'

# Membaca semua baris dari file kata.txt
with open(file_path, 'r') as file:
    lines = file.readlines()

# Membersihkan baris dari karakter newline
lines = [line.strip() for line in lines]

# Mencari jendela aplikasi berdasarkan judul
windows = gw.getWindowsWithTitle(window_title)

if windows:
    rf_online_window = windows[0]
    # Membawa jendela aplikasi ke depan tanpa mengubah ukuran
    rf_online_window.activate()
    # Menunggu sebentar untuk memastikan jendela aktif
    time.sleep(1)
    
    try:
        index = 0
        while True:
            # Menekan tombol ENTER pada keyboard
            pyautogui.press('enter')
            
            # Mengetik teks dari file kata.txt
            pyautogui.write(lines[index])
            
            # Menekan tombol ENTER pada keyboard lagi
            pyautogui.press('enter')
            
            # Update index untuk baris berikutnya
            index = (index + 1) % len(lines)
            
    except KeyboardInterrupt:
        print("Program dihentikan oleh pengguna.")
else:
    print(f"Jendela dengan judul '{window_title}' tidak ditemukan.")
