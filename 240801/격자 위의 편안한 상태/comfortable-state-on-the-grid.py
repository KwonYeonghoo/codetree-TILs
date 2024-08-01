N, M = tuple(map(int, input().split()))
commands = [list(map(int, input().split())) for _ in range(M)]
arr = [[0 for _ in range(N)] for _ in range(N)]

# 2차원 배열에서의 dx dy
# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def OOB(nx, ny):
    if nx<0 or nx>=N or ny<0 or ny>=N:
        return True
    else:
        return False

for command in commands:
    x = command[0] - 1
    y = command[1] - 1
    arr[x][y] = 1
    count = 0
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if OOB(nx, ny) or arr[nx][ny] == 0:
            continue
        count += 1
    if count == 3:
        print(1)
    else: print(0)