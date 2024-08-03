n, m = tuple(map(int, input().split()))
arr = [input().split() for _ in range(n)]

count = 0
for i in range(n):
    row_happy = 1
    col_happy = 1
    row_flag = False
    col_flag = False
    for j in range(n):
        # 가로 수열
        if j==0:
            r = arr[i][j]
        elif arr[i][j] == r:
            row_happy += 1
            r = arr[i][j]
        else:
            row_happy = 1
            r = arr[i][j]
        if row_happy == m:
            row_flag = True

        # 세로 수열
        if j==0:
            c = arr[j][i]
        elif arr[j][i] == c:
            col_happy += 1
            c = arr[j][i]
        else:
            col_happy = 1
            c = arr[j][i]
        if col_happy == m:
            col_flag = True
    
    if row_flag == True:
        count += 1
    if col_flag == True:
        count += 1

print(count)