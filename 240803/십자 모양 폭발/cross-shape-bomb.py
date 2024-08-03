n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
r,c = tuple(map(int, input().split()))
r,c = r-1, c-1
# arr[r][c+1]
# arr[r+1][c]

# 1. 폭탄 맞은 곳 0으로 일단 만들어주기
# 2. 새로운 배열 만들어서 0이 아닌 값들만 담기


bomb = arr[r][c] - 1 # 폭탄 위력
arr[r][c] = 0 # 폭탄 있는 곳 0으로 초기화
for i in range(1, bomb+1):
    if r+i >= n: pass
    else: arr[r+i][c] = 0

    if r-i < 0: pass
    else: arr[r-i][c] = 0

    if c-i < 0: pass
    else: arr[r][c-i] = 0

    if c+i >= n: pass
    else: arr[r][c+i] = 0

for i in range(n):
    temp = []
    zero_count = 0
    for j in range(n):
        if arr[j][i] == 0:
            zero_count += 1
            continue
        temp.append(arr[j][i])
    for _ in range(zero_count):
        temp.insert(0, 0)
    for k in range(n):
        arr[k][i] = temp[k]

for row in arr:
    print(' '.join(map(str, row)))