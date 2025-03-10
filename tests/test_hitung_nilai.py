import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from app import hitung_nilai_akhir

def test_hitung_nilai_akhir():
    assert hitung_nilai_akhir(80, 70, 90, 85) == (80 * 0.1) + (70 * 0.2) + (90 * 0.2) + (85 * 0.5), "Perhitungan salah untuk (80,70,90,85)"
    assert hitung_nilai_akhir(100, 100, 100, 100) == 100, "Perhitungan salah untuk (100,100,100,100)"
    assert hitung_nilai_akhir(0, 0, 0, 0) == 0, "Perhitungan salah untuk (0,0,0,0)"
