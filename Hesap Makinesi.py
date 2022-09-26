
z=input("YAPMAK İSTEDİĞİNİZ İŞLEMİ YAZINIZ --> ") 


if z == "TOPLAMA" or z == "ÇIKARMA" or z == "BÖLME" or z == "ÇARPMA" or z == "ÜST ALMA" or z == "YÜZDE":

    x=int(input("İLK DEĞERİ GİRİNİZ --> "))
    y=int(input("İKİNCİ DEĞERİ GİRİNİZ --> "))
 
 
    if z == "TOPLAMA":
        def toplama(x,y):
            islem1=x+y
            print("İŞLEMİNİZİN CEVABI "+str(islem1))
        toplama(x,y)

    elif z == "ÇIKARMA":
        def cikarma(x,y):
            islem2=x-y
            print("İŞLEMİNİZİN CEVABI "+str(islem2))
        cikarma(x,y)

    elif z == "BÖLME":
        def bolme(x,y):
            islem3=x/y
            print("İŞLEMİNİZİN CEVABI "+str(islem3))
        bolme(x,y)

    elif z == "ÇARPMA":
        def carpma(x,y):
            islem4=x*y
            print("İŞLEMİNİZİN CEVABI "+str(islem4))
        carpma(x,y)

    elif z == "ÜST ALMA":
        def ustalma(x,y):
            islem5=x**y
            print("İŞLEMİNİZİN CEVABI "+str(islem5))
        ustalma(x,y)

    elif z == "YÜZDE":
        def yuzde(x,y):
            islem6=x*y/100
            print("İŞLEMİNİZİN CEVABI "+str(islem6))
        yuzde(x,y)

elif z==("YARDIM"):
    print("CAPLOSK AÇIK VE TÜRKÇE KAREKTERLE YAZINIZ. DAHA FAZLA PROBLEM YAŞARSANIZ = Twitter: @Cem__akan ")

elif z==("YAPIMCI"):
    print("Twitter: @Cem__akan")

else:
    print("İŞLEMİNİZ YANLIŞ, LÜTFEN, TEKRAR DENEYİNİZ")
