with open('input.txt', 'r') as r:
    arr = list(map(int, r.readline().strip().split(' ')))
    L = arr[0]
    x_1 = arr[1]
    v_1 = arr[2]
    x_2 = arr[3]
    v_2 = arr[4]

def first_fun(t):
    return min(abs((x_1 + v_1 * t) % L), L - abs((x_1 + v_1 * t) % L))
    
def second_fun(t):
    return min(abs((x_2 + v_2 * t) % L), L - abs((x_2 + v_2 * t) % L))

ans = -1
def func(left, step):
    first = first_fun(left)
    second = second_fun(left)
    if first == second:
        return left
    if x_1 == 0 and v_1 == 0:
        return (L-x_2)/v_2
    if x_2 == 0 and v_2 == 0:
        return (L-x_1)/v_1
    else:
        bool = first > second
        bool_temp = bool
        while bool == bool_temp:
            left += step
            if abs(first_fun(left) - second_fun(left)) <= 3.8 * 10 ** -9:
                return left
            bool_temp = first_fun(left) > second_fun(left)

        left -= step
        step /= 2
        if step < 10 ** -10:
            return left
        return func(left, step)

if v_1 == 0 and v_2 == 0:
    if x_1 == x_2:
        ans = 0.0
else:
    ans = func(0.0, max( 1/max(abs(v_1), abs(v_2)),L/(120*max(abs(v_1), 
abs(v_2)))))
with open('output.txt', 'w') as f:
    if ans == -1:
        f.write('NO')
    else:
        f.write('YES\n')
        f.write(str(ans))
