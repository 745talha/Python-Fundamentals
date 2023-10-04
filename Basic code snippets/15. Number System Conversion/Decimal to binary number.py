decnum=int(input("Enter decimal number : "))
i,binnum=1,0
while(decnum>0):
    binnum +=(decnum % 2) * i
    decnum //=2
    i *=10
print("Binary number : ",binnum)
