sayac=0
for i in range(100,1000,2):
    sayi=str(i)
    a=int(sayi[2])
    b=int(sayi[1])
    c=int(sayi[0])
    if a==b or a==c or b==c:
        sayac=sayac+1
    if a==b and a==c:
        sayac=sayac+1

        
print(sayac)
