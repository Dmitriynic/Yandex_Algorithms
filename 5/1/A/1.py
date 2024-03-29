with open('input.txt', 'r') as r:
    p, v = list(map(int, r.readline().split(" ")))
    q, m = list(map(int, r.readline().split(" ")))

ans = 0

if abs(p - q) > v + m:
    ans = 2 * (v + m + 1)
else:
    if p + v > q + m:
        right = p + v
    else:
        right = q + m
    if p - v < q - m:
        left = p - v
    else:
        left = q - m
    ans = right - left + 1

with open('output.txt', 'w') as f:
    f.write(str(ans))