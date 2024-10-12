print("Selamat Datang Dipenghitungan IPS (Indeks Prestasi Semester)")
nama = str(input("Nama : "))
kehadiran = int(input("Jumlah kehadiran : "))
hadir = kehadiran / 14 * 10
print(f'Pesentase Kehadiran : {hadir}')

tugas = int(input("Nilai Rata-Rata Tugas : "))
hasil = tugas / 100 * 20
print(f'Persentase Tugas : {hasil}')

uts = int(input("Nilai UTS : "))
ujian1 = uts / 100 * 30
print(f'Persentase UTS : {ujian1}')

uas = int(input("Nilai UAS : "))
ujian2 = uas / 100 * 40
print(f'Persentase UAS : {ujian2}')

ips = hadir + hasil + ujian1 + ujian2
print (f'IPS : {ips}')
status = "Kerja Bagus" if ips > 80 else "Tetap Semangat"
print(status)
print("Terimakasih")