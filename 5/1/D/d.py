with open('input.txt', 'r') as r:
    arr = []
    for i in range(8):
        arr.append(list(r.readline().strip()))

def vertical_up(arr, i, j):
    if i != 0:
        if arr[i-1][j] != 'R' and arr[i-1][j] != 'B':
            arr[i - 1][j] = '1'
            vertical_up(arr, i-1, j)

def vertical_down(arr, i, j):
    if i != len(arr)-1:
        if arr[i+1][j] != 'R' and arr[i+1][j] != 'B':
            arr[i + 1][j] = '1'
            vertical_down(arr, i+1, j)

def horizontal_left(arr, i, j):
    if j != 0:
        if arr[i][j-1] != 'R' and arr[i][j-1] != 'B':
            arr[i][j - 1] = '1'
            horizontal_left(arr, i, j-1)

def horizontal_right(arr, i, j):
    if j != len(arr[0])-1:
        if arr[i][j+1] != 'R' and arr[i][j+1] != 'B':
            arr[i][j + 1] = '1'
            horizontal_right(arr, i, j+1)

def diagonal_up_left(arr, i, j):
    if i != 0 and j != 0:
        if arr[i-1][j-1] != 'R' and arr[i-1][j-1] != 'B':
            arr[i - 1][j - 1] = '1'
            diagonal_up_left(arr, i-1, j-1)

def diagonal_up_right(arr, i, j):
    if i != 0 and j != len(arr[0])-1:
        if arr[i-1][j+1] != 'R' and arr[i-1][j+1] != 'B':
            arr[i-1][j+1] = '1'
            diagonal_up_right(arr, i-1, j+1)

def diagonal_down_left(arr, i, j):
    if i != len(arr)-1 and j != 0:
        if arr[i+1][j-1] != 'R' and arr[i+1][j-1] != 'B':
            arr[i + 1][j - 1] = '1'
            diagonal_down_left(arr, i+1, j-1)

def diagonal_down_right(arr, i, j):
    if i != len(arr)-1 and j != len(arr[0])-1:
        if arr[i+1][j+1] != 'R' and arr[i+1][j+1] != 'B':
            arr[i + 1][j + 1] = '1'
            diagonal_down_right(arr, i+1, j+1)

for i in range(8):
    for j in range(8):
        if arr[i][j] == 'R':
            vertical_up(arr, i, j)
            vertical_down(arr, i, j)
            horizontal_left(arr, i, j)
            horizontal_right(arr, i, j)
        if arr[i][j] == 'B':
            diagonal_up_left(arr, i, j)
            diagonal_up_right(arr, i, j)
            diagonal_down_left(arr, i, j)
            diagonal_down_right(arr, i, j)

ans = 0

for i in range(8):
    for j in range(8):
        if arr[i][j] == '*':
            ans += 1

with open('output.txt', 'w') as f:
    f.write(str(ans))
