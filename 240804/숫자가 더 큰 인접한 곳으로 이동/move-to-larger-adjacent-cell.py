n, r, c = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def OOB(nr, nc):
    if nr<0 or nr>=n or nc<0 or nc>=n:
        return True
    else:
        return False

r, c = r-1, c-1
result = [arr[r][c]]

while True:
    min_num = 101
    cur_num = arr[r][c] # 5
    for dir in range(4):
        nr = r + dx[dir]
        nc = c + dy[dir]
        if OOB(nr,nc) or arr[nr][nc] <= cur_num:
            continue
        min_num = min(min_num, arr[nr][nc])
        if arr[nr][nc] == min_num:
            min_r, min_c = nr, nc
    if min_num == 101:
        break
    r, c = min_r, min_c
    result.append(arr[r][c])
print(' '.join(map(str, result)))