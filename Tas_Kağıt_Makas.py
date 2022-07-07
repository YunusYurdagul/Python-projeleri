import random
print("Taş:1\nKağıt:2\nMakas:3\nÇıkış:4")
Seçenek = [1,2,3]
while True:
    seçim = int(input("Taş,Kağıt,Makas? ya da Çıkış:"))
    pc = random.choice(Seçenek)
    if seçim == 1:
        if pc == 1:
            print("Bilgisayarın seçimi taş")
            print("Berabere!")

        elif pc == 2:
            print("Bilgisayarın seçimi kağıt")
            print("Kaybettiniz!")

        else:
            print("Bilgisayarın seçimi makas")
            print("Kazandınız!")

    elif seçim == 2:
        if pc == 1:
            print("Bilgisayarın seçimi taş")
            print("Kazandınız!")

        elif pc == 2:
            print("Bilgisayarın seçimi kağıt")
            print("Berabere!")

        else:
            print("Bilgisayarın seçimi makas")
            print("Kaybettiniz!")

    elif seçim == 3:
        if pc == 1:
            print("Bilgisayarın seçimi taş")
            print("Kaybettiniz!")

        elif pc == 2:
            print("Bilgisayarın seçimi kağıt")
            print("Kazandınız!")

        else:
            print("Bilgisayarın seçimi makas")
            print("Berabere!")

    elif seçim == 4:
        print("Oyunu kapattınız!")
        break

    else:
        print("Lütfen geçerli bir rakam girin")

