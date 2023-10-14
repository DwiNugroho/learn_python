# Soal

# PT. DINGIN DAMAI, memberi gaji pokok kepada karyawan kontraknya sebesar Rp.
# 300,000 perbulan, dengan memperoleh tunjangan-tunjangan sebagai berikut :

# Tunjangan jabatan
# golongan 1:5%
# golongan 2:10%
# golongan 3:15%

# Logikanya : Jika seorang karyawan tersebut dengan golongan 3, maka mendapatkan tunjangan sebesar
# 15% * Rp. 300,000

# tunjangan pendidikan
# SMA:2.5%
# D1:5%
# D3:20%
# S1:30%

# Jika seorang karyawan tersebut dengan Tingkat Pendidikan S1, maka mendapatkan tunjangan
# pendidikan sebesar 30% * Rp. 300,000

# Honor lembur
# Jumlah jam kerja normal sebanyak 8 jam, Honor lembur diberikan jika jumlah jam kerja lebih dari 8
# jam, maka kelebihan jam kerja tersebut dikalikan dengan Rp. 3500 untuk setiap kelebihan jam kerja
# karyawan tersebut.Tampilan yang diinginkan sebagai berikut :

# layar masukkan
#   program hitung gaji karyawan
#   nama karyawan:...
#   golongan jabatan:...
#   pendidikan:...
#   jumlah jam kerja:...

# layar keluaran
#   karyawan bernama...
#   honor yang diterima
#     tunjangan jabatan Rp...
#     tunjangan pendidikan Rp...
#     honor lembur Rp...
#     total gaji (gaji pokok + tunjangan + lembur) Rp...

## Jawaban

def hitung_tunjangan_jabatan(golongan):
    if golongan == 1:
        return 0.05 * 300000
    elif golongan == 2:
        return 0.10 * 300000
    elif golongan == 3:
        return 0.15 * 300000
    else:
        return 0

def hitung_tunjangan_pendidikan(pendidikan):
    if pendidikan == 'SMA':
        return 0.025 * 300000
    elif pendidikan == 'D1':
        return 0.05 * 300000
    elif pendidikan == 'D3':
        return 0.20 * 300000
    elif pendidikan == 'S1':
        return 0.30 * 300000
    else:
        return 0

def hitung_honor_lembur(jam_kerja):
    if jam_kerja > 8:
        return (jam_kerja - 8) * 3500
    else:
        return 0

# Input data dari pengguna
print("---------------- Program Hitung Gaji Karyawan----------------")
nama_karyawan = input("Nama karyawan: ")
golongan_jabatan = int(input(" Golongan jabatan (1/2/3)    : "))
pendidikan = input(" Pendidikan (SMA/D1/D3/S1)   : ")
jam_kerja = int(input(" Jumlah jam kerja            : "))

# Hitung tunjangan dan honor lembur
tunjangan_jabatan = int(hitung_tunjangan_jabatan(golongan_jabatan))
tunjangan_pendidikan = int(hitung_tunjangan_pendidikan(pendidikan))
honor_lembur = int(hitung_honor_lembur(jam_kerja))

# Hitung total gaji
total_gaji = int(300000 + tunjangan_jabatan + tunjangan_pendidikan + honor_lembur)

# Output hasil
print('--------------------------------------------------------------')
print(f"Karyawan bernama {nama_karyawan}")
print(f"Honor yang diterima")
print(f"  Tunjangan jabatan           Rp {tunjangan_jabatan:,.0f}")
print(f"  Tunjangan pendidikan        Rp {tunjangan_pendidikan:,.0f}")
print(f"  Honor lembur                Rp {honor_lembur:,.0f}")
print(f"  Total gaji                  Rp {total_gaji:,.0f}")
