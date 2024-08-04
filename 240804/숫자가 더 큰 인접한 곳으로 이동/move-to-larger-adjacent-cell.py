n, r, c = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def OOB(nr, nc):
    if nr<0 or nr>=n or nc<0 or nc>=n:
        return True
    else:
        return False

r, c = r-1, c-1
result = [arr[r][c]]

while True:
    cur_num = arr[r][c]
    for dir in range(4):
        nr = r + dx[dir]
        nc = c + dy[dir]
        if OOB(nr,nc) or arr[nr][nc] <= cur_num:
            continue
        else:
            cur_num = arr[nr][nc]
            break
    if cur_num == arr[r][c]: # 그대로이면 break
        break
    else:
        r,c = nr,nc # 좌표 업데이트
        result.append(cur_num) # 숫자 추가
print(' '.join(map(str, result)))