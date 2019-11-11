print("Masukan 3 Bilangan Yang Di Inginkan")

A= int(input("Masukan Bilangan Pertama : "))
B= int(input("Masukan Bilangan Kedua   : "))
C= int(input("Masukan Bilangan Ketiga  : "))

if A > B and A > C:
    print(A, "Terbesar Dari 3 Bilangan Yang Di Inputkan")
elif B > A and B > C:
    print(B, "Terbesar Dari 3 Bilangan Yang Di Inputkan")
else:
    print(C, "Terbesar Dari 3 Bilangan Yang Di Inputkan")
