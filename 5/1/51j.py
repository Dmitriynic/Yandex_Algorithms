with open('input.txt', 'r') as r:
    w, h, c = list(map(int, r.readline().strip().split(' ')))
    arr_1 = []
    count = 0
    while True:
        line = r.readline().strip()
        if line == '':
            arr_1.append('#')
            count += 1
        else:
            arr_1.append(line)
            count = 0
        if count > 1:
            break
    arr_1.pop()
    arr_1.pop()

arr = ' '.join(arr_1)

class Image:
    def __init__(self, width, height, layout):
        self.width = width
        self.height = height
        self.layout = layout

class Floating(Image):
    def __init__(self, width, height, layout, dx, dy):
        super().__init__(width, height, layout)
        self.dx = dx
        self.dy = dy

arr_images = []
arr_split = []
k = 0
m = 0
while m != len(arr):
    for j in range(m, len(arr)):
        if arr[j] == '(':
            break
    if arr[m:j] != '':
        arr_split.extend(arr[m:j+1].replace('(', '').strip().split(' '))
    if j + 1 != len(arr):
        m = j
        while arr[m] != ')':
            m += 1
        str_image = arr[j:m+1].replace(')', '').split(' ')
        dict_image = {}
        for p in range(1, len(str_image)):
            dict_image[str_image[p].split('=')[0]] = 
str_image[p].split('=')[1]
        dict_image['width'] = int(dict_image['width'])
        dict_image['height'] = int(dict_image['height'])
        if dict_image['layout'] != 'floating':
            arr_split.append(Image(dict_image['width'], 
dict_image['height'], dict_image['layout']))
        else:
            dict_image['dx'] = int(dict_image['dx'])
            dict_image['dy'] = int(dict_image['dy'])
            arr_split.append(Floating(dict_image['width'], 
dict_image['height'], dict_image['layout'], dict_image['dx'], 
dict_image['dy']))
        m += 1
    else:
        break

arr_split = [item for item in arr_split if item != '']
ans = []   
curr = [0, 0]
curr_h = h
image_h_arr = []
coords_arr = []
interval = [[0, w]]
left = 0
right = w
floating = [0, 0]
prev_floating = []
temp_5 = 0
for i in range(len(arr_split)):
    if arr_split[i] == '#':
        floating = [0, 0]
        if not image_h_arr:
            curr[0] += curr_h #+h
            curr[1] = 0
            curr_h = h
        else:
            curr[0] += max(curr_h, max(image_h_arr)) # +h
            temp_1 = True
            curr[1] = 0
            curr_h = h
            image_h_arr = []
            coords_arr = []
            interval = [[0, w]]
    elif type(arr_split[i]) == str:
        floating = [0, 0]
        if not image_h_arr:
            if len(arr_split[i])*c + c + curr[1] > w and curr[1] != 0:
                curr[0] += curr_h
                curr[1] = 0
                curr[1] += len(arr_split[i])*c
                curr_h = h
            elif len(arr_split[i])*c + curr[1] > w and curr[1] == 0:
                curr[0] += curr_h
                curr[1] = 0
                curr[1] += len(arr_split[i])*c
            elif curr[1] == 0:
                curr[1] += len(arr_split[i])*c
            else:
                curr[1] += len(arr_split[i])*c + c
        else:
            temp_3 = True
            while temp_3 == True:
                for q in range(len(interval)):
                    if curr[1] <= interval[q][1] or q == len(interval) - 
1:
                        if curr[1] == interval[q][0] and curr[1] + 
len(arr_split[i])*c <= interval[q][1]:
                            curr[1] += len(arr_split[i])*c
                            temp_3 = False
                            break
                        elif curr[1] < interval[q][1] and curr[1] >= 
