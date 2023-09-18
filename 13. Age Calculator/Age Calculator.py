curdate=int(input("Enter Current Date : "))
curmonth=int(input("Enter Current Month : "))
curyear=int(input("Enter Current Year : "))
birdate=int(input("Enter Birth Date : "))
birmonth=int(input("Enter Birth Month : "))
biryear=int(input("Enter Birth Year : "))
month=[31,28,31,30,31,30,31,31,30,31,30,31]
if(birdate>curdate):
    curdate=curdate+month[birmonth-1]
    curmonth=curmonth-1
if(birmonth>curmonth):
    curyear=curyear-1
    curmonth=curmonth+12
int=caldate=curdate-birdate
int=calmonth=curmonth-birmonth
int=calyear=curyear-biryear
print("Present Age")
print("Years : ",calyear)
print("Months : ",calmonth)
print("Days : ",caldate)
