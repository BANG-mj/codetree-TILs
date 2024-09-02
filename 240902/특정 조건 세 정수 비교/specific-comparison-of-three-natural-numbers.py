inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
min = 0

if a<b and a<c:
    min = a
elif b<a and b<c:
    min = b
else:
    min = c

if a==min:
    print(1, end=' ')
else:
    print(0, end=' ')

if a==b and a==c and b==c:
    print(1)
else:
    print(0)