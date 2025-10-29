"""
Modul Penilaian

Berisi kelas Penilaian untuk mengelola skor
quiz, tugas, uts, dan uas.
"""

class Penilaian:
    """
    Merepresentasikan kumpulan nilai untuk satu mahasiswa.
    Semua nilai divalidasi harus 0-100[cite: 155].
    """
    def __init__(self):
        """Membuat instance Penilaian baru, semua nilai awal 0."""
        self._quiz = 0.0
        self._tugas = 0.0
        self._uts = 0.0
        self._uas = 0.0

    # Helper validasi internal
    def _validate_score(self, nilai):
        """Helper untuk validasi nilai 0-100."""
        if not (0 <= nilai <= 100):
            raise ValueError(f"Nilai '{nilai}' tidak valid. Harus 0-100.")
        return float(nilai)

    # --- Properti untuk setiap komponen nilai ---
    @property
    def quiz(self):
        return self._quiz
    
    @quiz.setter
    def quiz(self, nilai):
        self._quiz = self._validate_score(nilai)

    @property
    def tugas(self):
        return self._tugas
    
    @tugas.setter
    def tugas(self, nilai):
        self._tugas = self._validate_score(nilai)

    @property
    def uts(self):
        return self._uts
    
    @uts.setter
    def uts(self, nilai):
        self._uts = self._validate_score(nilai)

    @property
    def uas(self):
        return self._uas
    
    @uas.setter
    def uas(self, nilai):
        self._uas = self._validate_score(nilai)

    def nilai_akhir(self):
        """
        Menghitung nilai akhir berdasarkan bobot:
        - Quiz: 15%
        - Tugas: 25%
        - UTS: 25%
        - UAS: 35%
        """
        total = (
            (self._quiz * 0.15) +
            (self._tugas * 0.25) +
            (self._uts * 0.25) +
            (self._uas * 0.35)
        )
        return total