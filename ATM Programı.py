print("""------------------

ATM Programına Hoş Geldiniz

Yapabileceğiniz İşlemler:

İşlem Kodu      İşlem Adı
     1.         Para Çekme
     2.         Para Yatırma
     3.         Bakiye Sorgulama
     4.         Çıkış
-------------------
""")

bakiye=int(1000)

while True:
    işlem= int(input("Yapmak İstediğiniz İşlemin Kodunu Giriniz:"))
    if  işlem==1:
        para_çekme=int(input("Çekmek İstediğiniz Tutarı Giriniz:"))
        if bakiye-para_çekme>=0:
            bakiye-=para_çekme
            print("Bakiyeniz {} TL'dir".format(bakiye))
        elif    bakiye-para_çekme<=0:
            print("Lütfen Başka Bir İşlem Seçiniz")
            continue
    elif  işlem==2:
        para_yatırma=int(input("Yatımak İstediğiniz Tutarı Yazınız:"))
        bakiye+=para_yatırma
        print("Bakiyeniz {} TL'dir".format(bakiye))
        continue
    elif işlem==3:
        print(bakiye)
        continue
    elif işlem==str("q":)
        print("Tekrar Bekleriz")
        break
    else:
        print("Lütfen Geçerli Bir İşlem Kodu Seçiniz")
        continue