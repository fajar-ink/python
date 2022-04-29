import numpy as np
nama = input("Masukkan nama donasi : ")
print("")
target = float(input("Masukkan target donasi : "))
masuk = float(input("Masukkan donasi masuk  : "))

persentase = masuk/target*100
kekurangan = int(target-masuk)

print("")
print("---------------")
print(nama)
print("")
print("Target donasi : Rp", int(target), ",-")
print("Donasi masuk  : Rp", int(masuk), ",-")
print("Persentase    :", np.around(persentase, 2), "%")
print("Kekurangan    : Rp", int(kekurangan), ",-")
print("")
