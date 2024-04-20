with open('input.txt', 'r') as r: 
    n = int(r.readline().strip())
    year = int(r.readline().strip())
    arr = []
    for i in range(n):
        l = list(r.readline().strip().split(' '))
        l[0] = int(l[0])
        arr.append(l)
    day_of_week = r.readline().strip()

ans_array = [53, 53, 52, 52, 52, 52, 52]
ans_1 = ''
ans_2 = ''
month_dict = {
    'January' : 0,
    'February' : 1,
    'March' : 2,
    'April' : 3,
    'May' : 4,
    'June' : 5,
    'July' : 6,
    'August' : 7,
    'September' : 8,
    'October' : 9,
    'November' : 10,
    'December' : 11
}
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
week_days_old = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
week_days_new = [day_of_week]
i = 0
while week_days_old[i] != day_of_week:
    i += 1
for j in range(1, 7):
    week_days_new.append(week_days_old[(i + j)%7])
num_of_day_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
additional_days = 2
if year % 400 == 0 or year % 4 == 0  and year % 100 != 0:
    num_of_day_month[1] = 29
    additional_days= 3
    ans_array[2] += 1
num_of_day_month_sum = []
num_of_day_month_sum.append(0)
for i in range(1, 12):
    num_of_day_month_sum.append(num_of_day_month_sum[i - 1] + num_of_day_month[i - 1])

for i in range(n):
    ans_array[(num_of_day_month_sum[month_dict[arr[i][1]]] + arr[i][0] - 1) % 7] -= 1
ans_i_min = 0
for i in range(1, 7):
    if ans_array[i] < ans_array[ans_i_min]:
        ans_i_min = i
ans_i_max = 0
for i in range(1, 7):
    if ans_array[i] > ans_array[ans_i_max]:
        ans_i_max = i
ans_1 = week_days_new[ans_i_max]
ans_2 = week_days_new[ans_i_min]
with open('output.txt', 'w') as f:
    f.write(ans_1 + ' ' + ans_2)
