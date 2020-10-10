print("\nSelamat datang di inkstep.id \nIsi data berikut ini untuk Daftar\n")
user =  input(" Masukkan username anda   : ")
email = input(" Masukkan email anda      : ")
pas =   input(" Masukkan password anda   : ")


print(f"\nPendaftaran berhasil. Username anda adalah {user} dan password anda adalah {pas}")



# Function Login
def login():
    print("Isi data berikut ini untuk Login")
    u = input("Username / email : ")
    p = input("Password         : ")
    print("-"*20)
    # boleh memilih login dengan username ataupun email
    if (u == user or u == email) and p == pas:
        print("Login berhasil")
    else:
        # jika gagal login, maka diperintah untuk mengulangi login dengan memanggil Function login()
        print("Maaf, username atau password anda salah, ulangi")
        login()


print("-"*20)
# Decision Login
tanya = input("Anda akan login? (y/n) ")
if tanya == "y" or tanya == "Y":
    login()
else:
    exit()