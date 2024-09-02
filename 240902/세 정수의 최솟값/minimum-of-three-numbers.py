inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
min = 0

if a<=b:
    if a<=c:
        min = a
    elif c<a:
        min = c
elif b<a:
    if b<=c:
        min = b
    elif c<b:
        min = c

print(min)