
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
            file_path = "menu_dataset.csv"
            df = pd.read_csv(file_path)
            for i , a in zip(df['YEMEK ADI'], df['İÇERİK']):
                print(i, '\n -', a)    

    def islem_odeme_onay(self, ara_toplam):
        while True: 
                islem_onay=input("işlemi onaylıyor musunuz ? (evet/hayır)").lower()
                if islem_onay=="evet":
                    print("yemekler sepete eklendi !")
                    while True:
                        odeme_onay=input("ödemeyi onaylıyor musunuz ? (evet/hayır)").lower()
                        if odeme_onay=="evet":
                            self.toplam+=ara_toplam
                            print("Ödemeniz onaylandı ! İyi günler diler, Neurapy'a yine bekleriz.")
                            return
                        elif odeme_onay=="hayır":
                            print("ödeme onaylanmadı. ana menüye dönülüyor...")
                            time.sleep(1)
                            return
                        else:
                            print("hatalı girdi.")
                elif islem_onay=="hayır":
                    print("ödeme onaylanmadı. ana menüye dönülüyor...")
                    time.sleep(1)
                    return
                else:
                    print("hatalı girdi.")


    def icerige_gore_oneri(self):
        if self.sistem == 'Kapalı':
            print('Lütfen önce sistemi açın.')

        else:

            file_path = "neurapy/neurapy/menu_dataset.csv"

            df = pd.read_csv(file_path)

            kullanici_listesi = input("yemekte bulunmasını istediğiniz ürün/ürünlerin adını (virgülle ayrılmış) girin:  \n")
            kullanici_listesi=[urun.strip() for urun in kullanici_listesi.split(",")]

            benzerlik_sonuclari = []

            df['İÇERİK']=df['İÇERİK'].str.lower().values

            for _, row in df.iterrows():
                sayac=0
                for veri in kullanici_listesi:
                    if veri in row["İÇERİK"]:
                        sayac+=1
                        if sayac>0:
                            benzerlik_sonuclari.append({
                                        "yemek adı": row["YEMEK ADI"],
                                        "fiyatı" : row["FİYAT"],
                                        "içeriği": row["İÇERİK"], 
                                        "benzerlik miktarı": sayac})
                    else:
                        pass

            benzerlik_df=pd.DataFrame(benzerlik_sonuclari)
            benzerlik_sort=benzerlik_df.sort_values(by="benzerlik miktarı", ascending=False)
            print(benzerlik_sort.head())
            
            satin_alma=input("önerilenlerden satın almak istediğiniz bir yemek var mı ? (evet/hayır").lower()
            if satin_alma == 'evet':
                ara_toplam=0
                satin_alinan = input("hangi yiyecekleri satın almak istiyorsunuz ? numarasını giriniz:")
                satin_alinan = [a.strip() for a in satin_alinan.split(",")]
                satin_alinan=[int(b) for b in satin_alinan]
                fiyatlar=[]
                for c in satin_alinan:
                    c=benzerlik_df.loc[c].values[1]
                    fiyatlar.append(c)
                    ara_toplam+=sum(fiyatlar)
                print(f"toplam ücret: {ara_toplam}")
                self.islem_odeme_onay(ara_toplam)
            else:
                print("ana menüye dönülüyor...")


    def yemege_gore_oneri(self):
        
        if self.sistem == 'Kapalı':
            print('Lütfen önce sistemi açın.')
            
        else:
            df = pd.read_csv("neurapy/neurapy/menu_dataset.csv")
            df.set_index("YEMEK ADI", inplace=True)
            df.index = df.index.str.lower()

            while True:
                girdi_al = input("Menümüzden beğendiğiniz bir yemeğin adını giriniz (küçük harflerle giriniz)(işlemi sonlandırmak için: q'ya basınız):")

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
                                

                        df_oneri=pd.DataFrame(oneri_list)
                        oneri_sort=df_oneri.sort_values(by="benzerlik miktarı", ascending=True)
                        son_bes=oneri_sort.tail(6)
                    print(son_bes.drop(son_bes.index[-1]))

                    satin_al_sor=input("önerilenlerden satın almak istediğiniz bir yemek var mı ? (evet/hayır").lower()
                    if satin_al_sor=="evet":
                        ara_toplam=0
                        satin_al=input("hangi yiyecekleri satın almak istiyorsunuz ? numarasını giriniz:")

                        satin_al = [i.strip() for i in satin_al.split(",")]
                        satin_al=[int(b) for b in satin_al]
                        fiyatlar=[]
                        for c in satin_al:
                            c=df_oneri.loc[c].values[1]
                            fiyatlar.append(c)
                        ara_toplam+=sum(fiyatlar)
                        print(f"toplam ücret: {ara_toplam}")
                        self.islem_odeme_onay(ara_toplam)
                    else:
                        print("ana menüye dönülüyor...")
                    
                elif girdi_al=="q":
                    break
                else:
                    print("menümüzde böyle bir yemek bulunmamaktadır. Tekrar deneyiniz.")


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
        print(f"ANA TOPLAM:{self.toplam+toplam_ekle}")

        self.islem_odeme_onay(toplam_ekle)        
                        
a = Neurapy()

print("""
      Neurapy'a Hoş Geldiniz !
      Hangi işlemi yapmak istersiniz ?
      1.Sistem açma
      2.Sistem Kapatma
      3.Menü Yazdırma
      4.Yemek İçeriğine Göre Yemek Önerisi Alma
      5.Yemeğe Göre Öneri Alma
      6.Sepete Yemek Ekle""")
    
while True:
    islem = int(input("""Sistemi açmak için 1'e, kapatmak için 2'ye\n 
                        Menüyü yazdırmak için 3'e\n
                        İçeriğe göre öneri almak için 4'e\n
                        Yemeğe göre öneri için 5'e\n
                        Sepete yemeke eklemek için 6'ya basabilirsiniz."""))
    
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
        print("Hatalı işlem. Lütfen tam sayı bir değer giriniz.")