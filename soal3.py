print ("~~ Selamat Datang Di Program Pengurutan Bilangan ~~")
print ("")
print ("Tentukan pilihan anda")
print ("1. Ascending")
print ("2. Descending")
print ("")
a1 = int(input(">> "))
print ("")

if a1 == 1:
    a1 = int(input("Masukan Bilangan Bulat Pertama : "))
    a2 = int(input("Masukan Bilangan Bulat Kedua : "))
    a3 = int(input("Masukan Bilangan Bulat Ketiga : "))
    a4 = int(input("Masukan Bilangan Bulat Keempat : "))
    list1 = [a1 , a2 , a3 , a4]
    print ("Urutan angka anda ", sorted(list1))
elif a1 == 2:
    a1 = int(input("Masukan Bilangan Bulat Pertama : "))
    a2 = int(input("Masukan Bilangan Bulat Kedua : "))
    a3 = int(input("Masukan Bilangan Bulat Ketiga : "))
    a4 = int(input("Masukan Bilangan Bulat Keempat : "))
    list2 = [a1 , a2 , a3 , a4]
    print ("Urutan bilangan dari kecil ", sorted(list2,reverse=True))
else:
    print ("Input anda salah")