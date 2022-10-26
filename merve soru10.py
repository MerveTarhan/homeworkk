sayac=0
for i in range(10000,100000):
    sayi=str(i)
    a=int(sayi[0])
    b=int(sayi[1])
    c=int(sayi[3])
    d=int(sayi[4])
    if a==c and b==d:
        sayac=sayac+1

        
print(sayac)
