sayac=0
for i in range(1000,10000):
    a=i//1000
    d=i%10
    if a>d:
        sayac=sayac+1

        
print(sayac)
