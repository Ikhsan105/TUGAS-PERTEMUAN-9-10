"""
Paket student_performance_tracker

Paket ini berisi semua logika inti, kelas, dan fungsi
untuk mengelola data performa mahasiswa.
"""

# Mengekspos kelas utama ke level paket
# Ini memudahkan kita mengimpor dari 'app.py'
from .mahasiswa import Mahasiswa
from .penilaian import Penilaian
from .rekap_kelas import RekapKelas
from .report import build_markdown_report, save_text

print("Paket 'tracker' berhasil di-load.")