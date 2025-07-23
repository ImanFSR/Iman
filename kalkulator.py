print("====================================")
print("Selamat datang di Program Kalkulator Sederhana dengan menggunakan Python")
print("Mohon maaf jika ada kesalahan dalam program ini ya!")
print("====================================")

print("Silahkan pilih operasi yang ingin dilakukan sebagai berikut:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

print("=====================================")

operasi = int(input("Masukkan operasi yang dipilih (1-4): "))
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

print("=====================================")

if operasi == 1:
    hasil = angka1 + angka2
    print(f"Hasil = {hasil}")

if operasi == 2:
    hasil = angka1 - angka2
    print(f"Hasil = {hasil}")

if operasi == 3:
    hasil = angka1 * angka2
    print(f"Hasil = {hasil}")

if operasi == 4:
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil = {hasil}")
    else:
        print("❌ Pembagian dengan nol tidak diperbolehkan.")
        
print("Terima kasih telah menggunakan program ini!")
print("=====================================")