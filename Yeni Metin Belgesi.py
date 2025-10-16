'''
 Yazar:Hamza Karaermiş
 E-mail: hamzakaraermis@gmail.com 
 Açıklama: try-except kullanımı

'''
if __name__== '__main__':
    try:
     sayı1 = float(input("Birinci sayıyı giriniz: "))
     sayı2 = float(input("İkinci sayıyı giriniz: "))
    except ValueError:
     print("Lütfen sadece sayı giriniz.")
    else:
     işlem = input("Yapmak istediğiniz işlemi giriniz(+,-,*,/): ")
     if işlem == "+":
        print(sayı1, "+", sayı2, "=", sayı1 + sayı2)
     elif işlem == "-":
        print(sayı1, "-", sayı2, "=", sayı1 - sayı2)
     elif işlem == "*":
        print(sayı1, "*", sayı2, "=", sayı1 * sayı2)
     elif işlem == "/":
       print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
     else:
        print("Belirtilen işlemlerden birini giriniz.")
