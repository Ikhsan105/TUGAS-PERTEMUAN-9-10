"""
Modul Mahasiswa

Berisi kelas Mahasiswa untuk merepresentasikan
data satu mahasiswa.
"""

class Mahasiswa:
    """
    Merepresentasikan satu mahasiswa dengan NIM, nama, dan persentase kehadiran.

    Atribut:
        nim (str): Nomor Induk Mahasiswa.
        nama (str): Nama lengkap mahasiswa.
    """

    def __init__(self, nim, nama):
        """
        Membuat instance Mahasiswa baru.

        Args:
            nim (str): Nomor Induk Mahasiswa.
            nama (str): Nama lengkap mahasiswa.
        """
        self.nim = nim
        self.nama = nama
        self._hadir_persen = 0.0  # Atribut internal [cite: 293]

    @property
    def hadir_persen(self):
        """
        Properti untuk mendapatkan nilai persentase kehadiran.
        """
        return self._hadir_persen

    @hadir_persen.setter
    def hadir_persen(self, nilai):
        """
        Properti 'setter' untuk validasi nilai kehadiran.
        Hanya menerima nilai antara 0 dan 100[cite: 146, 200].
        """
        if not (0 <= nilai <= 100):
            print(f"Error: Nilai kehadiran '{nilai}' tidak valid. Harus 0-100.")
        else:
            self._hadir_persen = float(nilai)
            print(f"Info: Kehadiran {self.nama} di-update ke {self._hadir_persen}%.")

    def info(self):
        """
        Menampilkan profil singkat mahasiswa[cite: 147].
        """
        return f"[{self.nim}] {self.nama} - Kehadiran: {self.hadir_persen}%"