jn_brand = ""
nm_user = ""
no_wa = ""
email = ""
nm_brand = ""

# Function input jenis brand
def jenis_brand():
    global jn_brand
    jn_brand = input("Jenis Brand: \n1. Pendidikan \n2. Makanan & Minuman \n3. Hiburan \n4. Seni \n5. Kesehatan \n6. Pakaian \n7. Lainnya...(isi manual) \nPilih jenis brand anda :")
    if jn_brand == "1":
        jn_brand = "Pendidikan"
    elif jn_brand == "2":
        jn_brand = "Makanan & Minuman"
    elif jn_brand == "3":
        jn_brand = "Hiburan"
    elif jn_brand == "4":
        jn_brand = "Seni"
    elif jn_brand == "5": 
        jn_brand = "Kesehatan"
    elif jn_brand == "6":
        jn_brand = "Pakaian"
    elif jn_brand == "7":
        jn_brand = input("Tuliskan jenis brand anda : ")
    else:
        print("-"*10)
        print("Pilihan anda salah, ulangi")
        jenis_brand()   



print("=== SELAMAT DATANG DI INKSTEP.ID ===")
print("Silahkan isi data berikut ini untuk pemesanan")
# Function Masukkan data
def masukkan():
    global nm_user, no_wa, email, nm_brand
    nm_user = input("Masukkan nama anda : ")
    no_wa = int(input("Masukkan nomor WA anda : "))
    email = input("Masukkan email anda : ")
    nm_brand = input("Masukkan nama brand : ")
    jenis_brand()


# Function Tampilkan data
def tampil():
    print("--------- \nDATA ANDA")
    print(f"Nama        : {nm_user}")
    print(f"No WA       : {no_wa}")
    print(f"Email       : {email}")
    print(f"Nama Brand  : {nm_brand}")
    print(f"Jenis Brand : {jn_brand}")
    

# Function Menu Pilihan (Edit / Keluar)
def menu_akhir():
    makhir = input("Edit = e, Keluar = x : ")
    if makhir == "e" or makhir == "E":
        print("-"*10)
        print("Anda akan mengedit data")
        masukkan()
        tampil()
        menu_akhir()
    elif makhir == "x" or makhir == "X":
        exit()
    else:
        print("Pilihan anda salah")


# Pemanggilan seluruh Function
masukkan()
tampil()
menu_akhir()