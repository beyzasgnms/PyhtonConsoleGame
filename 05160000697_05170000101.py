def sayi_al(minimum, maksimum):
    try:
        # sayi_al fonksiyonu, int sınıfında 2 parametre alıp kullanıcıdan bu 2 değer arasında bir tamsayı girmesini istiyor
        sayi = int(input())
        # girilen değer aralıkta olmadığı sürece yeniden girilmesi isteniyor
        while sayi < minimum or sayi > maksimum:
            print("Verilen aralığın dışında bir değer girdiniz")
            sayi = int(input("Lütfen geçerli bir sayı giriniz: "))
        # fonksiyon, kullanıcının girdiği değeri döndürüyor
    except ValueError:
        print("Hata!\nGeçersiz bir değer girdiniz")
        quit()
    else:
        return sayi


def oyun_alanini_al():
    # oyun_alanini_al fonksiyonu herhangi bir parametre almıyor
    # sayi_al fonksiyonunu çağırıyor ve kullanıcıdan belirtilen aralıkta satır/sütun sayısı girmesini istiyor
    print("Satır sayısını giriniz (3-7): ", end="")
    satir_sayisi = sayi_al(3, 7)
    print("Sütun sayısını giriniz (3-19): ", end="")
    sutun_sayisi = sayi_al(3, 19)
    # kullanıcıdan aldığı satır ve sütun sayılarını döndürüyor
    return satir_sayisi, sutun_sayisi


def oyuncu_ismi_al():
    # oyuncu_ismi_al fonksiyonu herhangi bir parametre almıyor
    # oyunu oynayacak oyuncuların isimlerini girmelerini istiyor
    oyuncu1 = input("1. Oyuncu, lütfen isminizi giriniz: ")
    oyuncu2 = input("2. Oyuncu, lütfen isminizi giriniz: ")
    # oyunda, tamamlanan karelerin içine oyuncu isimlerinin ilk karakterleri yazdırılacağı için...
    # isimlerin ilk karakterlerinin farklı olması sağlanana kadar 2. ismi yeniden istiyor
    while oyuncu1[0] == oyuncu2[0]:
        print("Oyuncu isimlerinin ilk harfleri aynı olamaz.")
        print("Karakterler büyük/küçük harf duyarlıdır. (Ali ve ali girilebilir)")
        oyuncu2 = input("2. Oyuncu, lütfen isminizi giriniz: ")
    # oyuncu isimlerini ve ilk karakterleri döndürüyor
    return oyuncu1, oyuncu2, oyuncu1[0], oyuncu2[0]


def sutun_harflerini_yaz(sutun_sayisi):
    # sutun_harflerini_yaz fonksiyonu, parametre olarak sütun sayısını alıyor
    # en fazla 19 sütun olabileceği için Latin Alfabesi'ndeki ilk 19 harfi tutan bir listeyi içinde barındırıyor
    harfler = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S"]
    print("    ", end="")
    # döngü, sütun sayısı kez dönerek eksik ya da fazla harf yazılması önleniyor
    for harf_no in range(sutun_sayisi):
        # harfler, harfler listesinin elemanlarının index'i ile yazılıyor
        print("", harfler[harf_no], " ", end="")
    print("")
    # fonksiyon herhangi bir değer döndürülmüyor


def iki_boyutlu_liste_olustur(tek_boyutlu_liste, dis_liste_eleman_say, ic_liste_eleman_say):
    # iki_boyutlu_liste_olustur fonksiyonu; list sınıfında 1, int sınıfında 2 parametre alıyor
    # list parametresi, tek boyutlu bir listeden oluşuyor ve fonksiyon bunu iki boyutluya çeviriyor
    # döngü dış listenin eleman (liste) sayısı kadar dönüyor
    for i in range(dis_liste_eleman_say):
        # içeride ise iç listenin eleman sayısı kadar elemana sahip boş bir liste yaratılıp...
        x = [""] * ic_liste_eleman_say
        # tek boyutlu listeye ekleniyor
        # böylece tek boyutlu listemiz iki boyutlu oluyor
        tek_boyutlu_liste.append(x)
    # fonksiyon, parametre olarak alınan tek boyutlu listeyi iki boyutlu haliyle döndürüyor
    return tek_boyutlu_liste


