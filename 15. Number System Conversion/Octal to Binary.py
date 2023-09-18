octalnum=int(input("Enter Octal number : "))
decimalnum,binarynum,i=0,0,1
while(octalnum !=0):
    decimalnum +=(octalnum%10) *i
    i=i*8
    octalnum//=10
i=1
while(decimalnum !=0):
    binarynum +=(decimalnum %2)*i
    decimalnum //=2
    i*=10
print("Binary number : ",binarynum)
