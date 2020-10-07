print("\nPROGRAM PEMBUAT SOAL")
print("="*20)
jml_soal = int(input("Masukkan jumlah soal yang akan dibuat : "))
jml_pilihan = int(input("Masukkan jumlah pilihan jawaban       : "))
print("\n")

# deklarasi list soal dan jawaban
soal = []
jawaban = []

# input soal beserta pilihan jawaban
for i in range(0, jml_soal):
    i+=1
    print(f"SOAL {i}")
    input_soal = input(" Masukkan soal: \n ")
    soal.append(input_soal)

    for j in range(0, jml_pilihan):
        j+=1
        input_jawaban = input(f" Jawaban {j}: ")
        jawaban.append(input_jawaban)
    print("\n")


print("="*25)
print("SOAL YANG TELAH ANDA BUAT :")
print("")

#tampilkan soal dan pilihan jawaban yang telah diinputkan
for i in range(0, len(soal)):
    data_soal = soal[i]
    print(f"SOAL {i+1}")
    print("",data_soal)

    a = i*jml_pilihan
    b = a+jml_pilihan
    for j in range((a),(b)):
        data_jawaban = jawaban[j]
        print(f" {(j+1)-(i*jml_pilihan)}. {data_jawaban}")
    print("")