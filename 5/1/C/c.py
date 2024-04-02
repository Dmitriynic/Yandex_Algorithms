with open('input.txt', 'r') as r:
    n = int(r.readline())
    arr = []
    for i in range(n):
        arr.append(int(r.readline()))

ans = 0
ost = 0
for i in range(n):
    ans += arr[i] // 4
    ost = arr[i] % 4
    if ost == 1:
        ans += 1
    elif ost == 2:
        ans += 2
    elif ost == 3:
        ans += 2

with open('output.txt', 'w') as f:
    f.write(str(ans))