with open('input.txt', 'r') as r:
    n, m = list(map(int, r.readline().strip().split(' ')))
    arr = list(map(int, r.readline().strip().split(' ')))
    attacks = []
    for i in range(m):
        attacks.append(list(map(int, r.readline().strip().split(' '))))

cum_sum = [0]
for i in range(1, n+1):
    cum_sum.append(arr[i-1] + cum_sum[i-1])

# Быстрый поиск
def findPos(cum_sum, num, delta):
    left = delta - 1
    right = len(cum_sum) - 1
    while left <=  right:
        left_sum = 0
        middle = (left + right) // 2
        left_sum = cum_sum[middle] - cum_sum[middle - delta]
        if left_sum == num:
            return middle - delta + 1
        if left_sum < num:
            left = middle + 1
        else:
            right = middle - 1
    return False

ans = []
for i in range(m):
    l = attacks[i][0]
    s = attacks[i][1]
    temp = findPos(cum_sum, s, l)
    if temp == False:
        ans.append(-1)
    else:
        ans.append(temp)

with open('output.txt', 'w') as f:
    for elem in ans:
        f.write(str(elem) + '\n')



