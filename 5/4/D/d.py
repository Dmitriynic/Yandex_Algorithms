with open('input.txt', 'r') as r:
    w, n, m = list(map(int, r.readline().strip().split(' ')))
    arr_left = list(map(int, r.readline().strip().split(' ')))
    arr_right = list(map(int, r.readline().strip().split(' ')))

max_left = max(arr_left)
max_right = max(arr_right)
left = max_left #столец, после которого разделим рапорт
right = w - max_right

#div - разделитель
def count_(div):
    str_num_left = 1
    str_num_right = 1
    ind = 0
    for elem in arr_left:
        if ind == 0:
            ind += elem
        elif ind + elem + 1 > div:
            str_num_left += 1
            ind = elem
        else:
            ind += elem + 1
    ind = 0
    for elem in arr_right:
        if ind == 0:
            ind += elem
        elif ind + elem + 1 > w - div:
            str_num_right += 1
            ind = elem
        else:
            ind += elem + 1
    return str_num_left, str_num_right

l = left
r = right
mid = 0
m_prev = mid
mid = (r + l) // 2
res = [max(count_(mid))]
while l <= r:
    first, second = count_(mid)
    res.append(max(first, second))
    if first == second or mid == m_prev:
        break
    elif first < second:
        r = mid
    else:
        l = mid + 1
    m_prev = mid
    mid = (r + l) // 2

with open('output.txt', 'w') as f:
    f.write(str(min(res)))

