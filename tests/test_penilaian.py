import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from models import Penilaian

class TestPenilaian:
    def setup_method(self):
        self.normal = Penilaian(tugas=80, uts=70, uas=90, proyek=85)
        self.hard = Penilaian(100, 100, 100, 100)
        self.easy = Penilaian(0, 0, 0, 0)

    def test_hitung_nilai_akhir(self):
        expected_normal_output = (80 * 0.1) + (70 * 0.2) + (90 * 0.2) + (85 * 0.5)
        assert self.normal.hitung_nilai_akhir() == expected_normal_output, "Perhitungan salah untuk mode normal"
        assert self.hard.hitung_nilai_akhir() == 100, "Perhitungan salah untuk mode hard"
        assert self.easy.hitung_nilai_akhir() == 0, "Perhitungan salah untuk mode easy"

    def test_prediksi_kelulusan(self):
        assert self.normal.prediksi_kelulusan() == True, "Prediksi kelulusan salah untuk mode normal"
        assert self.hard.prediksi_kelulusan() == True, "Prediksi kelulusan salah untuk mode hard"
        assert self.easy.prediksi_kelulusan() == False, "Prediksi kelulusan salah untuk mode easy"