# 4의 배수는 윤년, 그 외에는 평년
# 100의 배수이면서 400의 배수가 아니면 평년

year = int(input())
if year%4==0:
    if ((year%100==0) & (year%400!=0)):
        print("false")
    else:
        print("true")
else:
    print("false")