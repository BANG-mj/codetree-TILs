# 1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31
# 8:31, 9:30, 10:31, 11:30 ,12:31

month = int(input())

if month<8:
    if month == 2:
        print(28)
    elif month % 2 == 0:
        print(30)
    else:
        print(31)
else:
    if month%2==0:
        print(31)
    else:
        print(30)