
print(f"""\n---PROGRAM KONVERSI BILANGAN---
1 -> Desimal ke Biner
2 -> Biner ke Desimal
3 -> Exit""")
pilihan = int(input("Silahkan pilih menu : "))

if pilihan == 1:
    a = int(input("Masukkan bilangan desimal : "))
    b = bin(a) .replace("0b","")
    print(b)

elif pilihan == 2:
    a = int(input("Masukkan bilangan biner: "),2)
    print(a)

elif pilihan == 3:
    print("Terima kasih telah menggunakan program ini!")
    exit()
