from flask import Flask, request, render_template
from models import Penilaian
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tugas = float(request.form['tugas'])
        uts = float(request.form['uts'])
        uas = float(request.form['uas'])
        proyek = float(request.form['proyek'])
        hasil = Penilaian.hitung_nilai_akhir(tugas, uts, uas, proyek)
        return render_template('index.html', hasil=hasil)
    return render_template('index.html', hasil=None)

if __name__ == '__main__':
    app.run(debug=True)