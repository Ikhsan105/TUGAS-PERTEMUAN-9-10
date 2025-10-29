"""
Aplikasi Utama - Student Performance Tracker

File ini berisi Command Line Interface (CLI) untuk
berinteraksi dengan paket 'tracker'.

Cara menjalankan:
python app.py
"""
import os
# Impor dari paket 'tracker' yang sudah kita buat
try:
    from tracker import (
        RekapKelas,
        build_markdown_report,
        save_text
    )
except ImportError:
    print("Error: Pastikan file __init__.py ada di dalam folder 'tracker'.")
    exit()

# Tentukan path untuk menyimpan laporan [cite: 171]
SAVE_PATH = os.path.join("out", "report.md")

# --- Fungsi-fungsi untuk Menu ---

def muat_data_dummy(rekap):
    """Helper untuk mengisi data awal (simulasi load CSV)."""
    print("Memuat data dummy...")
    rekap.tambah_mahasiswa("230101001", "Ana")
    rekap.set_hadir("230101001", 92.0)
    rekap.set_penilaian("230101001", quiz=80, tugas=90, uts=85, uas=95) # Nilai Ana

    rekap.tambah_mahasiswa("230101002", "Bimo")
    rekap.set_hadir("230101002", 60.0)
    rekap.set_penilaian("230101002", quiz=50, tugas=60, uts=65, uas=70) # Nilai Bimo
    
    rekap.tambah_mahasiswa("230101003", "Cici")
    rekap.set_hadir("230101003", 100.0)
    rekap.set_penilaian("230101003", quiz=90, tugas=95, uts=92, uas=98) # Nilai Cici
    print("Data dummy berhasil dimuat.")

def tambah_mahasiswa_menu(rekap):
    """Menu untuk opsi 2: Tambah mahasiswa."""
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    rekap.tambah_mahasiswa(nim, nama)

def ubah_presensi_menu(rekap):
    """Menu untuk opsi 3: Ubah presensi."""
    nim = input("Masukkan NIM mahasiswa: ")
    try:
        persen = float(input("Masukkan persentase hadir (0-100): "))
        rekap.set_hadir(nim, persen)
    except ValueError:
        print("Error: Masukkan angka yang valid untuk persentase.")

def ubah_nilai_menu(rekap):
    """Menu untuk opsi 4: Ubah nilai."""
    nim = input("Masukkan NIM mahasiswa: ")
    try:
        quiz = float(input("Nilai Quiz (0-100): "))
        tugas = float(input("Nilai Tugas (0-100): "))
        uts = float(input("Nilai UTS (0-100): "))
        uas = float(input("Nilai UAS (0-100): "))
        rekap.set_penilaian(nim, quiz, tugas, uts, uas)
    except ValueError:
        print("Error: Masukkan angka yang valid untuk nilai.")

def lihat_rekap_menu(rekap):
    """Menu untuk opsi 5: Lihat rekap di terminal."""
    print("\n--- REKAP NILAI SAAT INI ---")
    records = rekap.rekap()
    if not records:
        print("Belum ada data mahasiswa.")
        return

    # Header
    print(f"{'NIM':<12} | {'Nama':<15} | {'Hadir (%)':<10} | {'Nilai Akhir':<12} | {'Predikat':<8}")
    print("-" * 70)
    
    # Data
    for rec in records:
        print(f"{rec['nim']:<12} | {rec['nama']:<15} | {rec['hadir']:<10.1f} | {rec['nilai_akhir']:<12.2f} | {rec['predikat']:<8}")
    print("-" * 70)


def simpan_laporan_menu(rekap):
    """Menu untuk opsi 6: Simpan laporan ke file Markdown."""
    print("Membuat laporan Markdown...")
    records = rekap.rekap()
    if not records:
        print("Tidak ada data untuk dilaporkan.")
        return
        
    content = build_markdown_report(records)
    save_text(SAVE_PATH, content)


def main_menu():
    """Menampilkan menu utama CLI [cite: 204-212]."""
    
    # Buat satu instance manajer rekap
    rekap_data = RekapKelas()

    while True:
        print("\n=== Student Performance Tracker ===")
        print("1) Muat data (dummy)")
        print("2) Tambah mahasiswa")
        print("3) Ubah presensi")
        print("4) Ubah nilai")
        print("5) Lihat rekap terminal")
        print("6) Simpan laporan Markdown")
        print("7) Keluar")
        
        pilihan = input("Pilih menu (1-7): ")
        
        if pilihan == '1':
            muat_data_dummy(rekap_data)
        elif pilihan == '2':
            tambah_mahasiswa_menu(rekap_data)
        elif pilihan == '3':
            ubah_presensi_menu(rekap_data)
        elif pilihan == '4':
            ubah_nilai_menu(rekap_data)
        elif pilihan == '5':
            lihat_rekap_menu(rekap_data)
        elif pilihan == '6':
            simpan_laporan_menu(rekap_data)
        elif pilihan == '7':
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# --- Titik Masuk Program ---
if __name__ == "__main__":
    """
    Entry point ini memastikan main_menu() hanya berjalan
    saat file ini dieksekusi sebagai script [cite: 202-203].
    """
    main_menu()