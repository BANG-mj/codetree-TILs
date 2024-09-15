inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

if a%2==0:
    a = a+1

for a in range(a, b+1, 2):
        print(a, end = ' ')