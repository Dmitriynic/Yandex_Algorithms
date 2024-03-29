with open('input.txt', 'r') as r:
    list_1 = list(map(int, r.readline().split(":")))
    list_2 = list(map(int, r.readline().split(":")))
    num = int(r.readline())

def equal(list_1, list_2, num, ans):
    if num == 1:
        if list_1[1] >= list_2[0] + ans:
            ans += 1
    else:
        if list_1[0] <= list_2[1]:
            ans += 1
    return ans
ans = 0
if list_1[0] + list_2[0] <= list_1[1] + list_2[1]:
    ans = list_1[1] + list_2[1] - list_1[0] - list_2[0]
    ans = equal(list_1, list_2, num, ans)

with open('output.txt', 'w') as f:
    f.write(str(ans))