def hamle_iste(hamle_yapan):
    try:
        # hamle_iste fonksiyonu, parametre olarak yalnızca string sınıfında hamle yapan oyuncunun adını alıyor
        # her sütunun index numarasına karşılık gelen sözlük oluşturuluyor
        sutun_karakter = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11,
                          "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18}
        print()
        # hamle yapan oyuncudan hamle girişi isteniyor
        print(hamle_yapan, ", hamle yapmak için <Sütun><Satır><K|G|D|B> girişi yapınız.", sep="")
        print("Örnek: C3K (C sütunu, 3. satır, Kuzey)")
        hamle = input("Hamleniz: ")
        # hamle girişinin 3 karakterden oluşması bekleniyor
        while len(hamle) != 3:
            print("Hamleniz 3 karakterden oluşmalıdır:")
            print("<Sütun><Satır><K|G|D|B>")
            hamle = input("Hamleniz: ")
        # sözlükte karakterler büyük harfle belirtildiğinden giriş büyük harflere çevriliyor
        hamle = hamle.upper()
        # 3 karakterli giriş ayrı ayrı karakterlere bölünüyor
        hamle_sutun_karakteri, hamle_satir, hamle_cizgi = hamle[0], (hamle[1]), hamle[2]
        # seçilen sütunun hangi index'e denk geldiği belirleniyor
        hamle_sutun = sutun_karakter[hamle_sutun_karakteri]
        # geçersiz çizgi girilmeye çalışıldığında doğru giriş gelene kadar aynı işlemler tekrarlanıyor
        while hamle_cizgi not in ["K", "G", "D", "B"]:
            print("Geçersiz çizgi yeri. Çizgi yerleri K|G|D|B karakterlerinden oluşmalıdır:")
            print("K: Kuzey, G: Güney, D: Doğu, B: Batı")
            hamle = input("Hamleniz: ")
            hamle = hamle.upper()
            hamle_sutun_karakteri, hamle_satir, hamle_cizgi = hamle[0], int(hamle[1]), hamle[2]
            hamle_sutun = sutun_karakter[hamle_sutun_karakteri]
        # fonksiyon hamle girişini ve bölünen karakterleri döndürüyor
        # karakterler index'i temsil ettiklerinden "satir - 1" döndürülüyor
        # (örn: 1. satırın index'i 0)
    except KeyError:
        print("Hata! Geçersiz bir sözlük elemanı girdiniz.")
    else:
        return hamle, int(hamle_sutun), int(hamle_satir) - 1, hamle_cizgi


def ekrana_ciz(satir, sutun, deger, yatay, dikey, oy1, oy2, skor1, skor2):
    # adından da anlaşılabileceği gibi bu fonksiyon oyun alanını ve skoru ekrana çiziyor
    # ekrana_ciz fonksiyonu, toplam 9 parametreye ihtiyaç duyuyor
    # list: 3 | int: 4 | string: 2
    print()
    # skoru ekrana yazarak işleme başlıyor
    print(oy1, skor1, "-", skor2, oy2)

    # daha sonra da sütun harflerini yazan fonksiyonu çağırıyor
    sutun_harflerini_yaz(sutun)

    # oyun alanının en üst ve en alt satırlarında herhangi bir değişiklik olamayacağı için bu satırlar
    # sabit bir stringle yazdırılıyor
    sabit_satir = "    "

    # yatay çizgiler döngüyle string'e ekleniyor
    for a in range(sutun):
        # son çizgilerden sonra boşluk konmuyor
        if a == sutun - 1:
            sabit_satir += "---"
        # diğer çizgiler arasında boşluk olması için burada bir boşluk ekleniyor
        else:
            sabit_satir += "--- "

    # oyun alanındaki satırları ekrana yazdıracak stringler tanımlanıyor
    # biri dikey çizgilerin bulunduğu satırları yazarken diğeri yatay çizgilerin bulunduğu satırları yazıyor
    # satir1 = satir2 = ""

    # yazdırma işlemi for döngüleriyle sağlanıyor
    for i in range(satir):
        if i < 9:
            satir2 = " " + str(i + 1) + " |"
        else:
            satir2 = str(i) + " |"

        satir1 = "    "
        for j in range(sutun):
            # iki boyutlu listelerden yatay çizgileri tutan listenin ilgili elemanında "x" karakteri varsa
            # o elemana denk gelen sütunda yatay çizgi yazılıyor
            if yatay[i][j] != "" and yatay[i][j] == "x":
                satir1 += "--- "
            # "x" karakteri bulunmayan elemanı temsilen boşluk bırakılıyor
            else:
                satir1 += "    "

            satir2 += " "
            # tamamlanan kareye isim yazmak için gereken boşluk oluşturuluyor
            if deger[i][j] != "" and dikey[i][j + 1] == "x":
                satir2 += deger[i][j]
            else:
                satir2 += " "

            # yukarıda yatay çizgiler için yapılan işlemin aynısı dikey çizgiler için de gerçekleştiriliyor
            if dikey[i][j + 1] != "" and dikey[i][j + 1] == "x":
                satir2 += " |"
            else:
                satir2 += "  "

        if satir < 9:
            satir2 += "  " + str(i + 1)
        else:
            satir2 += " " + str(i + 1)
        # satırlar ekrana çizdiriliyor
        print(satir1)
        if i < satir:
            print(satir2)
    # en alt satır çizdirilip altına harfler yazılıyor
    print(sabit_satir)
    sutun_harflerini_yaz(sutun)
    # fonksiyon herhangi bir değer döndürmüyor


