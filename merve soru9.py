for i in range(1,1000):
    a=i//100
    c=i%10
    b=(i-(a*100+c))//10
    if a+b+c<9:
        print(i, end=" ")
