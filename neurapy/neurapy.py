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

print("NEURAPY'A HOŞ GELDİNİZ !")
class Neurapy():
    def __init__ (self, sistem= 'Kapalı'):
        self.sistem= sistem
    
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
    
    def menu_yazdırma(self):

        if self.sistem == 'Kapalı':
            print('Lütfen önce sistemi açın.')
        
        else:
            file_path = 'menu_dataset.csv'
            df = pd.read_csv(file_path)
            for i , a in zip(df['YEMEK ADI'], df['İÇERİK']):
                print(i, '\n -', a)
    
    def icerige_gore_oneri(self):

        file_path = 'menu_dataset.csv'

        df = pd.read_csv(file_path)

        kullanici_listesi = input("Yemekte bulunmasını istediğiniz ürün/ürünlerin ismini (virgülle ayrılmış) giriniz:  \n").split(',')

        def benzerlik_kontrolu(veri1, veri2):
            return veri1 == veri2

        benzerlik_sonuclari = []

        index = -1
        for hücre_verisi in df['İÇERİK']:
                veriler = str(hücre_verisi).split(',')
                veriler = [veri.strip() for veri in veriler]  
                sayac = 0
                index += 1
                for veri in veriler: 
                        for kullanıcı_verisi in kullanici_listesi:
                            kullanıcı_verisi = kullanıcı_verisi.strip()
                            oran = benzerlik_kontrolu(kullanıcı_verisi, veri)
                            if oran == True:
                                sayac += 1
                if sayac != 0:
                    benzerlik_sonuclari.append({
                                    'sayac': sayac, 
                                    'index': index  
                })

        benzerlik_sonuclari.sort(key=lambda x:x['sayac'])
        sonuc_df = pd.DataFrame(benzerlik_sonuclari)
        print('\n')
        a = sonuc_df.tail(5)
        
        for index in a['index']:
            print('Yemek Adı: ' ,df['YEMEK ADI'][index], '   Yemeğin Fiyatı: ', df['FİYAT'][index],  '\n -', 'Yemeğin İçeriği: ', df['İÇERİK'][index], '\n')
        satin_alma = input('Önerilenlerden satın almak istediğiniz yemek var mı?(evet/hayır): ').lower()
        if satin_alma == 'evet':
            satin_alinan = input('Satın almak istediğiniz yemek(lerin) adını giriniz (küçük harflelerle ve virgülle ayırarak girebilirsiniz): ').split(',') 
            satin_alinan = [a.strip() for a in satin_alinan]
        toplam = 0
        df['YEMEK ADI'] = df['YEMEK ADI'].str.lower()
        for i in satin_alinan:
            satir = df[df['YEMEK ADI'] == i]
            if not satir.empty:
                 fiyat = satir['FİYAT'].values[0]
                 toplam += fiyat
                 print(fiyat) 
        print('Yemeklerinizin toplam fiyatı: ', toplam)
        onay = input('Siparişinizi onaylıyor musunuz(evet/hayır? ').lower()
        if onay == 'evet':
            print("yemekler sepete eklendi ! Başka bir yemek eklemek isterseniz ana menüden 'yemek ekle' işlemini seçiniz.")
            return toplam
        elif onay == 'hayır':
            print('İşlemlerinizi tekrar girebilmek için')
        else:
            print ('İşleminiz iptal oldu.')


    def yemege_gore_oneri(self):
        df = pd.read_csv("menu_dataset.csv")
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
                                islem_onay=input("sepete ekleme işlemini onaylıyor musunuz ? (evet/hayır)").lower()
                                if islem_onay=="evet":
                                     print("yemekler sepete eklendi ! Başka bir yemek eklemek isterseniz ana menüden 'yemek ekle' işlemini seçiniz.")
                                     return ara_toplam
                                break
                    else:
                        print("Ana Menüye Yönlendiriliyorsunuz...")
                        break
                    
                elif girdi_al=="q":
                    print("Ana Menüye Yönlendiriliyorsunuz...")
                    break

                else:
                    print("menümüzde böyle bir yemek bulunmamaktadır. Tekrar deneyiniz. (Çıkmak için q'ya basınız.)")


    def yemek_ekle(self):
         df = pd.read_csv("menu_dataset.csv")
         yemek_listesi={}
         yemek_isimleri=input("eklemek istediğiniz yemek/yemeklerin adını (virgülle ayırarak) giriniz:").lower()
         yemek_isimleri=[n.strip() for n in yemek_isimleri.split(",")]
         df["YEMEK ADI"]=df["YEMEK ADI"].str.lower().values
         for yemek in yemek_isimleri:
            if yemek in df["YEMEK ADI"]:
                fiyat = df.loc[df["YEMEK ADI"] == yemek, "FİYAT"].values
                yemek_listesi[yemek] = fiyat
         yemek_listesi=pd.DataFrame(yemek_listesi)
         print(yemek_listesi)




                            
a = Neurapy()

print("""
      Neurapy'a Hoş Geldiniz !
      Hangi işlemi yapmak istersiniz ?
      1.Makine açma
      2.Makine Kapatma
      3.Menü Yazdırma
      4.Yemek İçeriğine Göre Yemek Önerisi Alma
      5.Yemeğe Göre Öneri Alma
      6.Yemek Ekle""")
    
while True:
    islem = input("Sistemi açmak için 1, kapatmak için 2'ye basabilirsiniz.\n")
    if islem == '1':
        a.sistem_acma()

    elif islem == '2':
        a.sistem_kapat()

    elif islem == '3':
        a.menu_yazdırma()
    
    elif islem == '4':
        a.icerige_gore_oneri()


    elif islem == '5':
         a.yemege_gore_oneri()