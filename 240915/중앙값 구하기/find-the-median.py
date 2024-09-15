inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if a>b:
    if b>c:
        print(b)
    elif ((c>b)&(a>c)):
        print(c)
    else:
        print(a)
elif b>a:
    if a>c:
        print(a)
    elif (c>a)&(b>c):
        print(c)
    else:
        print(b)