# 3명의 감기 증상과 체온 입력
# Y + 37도 이상 = A
# N + 37도 이상 = B
# Y + 37도 미만 = C
# N + 37도 미만 = D
# 3명 중 A가 두명 이상일 경우 E
# 아닐 경우 N

emer = 0
inp = input()
arr = inp.split()
a_sym = arr[0]
a_tem = float(arr[1])
if ((a_sym == 'Y') & (a_tem>=37)):
    emer = emer + 1

inp = input()
arr = inp.split()
b_sym = arr[0]
b_tem = float(arr[1])
if ((b_sym == 'Y') & (b_tem>=37)):
    emer = emer + 1

inp = input()
arr = inp.split()
c_sym = arr[0]
c_tem = float(arr[1])
if ((c_sym == 'Y') & (c_tem>=37)):
    emer = emer + 1

if emer >=2:
    print('E')
else:
    print('N')