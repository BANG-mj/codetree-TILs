a_inp = input()
arr = a_inp.split()
a_math = int(arr[0])
a_eng = int(arr[1])

b_inp = input()
arr = b_inp.split()
b_math = int(arr[0])
b_eng = int(arr[1])

if a_math>b_math and a_eng>b_eng:
    print(1)
else:
    print(0)