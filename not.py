while True:
    try:
        a= int(input("LÜTFEN NOT GİRİNİZ"))
    except ValueError:
        print("LÜTFEN SADECE SAYI GİRİNİZ")
         
    with open("girdi2.txt","a") as f:
        f.write(str(a))
    
    
    if a == 505 :
        break

    if 100 < a or 0>a:
        print("100 VE 0 ARALIĞINDA BİR SAYI GİRİNİZ")

    if 100 >= a and 87 <= a:
        a1=("AA")
        print(a1)
        with open("sonuc2.txt","a") as w:
            w.write(a1)
    if 86 >= a and 81 <= a:
        a2=("BA")
        print(a2)
        with open("sonuc2.txt","a") as w:
            w.write(a2)
    if 80 >= a and 74 <= a:
        a3=("BB")
        print(a3)
        with open("sonuc2.txt","a") as w:
            w.write(a3)
    if 73 >= a and 67 <= a:
        a4=("CB")
        print(a4)
        with open("sonuc2.txt","a") as w:
            w.write(a4)
    if 66 >= a and 60 <= a:
        a5=("CC")
        print(a5)
        with open("sonuc2.txt","a") as w:
            w.write(a5)
    if 59 >= a and 53 <= a:
        a6=("DC")
        print(a6)
        with open("sonuc2.txt","a") as w:
            w.write(a6)        
    if 52 >= a and 46 <= a:
        a7=("DD")
        print(a7)
        with open("sonuc2.txt","a") as w:
            w.write(a7)
    if 45 >= a and 39 <= a:
        a8=("FD")
        print(a8)
        with open("sonuc2.txt","a") as w:
            w.write(a8)
    if 38 >= a and 0 <= a:
        a9=("FF")
        print(a9)    
        with open("sonuc2.txt","a") as w:
            w.write(a9)
   
while True:
    g= str(input("YAPMAK İSTEDİĞİNİZ İŞLEMİ YAZINIZ"))

    if g== "dur":
        print("Döngü durduruldu")
        break
    if g == "Girdi dosyasını temizle":
        with open("girdi2.txt","w") as f:
            f.write("")
        print("DOSYA TEMİZLENDİ")
    if g== "Sonuç dosyasını temizle":
      with open("sonuc2.txt","w") as w:
          w.write("")
      print("DOSYA TEMİZLENDİ")


