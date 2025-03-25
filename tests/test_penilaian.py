import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from models import Penilaian

def test_hitung_nilai_akhir():
    normal = Penilaian(tugas=80, uts=70, uas=90, proyek=85)
    hard = Penilaian(100, 100, 100, 100)
    easy = Penilaian(0, 0, 0, 0)
    expected_normal_output = (80 * 0.1) + (70 * 0.2) + (90 * 0.2) + (85 * 0.5)
    assert normal.hitung_nilai_akhir() == expected_normal_output, "Perhitungan salah untuk mode normal"
    assert hard.hitung_nilai_akhir() == 100, "Perhitungan salah untuk mode hard"
    assert easy.hitung_nilai_akhir() == 0, "Perhitungan salah untuk mode easy"