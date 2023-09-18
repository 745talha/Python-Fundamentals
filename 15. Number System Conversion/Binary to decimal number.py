binnum=int(input("Enter Binary number : "))
i,j,decnum = 1,0,0
while(binnum>0):
    rem=binnum%2
    decnum=decnum + rem *i
    i = i*2
    binnum=binnum//10
print("Binary to decimal number : ",decnum)
