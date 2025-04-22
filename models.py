class Penilaian:
    def __init__(self, tugas, uts, uas, proyek):
        self.tugas = tugas
        self.uts = uts
        self.uas = uas
        self.proyek = proyek

    def hitung_nilai_akhir(self):
        return (self.tugas * 0.1) + (self.uts * 0.2) + (self.uas * 0.2) + (self.proyek * 0.5)

    def prediksi_kelulusan(self):
        status = True
        self.hitung_nilai_akhir()
        return status