interval[q][0] and curr[1] + len(arr_split[i])*c + c <= interval[q][1]:
                            curr[1] += len(arr_split[i])*c + c
                            temp_3 = False
                            break
                        else:
                            if q + 1 != len(interval) and interval[q + 
1][0] > curr[1]:
                                curr[1] = interval[q+1][0]
                            elif q + 1 == len(interval):
                                curr[0] += curr_h
                                curr[1] = 0
                                temp_4 = 0
                                for u in range(len(coords_arr)):
                                    u -= temp_4
                                    if u == len(coords_arr):
                                        break
                                    image_h_arr[u] -= curr_h
                                    if image_h_arr[u] <= 0:
                                        image_h_arr.pop(u)
                                        for b in range(len(interval) - 1):
                                            if coords_arr[u][0] == 
interval[b][1]:
                                                interval[b] = 
[interval[b][0], interval[b+1][1]]
                                                interval.pop(b+1)
                                                temp_4 += 1
                                                break
                                        coords_arr.pop(u)
                                curr_h = h
                                    
    elif arr_split[i].layout == 'floating':
        if floating[1] == 0:
            if curr[1] + arr_split[i].dx < 0:
                ans.append([0, curr[0] + arr_split[i].dy])
                floating[0] = arr_split[i].dy
                if arr_split[i].dx < 0:
                    floating[1] = arr_split[i].width
                else:
                    floating[1] = arr_split[i].dx + arr_split[i].width
            elif curr[1] + arr_split[i].dx + arr_split[i].width >= w:
                ans.append([w - arr_split[i].width, curr[0] + 
arr_split[i].dy])
            else:
                ans.append([curr[1] + arr_split[i].dx, curr[0] + 
arr_split[i].dy])
                floating[0] = arr_split[i].dy
                floating[1] = arr_split[i].dx + arr_split[i].width
        else:
            if floating[1] + arr_split[i].width <= w:
                if curr[1] + floating[1] + arr_split[i].dx < 0:
                    ans.append([0 + floating[1], curr[0] + floating[0] + 
arr_split[i].dy])
                elif curr[1] + floating[1] + arr_split[i].dx + 
arr_split[i].width >= w:
                    ans.append([w - arr_split[i].width, curr[0] + 
floating[0] + arr_split[i].dy])
                else:
                    ans.append([curr[1] + floating[1] + arr_split[i].dx, 
curr[0] + floating[0] +  arr_split[i].dy])
                floating[0] += arr_split[i].dy
                floating[1] += arr_split[i].dx + arr_split[i].width
            else:
                floating[0] += arr_split[i].dy
                floating[1] += floating[1]
                if curr[1] + arr_split[i].dx < 0:
                    ans.append([0 + floating[1], curr[0] + floating[0] + 
arr_split[i].dy])
                elif curr[1] + floating[1] + arr_split[i].dx >= w:
                    ans.append([w - arr_split[i].width, curr[0] + 
floating[0] + arr_split[i].dy])
                else:
                    ans.append([curr[1] + floating[1] + arr_split[i].dx, 
curr[0] + floating[0] +  arr_split[i].dy])
                floating[0] += arr_split[i].dy
                floating[1] += arr_split[i].dx + arr_split[i].width
    else:
        floating = [0, 0]
        if arr_split[i].layout == 'embedded':
            if not image_h_arr:
                if curr[1] == 0:
                    ans.append([curr[1], curr[0]])
                    curr_h = max(arr_split[i].height, curr_h, h)
                    curr[1] += arr_split[i].width
                elif arr_split[i].width + curr[1] + c >= w:
                    curr[0] += curr_h
                    curr[1] = 0
                    ans.append([curr[1], curr[0]])
                    curr_h = max(arr_split[i].height, h)
                    curr[1] += arr_split[i].width
                else:
                    ans.append([curr[1] + c, curr[0]])
                    curr_h = max(arr_split[i].height, curr_h, h)
                    curr[1] += arr_split[i].width + c
            else:
                temp_3 = True
                while temp_3 == True:
                    for q in range(len(interval)):
                        if curr[1] == interval[q][0] and curr[1] + 
