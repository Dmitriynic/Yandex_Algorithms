with open('input.txt', 'r') as r:
    n = int(r.readline().strip())

m = 0
#бинарный поиск по арифметической прогрессии
def findPos(num):
    l = 0
    r = num
    while l < r:
        m = (l + r) // 2
        if (1 + m)*m//2 < num:
            l = m + 1
        else:
            r = m
    return r

row = findPos(n) #порядок диагональной колонки
order = True
if row % 2 == 0:
    order = False
up = n - (1 + (row-1))*(row-1)//2
down = 1 - (n - (1 + row)*row//2)
if order == True:
    ans = f'{up}/{down}'
else:
    ans = f'{down}/{up}'

with open('output.txt', 'w') as f:
    f.write(ans)