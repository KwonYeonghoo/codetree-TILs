from collections import deque

n,m,t = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
count = [[0 for _ in range(n)] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

marbles = [list(map(int, input().split())) for _ in range(m)]

def OOB(nr, nc):
    if nr<0 or nr>=n or nc<0 or nc>=n:
        return True
    else:
        return False



for _ in range(t):
    temp = []
    for marble in marbles:
        r,c = marble[0]-1, marble[1]-1
        count[r][c] += 1
        if count[r][c] > 1:
            count[r][c] = 0
            continue
        max_num = arr[r][c]
        for dir in range(4):
            nr = r + dx[dir]
            nc = c + dy[dir]
            if OOB(nr, nc) or arr[nr][nc] <= arr[r][c]:
                continue
            num = arr[nr][nc]
            max_num = max(num, max_num)
            if arr[nr][nc] == max_num:
                max_r, max_c = nr, nc
                # count[max_r][max_c] += 1
        if max_num == arr[r][c]: # 변화가 없다면
            temp.append([r+1, c+1])
        else:
            temp.append([max_r+1, max_c+1])
    marbles = temp
print(len(marbles))