arr_split[i].width <= interval[q][1]:
                            ans.append([curr[1], curr[0]])
                            curr_h = max(arr_split[i].height, curr_h, h)
                            curr[1] += arr_split[i].width
                            temp_3 = False
                            break
                        elif curr[1] < interval[q][1] and curr[1] >= 
interval[q][0] and curr[1] + arr_split[i].width + c <= interval[q][1]:
                            ans.append([curr[1] + c, curr[0]])
                            curr_h = max(arr_split[i].height, curr_h, h)
                            curr[1] += arr_split[i].width + c
                            temp_3 = False
                            break
                        else:
                            if q + 1 != len(interval) and interval[q + 
1][0] > curr[1]:
                                curr[1] = interval[q+1][0]
                            elif q + 1 == len(interval):
                                curr[0] += curr_h
                                curr[1] = 0
                                temp_4 = 0
                                for u in range(len(coords_arr)):
                                    u -= temp_4
                                    if u == len(coords_arr):
                                            break
                                    image_h_arr[u] -= curr_h
                                    if image_h_arr[u] <= 0:
                                        image_h_arr.pop(u)
                                        for b in range(len(interval) - 1):
                                            if coords_arr[u][0] == 
interval[b][1]:
                                                interval[b] = 
[interval[b][0], interval[b+1][1]]
                                                interval.pop(b+1)
                                                temp_4 += 1
                                                break
                                        coords_arr.pop(u)
                                curr_h = h
        else:
            if not image_h_arr:
                if arr_split[i].width + curr[1] > w:
                    curr[0] += curr_h
                    curr[1] = 0
                    ans.append([curr[1], curr[0]])
                    image_h_arr.append(arr_split[i].height)
                    coords_arr.append([curr[1], curr[1] + 
arr_split[i].width])
                    interval[0] = [0, curr[1]]
                    interval.append([curr[1] + arr_split[i].width, w])
                    curr[1] += arr_split[i].width
                else:
                    ans.append([curr[1], curr[0]])
                    image_h_arr.append(arr_split[i].height)
                    coords_arr.append([curr[1], curr[1] + 
arr_split[i].width])
                    interval[0] = [0, curr[1]]
                    interval.append([curr[1] + arr_split[i].width, w])
                    curr[1] += arr_split[i].width
            else:
                temp_3 = True
                while temp_3 == True:
                    for q in range(len(interval)):
                        if curr[1] <= interval[q][1] or q == len(interval) 
- 1:
                            if curr[1] < interval[q][1] and curr[1] >= 
interval[q][0] and curr[1] + arr_split[i].width <= interval[q][1]:
                                ans.append([curr[1], curr[0]])
                                image_h_arr.append(arr_split[i].height)
                                coords_arr.append([curr[1], curr[1] + 
arr_split[i].width])
                                interval.insert(q+1, [curr[1] + 
arr_split[i].width, interval[q][1]])
                                interval[q] = [interval[q][0], curr[1]]
                                curr[1] += arr_split[i].width
                                temp_3 = False
                                break
                            else:
                                if q + 1 != len(interval) and interval[q + 
1][0] > curr[1]:
                                    curr[1] = interval[q+1][0]
                                elif q + 1 == len(interval):
                                    curr[0] += curr_h
                                    curr[1] = 0
                                    temp_4 = 0
                                    for u in range(len(coords_arr)):
                                        u -= temp_4
                                        if u == len(coords_arr):
                                            break
                                        image_h_arr[u] -= curr_h
                                        if image_h_arr[u] <= 0:
                                            image_h_arr.pop(u)
                                            for b in range(len(interval) - 
1):
                                                if coords_arr[u][0] == 
interval[b][1]:
                                                    interval[b] = 
[interval[b][0], interval[b+1][1]]
                                                    interval.pop(b+1)
                                                    temp_4 += 1
                                                    break
                                            coords_arr.pop(u)
                                    curr_h = h


with open('output.txt', 'w') as f:
    for i in range(len(ans)):
        f.write(str(ans[i][0]) + ' ' + str(ans[i][1]) + '\n')
