def generator(n):
    a,b=0,1
    while a<=n :
        yield a
        a,b=b,a+b


for num in generator(int (input("enter a number : "))):
    print(num)


# output :