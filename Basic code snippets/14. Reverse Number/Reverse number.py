num=int(input("Enter an Integer : "))
revnum=0
while(num !=0):
    rem=num%10
    revnum=revnum*10 +rem
    num //=10
print("Reverse number : ",revnum)