def main():
    try:
        # main fonksiyonu, oyunu çalıştıran ana fonksiyon
        # öncelikle kullanıcıdan oyun alanının büyüklüğü isteniyor
        satir_sayisi, sutun_sayisi = oyun_alanini_al()
        # sonra da oyunu oynayacak olan oyuncuların isimleri alınıyor
        player1, player2, karakter1, karakter2 = oyuncu_ismi_al()
        # iki boyutluya dönüştürmek için kullanılacak olan tek boyutlu listeler oluşturuluyor
        # değer listesi, tamamlanan karenin içinin dolu olup olmadığını kontrol ediyor
        deger_listesi = []
        # yatay çizgi listesi, yatay çizgilerin konumlarını tutuyor
        yatay_cizgi = []
        # dikey çizgi listesi, dikey çizgilerin konumlarını tutuyor
        dikey_cizgi = []
        # listeler gereken şekilde iki boyutluya çevriliyor
        deger_listesi = iki_boyutlu_liste_olustur(deger_listesi, satir_sayisi, sutun_sayisi)
        yatay_cizgi = iki_boyutlu_liste_olustur(yatay_cizgi, satir_sayisi + 1, sutun_sayisi + 1)
        dikey_cizgi = iki_boyutlu_liste_olustur(dikey_cizgi, satir_sayisi + 1, sutun_sayisi + 1)

        # yatay çizgi bulunması gereken yerlerin indexleri işaretleniyor
        for i in range(sutun_sayisi):
            yatay_cizgi[0][i] = "x"
            yatay_cizgi[satir_sayisi][i] = "x"

        # dikey çizgi bulunması gereken yerlerin indexleri işaretleniyor
        for j in range(satir_sayisi):
            dikey_cizgi[j][0] = "x"
            dikey_cizgi[j][sutun_sayisi] = "x"

        # oyun bir döngüyle devam edeceği için boolean bir değişken tanımlanıyor
        oyun_bitti = False
        # kare tamamlayan oyuncunun oyuna devam etmesini sağlayacak bir değişken tanımlanıyor
        oyuncu_degistir = True
        # oyuncu_degistir boolean'ı True olarak tanımlandığından hamle yapan oyuncu, 2. oyuncu olarak belirtiliyor
        hamle_yapan = player2
        # oyuncuların skorları tutuluyor
        skor1 = skor2 = 0

        while not oyun_bitti:
            if oyuncu_degistir:
                if hamle_yapan == player1:
                    hamle_yapan = player2
                else:
                    hamle_yapan = player1
            oyuncu_degistir = True

            # oyun alanı ve skor bilgisi ekrana yazdırılıyor
            ekrana_ciz(satir_sayisi, sutun_sayisi, deger_listesi, yatay_cizgi, dikey_cizgi, player1, player2, skor1, skor2)
            # programın döngüye girmesi için hamle değişkeni başta tanımlanıyor
            hamle = ""
            while hamle == "":
                # oyuncudan hamle girişi isteniyor
                hamle, hamle_sutun, hamle_satir, hamle_cizgi = hamle_iste(hamle_yapan)

                if hamle_cizgi == "K":
                    # hamle girişi yapılan yerin durumu kontrol ediliyor
                    # eğer giriş yapılan yerde zaten çizgi varsa yeniden giriş isteniyor
                    if yatay_cizgi[hamle_satir][hamle_sutun] != "" and yatay_cizgi[hamle_satir][hamle_sutun] == "x":
                        print("Hamle yapılan yer dolu.")
                        hamle = ""
                    else:
                        # giriş yapılan yer boş ise ilgili index dolduruluyor
                        yatay_cizgi[hamle_satir][hamle_sutun] = "x"

                elif hamle_cizgi == "G":
                    # hamle girişi yapılan yerin durumu kontrol ediliyor
                    # eğer giriş yapılan yerde zaten çizgi varsa yeniden giriş isteniyor
                    if yatay_cizgi[hamle_satir + 1][hamle_sutun] != "" and yatay_cizgi[hamle_satir + 1][hamle_sutun] == "x":
                        print("Hamle yapılan yer dolu.")
                        hamle = ""
                    else:
                        # giriş yapılan yer boş ise ilgili index dolduruluyor
                        yatay_cizgi[hamle_satir + 1][hamle_sutun] = "x"

                elif hamle_cizgi == "D":
                    # hamle girişi yapılan yerin durumu kontrol ediliyor
                    # eğer giriş yapılan yerde zaten çizgi varsa yeniden giriş isteniyor
                    if dikey_cizgi[hamle_satir][hamle_sutun + 1] != "" and dikey_cizgi[hamle_satir][hamle_sutun + 1] == "x":
                        print("Hamle yapılan yer dolu.")
                        hamle = ""
                    else:
                        dikey_cizgi[hamle_satir][hamle_sutun + 1] = "x"

                elif hamle_cizgi == "B":
                    # hamle girişi yapılan yerin durumu kontrol ediliyor
                    # eğer giriş yapılan yerde zaten çizgi varsa yeniden giriş isteniyor
                    if dikey_cizgi[hamle_satir][hamle_sutun] != "" and dikey_cizgi[hamle_satir][hamle_sutun] == "x":
                        print("Hamle yapılan yer dolu.")
                        hamle = ""
                    else:
                        # giriş yapılan yer boş ise ilgili index dolduruluyor
                        dikey_cizgi[hamle_satir][hamle_sutun] = "x"

            # kapanan kare olup olmadığı kontrol ediliyor
            for i in range(satir_sayisi):
                for j in range(sutun_sayisi):
                    if yatay_cizgi[i][j] != "" and yatay_cizgi[i][j] == "x":
                        if yatay_cizgi[i + 1][j] != "" and yatay_cizgi[i + 1][j] == "x":
                            if dikey_cizgi[i][j] != "" and dikey_cizgi[i][j] == "x":
                                if dikey_cizgi[i][j + 1] != "" and dikey_cizgi[i][j + 1] == "x":
                                    if deger_listesi[i][j] in ["", " "]:
                                        # eğer yeni bir kare kapandıysa sıranın diğer oyuncuya geçmemesi sağlanıyor
                                        oyuncu_degistir = False
                                        # kareyi kapatan oyuncunun karakteri yazılıyor
                                        # ve skoru artırılıyor
                                        if hamle_yapan == player1:
                                            deger_listesi[i][j] = karakter1
                                            skor1 += 1
                                        else:
                                            deger_listesi[i][j] = karakter2
                                            skor2 += 1

            # oyunun bitip bitmediği kontrol ediliyor
            toplam_skor = skor1 + skor2
            toplam_kare = satir_sayisi * sutun_sayisi
            if toplam_kare == toplam_skor:
                oyun_bitti = True

        # oyun bittikten sonra oyun alanının son hali ve skor bilgisi ekrana yazdırılıyor
        ekrana_ciz(satir_sayisi, sutun_sayisi, deger_listesi, yatay_cizgi, dikey_cizgi, player1, player2, skor1, skor2)

        # sonuç ekranı yazdırılıyor
        print("Oyun Bitti")
        print("Sonuç:", player1, skor1, "-", skor2, player2)
        if skor1 > skor2:
            print("Kazanan ", player1, "!", sep="")
        elif skor2 > skor1:
            print("Kazanan ", player2, "!", sep="")
        else:
            print("Berabere!")
    except IndexError:
        print("Hata! Geçersiz bir liste elemanı girdiniz.")
    except TypeError:
        print("Hata! Girilen nesne yinelenebilir değil.")


main()
