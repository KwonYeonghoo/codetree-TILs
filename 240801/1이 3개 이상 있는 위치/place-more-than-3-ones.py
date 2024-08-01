N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0] # 우, 하, 좌, 상

def OOB(nx, ny):
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        return True
    else:
        return False

ans = 0 
for i in range(N):
    for j in range(N):
        x, y = i, j
        count = 0
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if OOB(nx, ny):
                continue
            if arr[nx][ny] == 1:
                count += 1
        if count >= 3:
            ans += 1
print(ans)