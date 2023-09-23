n1=float(input("Enter first number : "))
op=input("Enter operation ")
n2=float(input("Enter second number : "))
if(op=="+"):
    print("Result : ",n1+n2)
elif(op=="-"):
    print("Result : ",n1-n2)
elif(op=="*"):
    print("Result : ",n1*n2)
elif(op=="/"):
    print("Result : ",n1/n2)
else:
    print("Invalid input")
