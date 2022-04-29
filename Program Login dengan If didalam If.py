print("Daftar akun")
print("-------------")
u = input("Masukkan username : ")
p = input("Masukkan password : ")

print("Tersimpan")

print("")
print("Login")
print("-------------")
user = input("Masukkan username : ")
password = input("Masukkan password : ")

if user == u:
    if password == p:
        print("Selamat datang")
    else:
        print("Password salah")
else:
    if password != p:
        print("Password salah")
    else:
        print("Username salah")
