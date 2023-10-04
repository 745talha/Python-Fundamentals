binnum=int(input("Enter Binary number: "))
octnum,decnum,i=0,0,1
while(binnum !=0):
    decnum +=(binnum%10) * i
    i=i*2
    binnum //=10
i=1
while(decnum !=0):
    octnum +=(decnum %8)*i
    decnum //=8
    i *=10
print("Octal value : ",octnum)
