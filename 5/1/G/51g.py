with open('input.txt', 'r') as r:
    x = int(r.readline().strip())
    y = int(r.readline().strip())
    p = int(r.readline().strip())

ans = 0
if x >= y:
    ans = 1
elif x > p:
    ans = 1
    y -= x
    val = True
    while y > 0:
        if x - y > 0 and x < y + p and x - (p - (x - y)) >= p - (x - y):
            ans += 2
            break
        x_arr = []
        y_arr = []
        p_arr = []
        p_potentional =  p - (x - y)
        x_potentional = x - p_potentional
        if p_potentional <= 3 * x_potentional/2 and y - 2*(x-p) > 0:
            ans += 3
            break
        if p_potentional <= 1.616 * x_potentional and x - y >= 0:
            ans_1 = 0
            ans_2 = 1
            ans_3 = 0
            ans_4 = 0
            y_1 = y
            y_2 = y
            y_3 = y
            while y_1 > 0:
                y_1 -= x - p
                ans_1 += 1
            while y_2 > 0:
                y_2 -= x - p
                ans_3 += 1
                p_pot_2 = p - (x - y_2)
                x_pot_2 = x - p_pot_2
                if p_pot_2 <= 3 * x_pot_2/2 and y_2 - 2*(x_pot_2-p_pot_2) > 0:
                    ans_3 += 3
                    break
            while y_3 > 0:
                y_3 -= x - p
                ans_4 += 1
                if x - y_3 > 0 and x < y_3 + p and x - (p - (x - y_3)) >= p - (x - y_3):
                    ans_4 += 2
                    break
            x_1 = x_potentional
            p_1 = p_potentional
            while p_1 > 0:
                p_1 -= x_1
                x_1 -= p_1
                ans_2 += 1
            ans_out = min(ans_1, ans_2, ans_3, ans_4)
            ans+= ans_out
            break
        y -= x - p
        ans += 1
else:
    ans = 1
    y -= x
    if x - y <= 0:
        ans = -1
    else:
        ans += 1
        p -= x - y
        x -= p
        if x <= 0:
            ans = -1
        while ans != -1:
            ans += 1
            p -= x
            if p <= 0:
                break
            x -= p
            if x <= 0:
                ans = -1

with open('output.txt', 'w') as f:
    f.write(str(ans))
