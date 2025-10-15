'''
 Yazar:Hamza Karaermiş
 E-mail: hamzakaraermis@gmail.com 
 Açıklama:

'''
if __name__== '__main__':
    try:
        sayı1 = int(input("Birinci sayıyı giriniz: "))
        sayı2 = int(input("İkinci sayıyı giriniz: "))
        print (sayı1 ,''  ---- '', sayı2 )
    except:
        print("Lütfen sadece tam sayı giriniz.")
        
        