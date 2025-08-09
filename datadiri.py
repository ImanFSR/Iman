# datadiri.py
garis = "=" * 40

print(garis)

print("Selamat datang di Program Data Diri Sederhana dengan menggunakan Python")
print("Mohon maaf jika ada kesalahan dalam program ini ya!")

print(garis)

name = input("Masukkan nama lengkap anda: ")
nama = input("Masukkan nama panggilan anda: ")
age = int(input("Masukkan umur anda: "))
sch = input("Status sekarang? (Mahasiswa/Kerja/Nganggur): ").lower()
if sch == "mahasiswa":
    kampus = input("Masukkan nama tempat kampus anda: ")
    smt = int(input("Masukkan semester anda sekarang: "))
    print(garis)
    print(f"Nama panjang anda adalah {name}, dan nama panggilan anda adalah {nama}.")
    print(f"Umur anda sekarang adalah {age} tahun.")
    print(f"Anda adalah seorang {sch} semester {smt} dari kampus {kampus}.")

elif sch == "kerja":
    kerja = input("Masukkan nama tempat kerja anda: ")
    jbt = input("Masukkan jabatan anda: ")
    print(garis)
    print(f"Nama panjang anda adalah {name}, dan nama panggilan anda adalah {nama}.")
    print(f"Umur anda sekarang adalah {age} tahun, dan anda sekarang {sch} di {kerja} sebagai {jbt}.")

elif sch == "nganggur":
    print(garis)
    print(f"Nama panjang anda adalah {name}, dan nama panggilan anda adalah {nama}.")
    print(f"Umur anda sekarang adalah {age} tahun, dan anda sekarang adalah seorang pengagguran ga guna.")

else:
    print(garis)
    print("Status tidak valid, silakan masukkan Mahasiswa, Kerja, atau Nganggur.")
print(garis)
print("Terima kasih sudah mengisi data diri anda!")

