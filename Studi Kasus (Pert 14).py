
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
