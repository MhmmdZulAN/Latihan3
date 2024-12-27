txt = 'Hello World'

print(txt)
# Menampilkan Jumlah Karakter
print(len(txt))

# Ambil Karakter Terakhir
print(txt[-1])

# Menampilkan huruf terakhir
print(txt[2:5])


# Hilangkan spasi pada text
print(txt.replace(' ',''))

#Ubah text menjadi huruf besar
print(txt.upper())

#ubah text menjadi huruf kecil
print(txt.lower())

# mengubah huruf H menjadi J
print(txt.replace('H','J'))

#LENGKAPI KODE BERIKUT!!

umur = 24
txt = 'Hello, nama saya John, dan umur saya adalah {} tahun'

print(txt.format(umur))


#STUDI KASUS
def validasi_form(nama, nomor_telepon, email):
    errors = []
    
    # Validasi nama lengkap (hanya huruf)
    if not nama.replace(" ", "").isalpha():
        errors.append("Nama lengkap harus hanya berisi huruf.")
    
    # Validasi nomor telepon (hanya angka)
    if not nomor_telepon.isdigit():
        errors.append("Nomor telepon harus hanya berisi angka.")
    
    # Validasi email (harus mengandung '@' dan '.')
    if "@" not in email or "." not in email:
        errors.append("Email harus mengandung karakter '@' dan '.'.")
    
    # Output hasil validasi
    if errors:
        print("Terdapat kesalahan pada data pendaftaran:")
        for error in errors:
            print(f"- {error}")
    else:
        print("Data pendaftaran valid.")

# Contoh penggunaan
nama = input("Masukkan nama lengkap: ")
nomor_telepon = input("Masukkan nomor telepon: ")
email = input("Masukkan email: ")

validasi_form(nama, nomor_telepon, email)


