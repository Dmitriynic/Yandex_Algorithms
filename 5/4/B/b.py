with open('input.txt', 'r') as r:
    n = int(r.readline().strip())

# k + 2 * (k - 1) + 3 * (k - 2) + 4 * (k - 3) + ... + k * 1 + k - 1 k + ik -i -i^2
# 1, (1) + 1_ + 1 + 1_ + ((2)), (1) + (1_) + (1) + (1_) + 1 + 1_  + (2) + 1_ + 
#2 + 1_ + ((3)), сколько новых элементов добавили, столько и промежутков, каждый 
# раз при этом добавляем по одному элементу для каждого сущ числа и 1 
#новый(потенциальный k)
sum = 1
cum_sum = 1 
ans = 1
if n != 1:
    while(sum <= n):
        ans += 1
        sum += 2*ans + cum_sum
        cum_sum += ans

    ans -= 1 

with open('output.txt', 'w') as f:
    f.write(str(ans))
