# menü yazdırma/öneri alma
# öneri yapma (girdi al, menüden benzerlik hesaplama (cosine benzerlik formülünü yazdığımız bir sınıf oluşturarak yapabiliriz.), öneri listesi sunma)
# önerilerden satın almak isteyip istemediğini öğrenelim
# öneriler içinden almak istediklerini seçtirme (fiyat hesaplama)
# fiyat sunma
# ekstra menüden almak istedikleri var mı diye soru sorma
# varsa onları da alıp tekrar fiyat hesaplama
# ödemeyi alma

import pandas as pd
import numpy as np
import time

class Neurapy():
    def __init__ (self, sistem= 'Kapalı'):
        self.sistem= sistem
        self.toplam=0
    
    def sistem_acma(self):
        if self.sistem == 'Açık':
            return 'Sistem zaten açık'
        else:
            print("Sistem açılıyor...")
            self.sistem = 'Açık'
            return (self.sistem)
        
    def sistem_kapat(self):
        if self.sistem == 'Kapalı':
            return 'Sistem zaten kapalı'
        else:
            print("Sistem kapatılıyor...")
            self.sistem = 'Kapalı'
            return "NeuraPy'a geldiğiniz için teşekkürler, iyi günler dileriz.."
    
    def menu_yazdirma(self):

        if self.sistem == 'Kapalı':
            print('Lütfen önce sistemi açın.')
        
        else:
            file_path = "neurapy/neurapy/menu_dataset.csv"
            df = pd.read_csv(file_path)
            for i , a in zip(df['YEMEK ADI'], df['İÇERİK']):
                print(i, '\n -', a)
    
    def icerige_gore_oneri(self):

        if self.sistem == 'Kapalı':
            print('Lütfen önce sistemi açın.')
        else:

            file_path = "neurapy/neurapy/menu_dataset.csv"

            df = pd.read_csv(file_path)

        for i , a in zip(df['YEMEK ADI'], df['İÇERİK']):
            print(i, '\n -', a)


        kullanici_listesi = input("yemekte bulunmasını istediğiniz ürün/ürünlerin adını (virgülle ayrılmış) girin:  \n").split(',')

        def benzerlik_kontrolü(veri1, veri2):
            return veri1 == veri2

        benzerlik_sonuçları = []

        index = -1
        for hücre_verisi in df['İÇERİK']:
                veriler = str(hücre_verisi).split(',')
                veriler = [veri.strip() for veri in veriler]  
                sayac = 0
                index += 1
                for veri in veriler: 
                        for kullanıcı_verisi in kullanici_listesi:
                            kullanıcı_verisi = kullanıcı_verisi.strip()
                            oran = benzerlik_kontrolü(kullanıcı_verisi, veri)
                            if oran == True:
                                sayac += 1
                if sayac != 0:
                    benzerlik_sonuçları.append({
                                    'sayac': sayac, 
                                    'index': index  
                })

        benzerlik_sonuçları.sort(key=lambda x:x['sayac'])


        sonuç_df = pd.DataFrame(benzerlik_sonuçları)
        print('\n')
        a = sonuç_df.tail(5)
        for index in a['index']:
            print('Yemek Adı: ' ,df['YEMEK ADI'][index], '   Yemeğin Fiyatı: ', df['FİYAT'][index],  '\n -', 'Yemeğin İçeriği: ', df['İÇERİK'][index], '\n')
        satın_alma = input('Önerilenlerden satın almak istediğiniz yemek var mı?(evet/hayır): ').lower()
        if satın_alma == 'evet':
            satın_alınan = input('Satın almak istediğiniz yemeği ya da yemek/yemeklerin adını giriniz (virgülle ayırarak): ').lower()
            satın_alınan = [a.strip() for a in satın_alınan.split(",")]
        toplam = 0
        df['YEMEK ADI'] = df['YEMEK ADI'].str.lower()
        
        self.toplam+=toplam
        print('Yemeklerinizin toplam fiyatı: ', toplam)
        islem_onay=input("başka bir işlem yapmak istiyor musunuz ? (evet/hayır)").lower()
        if islem_onay=="evet":
            print("yemekler sepete eklendi ! menüden başka bir yemek eklemek isterseniz ana menüden 'Yemek Ekle' işlemini seçiniz.")
        elif islem_onay=="hayır":
            odeme_onay=input("ödemeyi onaylıyor musunuz ? (evet/hayır)").lower()
            if odeme_onay=="evet":
                print("Ödemeniz onaylandı ! İyi günler diler, Neurapy'a yine bekleriz.")
            elif odeme_onay=="hayır":
                print("ödeme onaylanmadı. ana menüye dönülüyor...")
                time.sleep(1)
            else:
                print("hatalı girdi.")
        


    def yemege_gore_oneri(self):
        
        if self.sistem == 'Kapalı':
            print('Lütfen önce sistemi açın.')
        else:
            df = pd.read_csv("neurapy/neurapy/menu_dataset.csv")
            df.set_index("YEMEK ADI", inplace=True)
            df.index = df.index.str.lower()

            while True:
                    girdi_al = input("Menümüzden beğendiğiniz bir yemeğin adını giriniz (küçük harflerle giriniz):")

                    if girdi_al in df.index:
                        oneri_list = []
                        girdi_set = str(df.loc[girdi_al].values[1]).split(",")
                        girdi_set.append(df.loc[girdi_al].values[0])
                        girdi_set.append(df.loc[girdi_al].values[2])

                        for index, row in df.iterrows():
                            menu_pisme = row.values[0]
                            menu_tur= row.values[2]
                            veriler = str(row.values[1]).split(",")
                            veriler.append(menu_pisme)
                            veriler.append(menu_tur)
                            kesisim_bul=np.intersect1d(veriler,girdi_set)

                            oneri_list.append({
                                "yemek adı": index,
                                "yemek fiyatı": row["FİYAT"],
                                "benzerlik miktarı": len(kesisim_bul)})
                            
                        df_oneri=oneri_list.sort(key=lambda x:x["benzerlik miktarı"])
                        oneri_list.pop()
                        df_oneri=pd.DataFrame(oneri_list)
                        print(df_oneri.tail(5))

                        satin_al_sor=input("önerilenlerden satın almak istediğiniz bir yemek var mı ? (evet/hayır").lower()
                        if satin_al_sor=="evet":
                            ara_toplam=0
                            satin_al=input("hangi yiyecekleri satın almak istiyorsunuz ? numarasını giriniz:")

                            satin_al = str(satin_al).split(",")
                            satin_al=[int(b) for b in satin_al]
                            fiyatlar=[]
                            for c in satin_al:
                                c=df_oneri.loc[c].values[1]
                                fiyatlar.append(c)
                            ara_toplam+=sum(fiyatlar)
                            print(f"toplam ücret: {ara_toplam}")
                            self.toplam+=ara_toplam
                            islem_onay=input("başka bir işlem yapmak istiyor musunuz ? (evet/hayır)").lower()
                            if islem_onay=="evet":
                                print("yemekler sepete eklendi ! menüden başka bir yemek eklemek isterseniz ana menüden 'Yemek Ekle' işlemini seçiniz.")
                            elif islem_onay=="hayır":
                                odeme_onay=input("ödemeyi onaylıyor musunuz ? (evet/hayır)").lower()
                                if odeme_onay=="evet":
                                    print("Ödemeniz onaylandı ! İyi günler diler, Neurapy'a yine bekleriz.")
                                    break
                                elif odeme_onay=="hayır":
                                    print("ödeme onaylanmadı. ana menüye dönülüyor...")
                                else:
                                    print("hatalı girdi.")
                            else:
                                print("hatalı girdi.")
                    
                    elif girdi_al=="q":
                        break

                    else:
                        print("menümüzde böyle bir yemek bulunmamaktadır. Tekrar deneyiniz. (Çıkmak için q'ya basınız.)")


    def yemek_ekle(self):
        df = pd.read_csv("neurapy/neurapy/menu_dataset.csv")
        fiyat_list=[]
        yemek_isimleri=input("eklemek istediğiniz yemek/yemeklerin adını (virgülle ayırarak) giriniz:").lower()
        yemek_isimleri=[n.strip() for n in yemek_isimleri.split(",")]
        df["YEMEK ADI"]=df["YEMEK ADI"].str.lower().values
        for yemek, fiyat in df.iterrows():
            if yemek in df["YEMEK ADI"]:
                fiyat_list.append(fiyat.values[4])
        yemek_listesi=dict(zip(yemek_isimleri,fiyat_list)) 
        yemek_listesi_df=pd.DataFrame(yemek_listesi.items(), columns= ["YEMEK ADI", "FİYAT"])
        print(yemek_listesi_df)
        toplam_ekle=yemek_listesi_df["FİYAT"].sum()
        print(f"eklenecek ücret: {toplam_ekle}")
        self.toplam+=toplam_ekle
        print(f"TOPLAM: {self.toplam}")
        islem_onay=input("başka bir işlem yapmak istiyor musunuz ? (evet/hayır)").lower()      
        if islem_onay=="evet":
            print("yemekler sepete eklendi !")
            odeme_onay=input("ödemeyi onaylıyor musunuz ? (evet/hayır)").lower()
            if odeme_onay=="evet":
                print("Ödemeniz onaylandı ! İyi günler diler, Neurapy'a yine bekleriz.")
            elif odeme_onay=="hayır":
                print("ödeme onaylanmadı. ana menüye dönülüyor...")
                time.sleep(1)
            else:
                print("hatalı girdi.")
        elif islem_onay=="hayır":
            print("işlem onaylanmadı. ana menüye dönülüyor...")
            time.sleep(1)
        else:
            print("hatalı girdi.")         
                    
a = Neurapy()

print("""
      Neurapy'a Hoş Geldiniz !
      Hangi işlemi yapmak istersiniz ?
      1.Sistem açma
      2.Sistem Kapatma
      3.Menü Yazdırma
      4.Yemek İçeriğine Göre Yemek Önerisi Alma
      5.Yemeğe Göre Öneri Alma
      6.Yemek Ekle""")
    
while True:
    islem = int(input("""Sistemi açmak için 1, kapatmak için 2'ye basabilirsiniz. 
Menüyü yazdırmak için 3 basın. İçeriğe göre öneri almak için 4 basınız.
Yemeğe göre öneri için 5 basabilirsiniz. \n """))
    
    try:
        if islem == 1:
            a.sistem_acma()

        elif islem == 2:
            a.sistem_kapat()
            break

        elif islem == 3:
            a.menu_yazdirma()
        
        elif islem == 4:
            a.icerige_gore_oneri()

        elif islem == 5:
            a.yemege_gore_oneri()
        
        elif islem== 6:
            a.yemek_ekle()

    except ValueError:
        print("Hatalı işlem.")