# 세 값 중 가장 큰 숫자를 출력

inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if ((a > b) & (a > c)):
    print(a)
elif ((b > a) & (b > c)):
    print(b)
else:
    print(c)