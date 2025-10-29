"""
Modul Rekap Kelas

Berisi kelas manajer 'RekapKelas' untuk mengelola
kumpulan data mahasiswa dan penilaian.
"""
from .mahasiswa import Mahasiswa
from .penilaian import Penilaian

class RekapKelas:
    """
    Manajer untuk mengelola banyak objek Mahasiswa dan Penilaian.
    Menggunakan komposisi (memiliki 'has-a')[cite: 319].
    """
    def __init__(self):
        """
        Membuat instance manajer rekap.
        Data disimpan dalam dictionary sesuai spesifikasi[cite: 160].
        """
        self._data = {} # Format: {nim: {'mhs': obj, 'nilai': obj}}

    def tambah_mahasiswa(self, nim, nama):
        """Menambah mahasiswa baru ke dalam rekap[cite: 162]."""
        if nim in self._data:
            print(f"Error: NIM {nim} sudah ada.")
            return
        
        mhs_obj = Mahasiswa(nim, nama)
        nilai_obj = Penilaian()
        self._data[nim] = {'mhs': mhs_obj, 'nilai': nilai_obj}
        print(f"Sukses: Mahasiswa {nama} berhasil ditambahkan.")

    def set_hadir(self, nim, persen):
        """Mengatur persentase kehadiran untuk mahasiswa[cite: 163]."""
        if nim not in self._data:
            print(f"Error: NIM {nim} tidak ditemukan.")
            return
        
        try:
            self._data[nim]['mhs'].hadir_persen = persen
        except ValueError as e:
            print(f"Error: {e}")

    def set_penilaian(self, nim, quiz, tugas, uts, uas):
        """Mengatur semua nilai untuk mahasiswa[cite: 164]."""
        if nim not in self._data:
            print(f"Error: NIM {nim} tidak ditemukan.")
            return
        
        try:
            nilai_obj = self._data[nim]['nilai']
            nilai_obj.quiz = quiz
            nilai_obj.tugas = tugas
            nilai_obj.uts = uts
            nilai_obj.uas = uas
            print(f"Sukses: Nilai {self._data[nim]['mhs'].nama} berhasil di-update.")
        except ValueError as e:
            print(f"Error set nilai: {e}")

    def _get_predikat(self, nilai_akhir):
        """Helper internal untuk menentukan predikat huruf[cite: 166]."""
        if nilai_akhir >= 85:
            return "A"
        elif nilai_akhir >= 75:
            return "B"
        elif nilai_akhir >= 65:
            return "C"
        elif nilai_akhir >= 50:
            return "D"
        else:
            return "E"

    def rekap(self):
        """
        Mengembalikan list of dictionaries dari semua data[cite: 165].
        """
        records = []
        for nim, data in self._data.items():
            mhs = data['mhs']
            nilai = data['nilai']
            
            n_akhir = nilai.nilai_akhir()
            predikat = self._get_predikat(n_akhir)
            
            records.append({
                "nim": mhs.nim,
                "nama": mhs.nama,
                "hadir": mhs.hadir_persen,
                "nilai_akhir": n_akhir,
                "predikat": predikat
            })
        return records