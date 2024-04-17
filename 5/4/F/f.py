with open('input.txt', 'r') as r:
    w, h, n = list(map(int, r.readline().strip().split(' ')))
    arr = []
    for i in range(n):
        arr.append(list(map(int, r.readline().strip().split(' '))))

def findMin(ind):
    res = arr[0][ind]
    for i in range(n):
        if arr[i][ind] < res:
            res = arr[i][ind]
    return res

def findMax(ind):
    res = arr[0][ind]
    for i in range(n):
        if arr[i][ind] > res:
            res = arr[i][ind]
    return res

min_w = findMin(0)
max_w = findMax(0)
min_h = findMin(1)
max_h = findMax(1)

print(min_w, max_w, min_h, max_h)