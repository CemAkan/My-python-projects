class ürün:
    fiyat=0
    agırlık=0
    renk=""
    tür=""

muz = ürün()
muz.fiyat=6
muz.tür="anamur yerli"
muz.renk="sarı"
muz.agırlık=0.100

bebekbezi = ürün()
bebekbezi.fiyat=129
bebekbezi.tür="5 aylık"
bebekbezi.renk="beyaz"
bebekbezi.agırlık=8.100

elma = ürün()
elma.fiyat=21
elma.tür="amasya yerli"
elma.renk="yeşil"
elma.agırlık=1.130

et = ürün()
et.fiyat=100
et.tür="yerli besi"
et.renk="kırmızı"
et.agırlık=1.000

makarna = ürün()
makarna.fiyat=9
makarna.tür="fiyonk"
makarna.renk="sarı"
makarna.agırlık=0.500

soda = ürün()
soda.fiyat=2
soda.tür="limonlu"
soda.renk="saydam"
soda.agırlık=0.256

anahtarlık = ürün()
anahtarlık.fiyat=10
anahtarlık.tür="metal"
anahtarlık.renk="gri"
anahtarlık.agırlık=0.305

semsiye = ürün()
semsiye.fiyat=39
semsiye.tür="tam otomatik"
semsiye.renk="siyah"
semsiye.agırlık=0.600

biskuvi = ürün()
biskuvi.fiyat=4
biskuvi.tür="çikolatalı"
biskuvi.renk="siyah"
biskuvi.agırlık=0.120

su = ürün()
su.fiyat=1
su.tür="mineralli"
su.renk="saydam"
su.agırlık=0.300


while True:
    a= str(input("LÜTFEN ÜRÜN GİRİNİZ"))
    if type(a)==int:
        print("LÜTFEN RAKAM GİRMEYİNİZ")


    if a != "muz":
        if a!= "su":
            if a!= "bebekbezi":
                if a!= "semsiye":
                    if a!= "elma":
                        if a!= "soda":
                            if a!= "et":
                                if a!= "makarna":
                                    if a!= "biskuvi":
                                        if a!= "anahtarlık":
                                             print("TANIMLI BİR ÜRÜN GİR")
                                        

    with open("girdi.txt","a") as f:
        f.write(str(a))
        f.write("\n")
    
   
    if a=="dur":
        break
    elif a=="yardım":
        print("İŞLEMİ DURDURMAK İÇİN (dur) YAZINIZ. \n DİĞER İŞLEMLER İÇİN LÜTFEN SADECE İLK HARFİ BÜYÜK SONRAKİ HARFLERİ KÜÇÜK OLACAK ŞEKİLDE YAZINIZ \n TÜRKÇE KARAKTER KULLANINIZ ")
    elif a=="yapımcı":
        print("twitter: @Cem__akan")


t=0
k=0
float(k)
renkler = []
turler = []

with open("girdi.txt","r") as f:
    icerik = f.readlines()
    
    for x in icerik:
        if x == "muz\n":
            t=t+muz.fiyat
            k=k+muz.agırlık
            renkler.append(muz.renk)
            turler.append(muz.tür)
        elif x == "bebekbezi\n":
            t=t+bebekbezi.fiyat
            k=k+bebekbezi.agırlık
            renkler.append(bebekbezi.renk)
            turler.append(bebekbezi.tür)
        elif x == "et\n":
            t=t+et.fiyat
            k=k+et.agırlık
            renkler.append(et.renk)
            turler.append(et.tür)
        elif x== "semsiye\n":
            t=t+semsiye.fiyat 
            k=k+semsiye.agırlık  
            renkler.append(semsiye.renk)
            turler.append(semsiye.tür)
        elif x == "soda\n":
            t=t+soda.fiyat
            k=k+soda.agırlık
            renkler.append(soda.renk)
            turler.append(soda.tür)
        elif x == "biskuvi\n":
            t=t+biskuvi.fiyat
            k=k+biskuvi.agırlık
            renkler.append(biskuvi.renk)
            turler.append(biskuvi.tür)
        elif x == "anahtarlık\n":
            t=t+anahtarlık.fiyat
            k=k+anahtarlık.agırlık
            renkler.append(anahtarlık.renk)
            turler.append(anahtarlık.tür)
        elif x == "elma\n":
            t=t+elma.fiyat
            k=k+elma.agırlık
            renkler.append(elma.renk)
            turler.append(elma.tür)
        elif x == "makarna\n":
            t=t+makarna.fiyat
            k=k+makarna.agırlık
            renkler.append(makarna.renk),
            turler.append(makarna.tür)
        elif x == "su\n":
            t=t+su.fiyat
            k=k+su.agırlık
            renkler.append(su.renk)
            turler.append(su.tür)

while True:
    g= str(input("YAPMAK İSTEDİĞİNİZ İŞLEMİ YAZINIZ"))


    if g == "Toplam":
        print("TOPLAM FİYAT",t,"TL")
        with open("sonuc.txt","a") as w:
            w.write(str(t))
            w.write("\n")

    if g == "Türler":
        print("ALDIĞINIZ ÜRÜNLERİN RENKLERİ",turler)
        with open("sonuc.txt","a") as w:
            w.write(str(turler))
            w.write("\n")

    if g == "Renkler":
        print("ALDIĞINIZ ÜRÜNLERİN RENKLERİ",renkler)
        with open("sonuc.txt","a") as w:
          w.write(str(renkler))
          w.write("\n")

    if g == "Agırlık":
        print("TOPLAM AĞIRLIK",k)
        with open("sonuc.txt","a") as w:
            w.write(str(k))
            w.write("\n")
    if g == "Girdi dosyasını temizle":
        with open("girdi.txt","w") as f:
            f.write("")
        print("DOSYA TEMİZLENDİ")

    if g== "Sonuç dosyasını temizle":
      with open("sonuc.txt","w") as w:
          w.write("")
      print("DOSYA TEMİZLENDİ")

    if g== "Kalanı hesapla":
      s=  int(input("BAKİYENİZİ GİRİNİZ"))
      print("KALAN PARANIZ",s-t,"TL'DİR.")

    if g== "dur":
        print("DÖNGÜ DURDURULDU.")
        break


