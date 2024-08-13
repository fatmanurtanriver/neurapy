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
    def __init__ (self, sistemi_acma = 'Kapalı'):
        self.sistemi_acma= sistemi_acma
    
    def sistem_acma(self):
        if self.sistemi_acma == 'Açık':
            return 'Sistem zaten açık'
        else:
            print("Sistem açılıyor...")
            self.sistemi_acma = 'Açık'
            return (self.sistemi_acma)
        
    def sistem_kapat(self):
        if self.sistemi_acma == 'Kapalı':
            return 'Sistem zaten kapalı'
        else:
            print("Sistem kapatılıyor...")
            self.sistemi_acma = 'Kapalı'
            return "NEURAPY'A GELDİĞİNİZ İÇİN SAĞ OLUN. HOŞÇAKALIN. TEKRAR BEKLERİZ."
    
    def menu_yazdırma(self):

        if self.sistemi_acma == 'Kapalı':
            print('Lütfen önce sistemi açın.')
        
        else:
            file_path = 'menu_dataset.csv'
            df = pd.read_csv(file_path)
            yemek_adı = df['YEMEK ADI']
            icerik = df['İÇERİK']
            for i, a in zip(yemek_adı, icerik):
                print(i,'\n -',a)
    
    def icerige_gore_oneri(self):

        file_path = 'menu_dataset.csv'

        df = pd.read_csv(file_path)

        for i , a in zip(df['YEMEK ADI'], df['İÇERİK']):
            print(i, '\n -', a)


        kullanici_listesi = input("Kullanıcıdan alınacak listeyi (virgülle ayrılmış) girin:  \n").split(',')

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

    def yemege_gore_oneri(self):
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
                                islem_onay=input("başka bir işlem yapmak istiyor musunuz ? (evet/hayır)").lower()
                                odeme_onay=input("ödeme yapmak istiyor musunuz ?(evet/hayır)").lower()
                                    
        #def yemek_ekle 


                    elif satin_al_sor=="hayır":
                        print("İyi günler diler, Neurapy'a yine bekleriz.")
                        break
                    
                elif girdi_al=="q":
                    break

                else:
                    print("menümüzde böyle bir yemek bulunmamaktadır. Tekrar deneyiniz. (Çıkmak için q'ya basınız.)")


                            
a = Neurapy()
    
while True:
    islem = input('Sistemi açmak için 1, kapatmak için 2 \n')
    if islem == '1':
        a.sistem_acma()

    elif islem == '2':
        a.sistem_kapat()

    elif islem == '3':
        a.menu_yazdırma()
    
    elif islem == '4':
        a.oneri()
        break
    