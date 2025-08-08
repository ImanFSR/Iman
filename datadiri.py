print("=====================================")

print("Selamat datang di Program Data Diri Sederhana dengan menggunakan Python")
print("Mohon maaf jika ada kesalahan dalam program ini ya!")

print("=====================================")

name = input("Masukkan nama lengkap anda: ")
nama = input("Masukkan nama panggilan anda: ")
age = int(input("Masukkan umur anda: "))
sch = input("Status sekarang? (Mahasiswa/Kerja/Nganggur): ").lower()
if sch == "mahasiswa":
    kampus = input("Masukkan nama tempat kampus anda: ")
    print("=====================================")
    print(f"Nama panjang anda adalah {name}, dan nama panggilan anda adalah {nama}.")
    print(f"Umur anda sekarang adalah {age} tahun, dan anda sekarang adalah seorang {sch} dari {kampus}.")

if sch == "kerja":
    kerja = input("Masukkan nama tempat kerja anda: ")
    jbt = input("Masukkan jabatan anda: ")
    print("======================================")
    print(f"Nama panjang anda adalah {name}, dan nama panggilan anda adalah {nama}.")
    print(f"Umur anda sekarang adalah {age} tahun, dan anda sekarang {sch} di {kerja} sebagai {jbt}.")

if sch == "nganggur":
    print("======================================")
    print(f"Nama panjang anda adalah {name}, dan nama panggilan anda adalah {nama}.")
    print(f"Umur anda sekarang adalah {age} tahun, dan anda sekarang adalah seorang pengagguran ga guna.")

elif sch not in ["mahasiswa", "kerja", "nganggur"]:
    print("======================================")
    print("Status tidak valid, silakan masukkan Mahasiswa, Kerja, atau Nganggur.")
print("======================================")
print("Terima kasih sudah mengisi data diri anda!")