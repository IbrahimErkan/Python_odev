for sayi in range(5):
    sayi=int(input("sayı:"))
    x=sayi-1
    while x>1:
        if sayi%x==0:
            print('{} sayısı asal degildir'.format(sayi))
            break
        else:
            x-=1
    else:
        print('{} sayısı asaldır'.format(sayi))
