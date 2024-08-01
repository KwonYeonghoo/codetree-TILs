N, T = tuple(map(int, input().split()))
commands = input()
arr = [list(map(int, input().split())) for _ in range(N)]
# 2차원 배열에서의 dx dy
# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 북쪽을 바라보는 초기상태
dir = 0
ans = 0
x, y = N//2, N//2
ans += arr[x][y]
for c in commands:
    if c == 'L':
        dir = (dir - 1 + 4) % 4
    elif c == 'R':
        dir = (dir + 1 + 4) % 4
    else:
        if x+dx[dir]<0 or x+dx[dir]>=N or y+dy[dir]<0 or y+dy[dir]>=N:
            continue
        x += dx[dir]
        y += dy[dir]
        ans += arr[x][y]
print(ans)