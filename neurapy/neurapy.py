# menü yazdırma/öneri alma
# öneri yapma (girdi al, menüden benzerlik hesaplama, öneri listesi sunma)
# önerilerden satın almak isteyip istemediğini öğrenelim
# öneriler içinden almak istediklerini seçtirme (fiyat hesaplama)
# fiyat sunma
# ekstra menüden almak istedikleri var mı diye soru sorma
# varsa onları da alıp tekrar fiyat hesaplama
# ödemeyi alma



print("NEURAPY'A HOŞ GELDİNİZ !")
class Neurapy():
    def __init__ (self, sistemi_acma = 'Kapalı'):
        self.sistemi_acma= sistemi_acma
    
    def sistem_acma(self):
        if self.sistemi_acma == 'Açık':
            return 'Sistem zaten açık'
        else:
            print( 'Sistem açılmakta')
            self.sistemi_acma = 'Açık'
            return (self.sistemi_acma)
        
    def sistem_kapat(self):
        if self.sistemi_acma == 'Kapalı':
            return 'Sistem zaten kapalı'
        else:
            print( 'Sistem kapatılmakta')
            self.sistemi_acma = 'Kapalı'
            return "NEURAPY'A GELDİĞİNİZ İÇİN SAĞ OLUN. HOŞÇAKALIN. TEKRAR BEKLERİZ."
        
    
            
        
                        
a = Neurapy()
    
while True:
    islem = input('Sistemi açmak için 1, kapatmak için 2 \n')
    if islem == '1':
        a.sistem_acma()

    if islem == '2':
        a.sistem_kapat()
    