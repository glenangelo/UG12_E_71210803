a = input("Hi Tutu, Silahkan Masukkan hari yang ingin Anda telusuri: ")
matkul = ["1 Algoritma", "3 Sistem Operasi", "4 PAK", "5 Praktikum INLAN", "2 Matematika Teknik", "4 Bhs Indonesia", "6 PKN", "1 IMK", "3 LogMat", "4 Praktekkom", "2 Sistem Basis Data", "4 Praktikum Sistem Basis Data", "6 INLAN"]

if a == "senin":
    for i in range(0,4):
        print("Kelas Ke-",matkul[i])

elif a == "selasa":
    for i in range(4,7):
        print("Kelas Ke-", matkul[i])

elif a == "rabu":
        print("Hari rabu Anda tidak ada kelas")

elif a == "kamis":
    for i in range(7,10):
        print("Kelas Ke-", matkul[i])

elif a == "jumat":
    for i in range(10,12):
        print("Kelas Ke-", matkul[i])

else:
    print("Hari tidak ditemukan")