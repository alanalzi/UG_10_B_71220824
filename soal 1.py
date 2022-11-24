print("~~~~~~~~~~~~~~~~ /('v')\ ~~~~~~~~~~~~~~~~")
print("PROGRAM PENGHITUNG VOLUME BANGUN RUANG")
print("~~~~~~~~~~~~~~~~ \('v')/ ~~~~~~~~~~~~~~~~")

print("Pilihlah salah satu bangun ruang yang ingin di hitung volumenya: ")
print("1. Limas")
print("2. Bola")
print("3. Prisma")
print("4. Kerucut")
print("")
bangun_ruang = input("Masukan pilihan Anda ")
if bangun_ruang == '1':
#limas
    sisi_alas = int(input("Masukan sisi alas limas: "))
    tinggi_limas = int(input("Masukan tinggi limas: "))
    hasil = float((sisi_alas*sisi_alas/3)*tinggi_limas)
    print("volume limas tersebut adalah",hasil)
elif bangun_ruang == '2':
    jari_jari = int(input("Masukan panjang jari-jari bola: "))
    hasil_bola = int(4/3*3.14*jari)
    volume = print("Volume bola tersebut adalah",hasil)    
elif bangun_ruang == '3':
    print("Pilihlah salah satu dari pilihan di bawah:")
    print("1. Prisma segitiga")
    print("2. Prisma segiempat")
    print("3. prisma segilima")
