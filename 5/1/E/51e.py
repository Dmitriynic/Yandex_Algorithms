with open('input.txt', 'r') as r:
    n, k, d = list(map(int, r.readline().strip().split(' ')))

ans = ''
n_1 = n

temp = (10 * n_1 + 9) % k
if temp < 10 and temp >= 0:
    n_1 = 10 * n_1 + 9 - temp
    n_1 = str(n_1) + '0' * (d - 1)

if type(n_1) == str:
    ans = n_1
else:
    ans = -1

with open('output.txt', 'w') as f:
    f.write(str(ans))
