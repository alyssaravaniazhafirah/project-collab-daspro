print("====================================================================")
print("                  UNIVERSITAS BINA SARANA INFORMATIKA               ")
print("                     FAKULTAS TEKNIK INFORMATIKA                   ")
print("                PROGRAM STUDI S1 TEKNOLOGI INFORMASI               ")
print("====================================================================")
print("                         KARTU RENCANA STUDI (KRS)                 ")
print("                       SEMESTER : Ganjil 2024/2025                 ")
print("====================================================================")

print("|                        IDENTITAS MAHASISWA                       |")
print("--------------------------------------------------------------------")
nim = input("NIM (Nomor Induk Mahasiswa) : ")
nama = input("Nama Mahasiswa              : ")
print("--------------------------------------------------------------------")

# Daftar mata kuliah sebagai dictionary
daftar_matkul = {
    "153": {"nama": "PENGANTAR TEKNOLOGI INFORMASI DAN KOMUNIKASI", "sks": 3, "keterangan": "Wajib"},
    "712": {"nama": "ENTREPRENEURSHIP", "sks": 3, "keterangan": "Wajib"},
    "101": {"nama": "PENDIDIKAN PANCASILA", "sks": 2, "keterangan": "Wajib"},
    "894": {"nama": "DASAR PEMROGRAMAN", "sks": 4, "keterangan": "Wajib"},
    "104": {"nama": "BAHASA INGGRIS I", "sks": 2, "keterangan": "Pilihan"},
    "207": {"nama": "LOGIKA DAN ALGORITMA", "sks": 4, "keterangan": "Wajib"}
}

print("|                    DAFTAR MATA KULIAH TERSEDIA                   |")
print("--------------------------------------------------------------------")
print("| Kode | Nama Mata Kuliah                     | SKS | Keterangan   |")
print("|------|--------------------------------------|-----|--------------|")
for kode, matkul in daftar_matkul.items():
    print(f"| {kode:<4} | {matkul['nama']:<36} | {matkul['sks']:<3} | {matkul['keterangan']:<12} |")
print("--------------------------------------------------------------------")

banyak_matkul = int(input("Masukkan banyak mata kuliah yang akan diambil : "))

# List untuk menyimpan mata kuliah yang diambil
matkul_diambil = []

# Input data mata kuliah yang diambil
for i in range(banyak_matkul):
    print(f"\nMasukkan data matkul ke-{i+1}:")
    kode = input("Kode Mata Kuliah (153/712/101/894/104/207): ")
    kelas = input("Kelas (A/B/C): ")

    if kode in daftar_matkul:
        matkul_diambil.append({
            "kode": kode,
            "nama": daftar_matkul[kode]["nama"],
            "sks": daftar_matkul[kode]["sks"],
            "keterangan": daftar_matkul[kode]["keterangan"],
            "kelas": kelas
        })
    else:
        print("Kode Mata Kuliah Tidak Dikenal")

print("\n====================================================================")
print("|                    RENCANA STUDI MAHASISWA                       |")
print("|     (Mata Kuliah yang akan diambil pada semester ini)            |")
print("--------------------------------------------------------------------")
print("| Kode | Nama Mata Kuliah                     | SKS | Kelas | Keterangan |")
print("|------|--------------------------------------|-----|-------|-------------|")

total_sks = 0
for matkul in matkul_diambil:
    print(f"| {matkul['kode']:<4} | {matkul['nama']:<36} | {matkul['sks']:<3} | {matkul['kelas']:<5} | {matkul['keterangan']:<10} |")
    total_sks += matkul['sks']

print("--------------------------------------------------------------------")
print(f"| JUMLAH TOTAL SKS : {total_sks:<3}                                           |")
print("====================================================================")

print("======================== DATA MAHASISWA ============================")
print(f"NIM             : {nim}")
print(f"Nama Mahasiswa  : {nama}")
print("Program Studi   : S1 Teknologi Informasi")
print("Dosen Wali      : Dr. Andi Suhendra, M.Kom.")
print("====================================================================")
print("KRS berhasil dicetak. Selamat belajar!")
