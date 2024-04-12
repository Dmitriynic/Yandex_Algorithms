with open('input.txt', 'r') as r:
    n = int(r.readline().strip())
    arr = list(map(int, r.readline().strip().split(' ')))

ans = []

if n == 2:
    a_1 = arr[0]
    a_2 = arr[1]
    if a_1 % 2 == 1 and a_2 % 2 == 1:
        ans.append('x')
    else:
        ans.append('+')
else:
    pos = 0
    i = n - 1
    while arr[i] % 2 == 0:
        i -= 1
    pos = i
    curr = arr[0]
    if pos > 0:
        for j in range(1, pos):
            curr += arr[j]
            ans.append('+')
        if curr % 2 == 0:
            curr += arr[pos]
            ans.append('+')
        else:
            curr *= arr[pos]
            ans.append('x')
    if pos < n - 1:
        for i in range(pos + 1, n):
            ans.append('+')    


with open('output.txt', 'w') as f:
    f.write(''.join(ans))
