N = int(input())
arr = [input().split() for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1] # 동, 남, 서, 북

def find_direction(str):
    if str == 'E':
        return 0
    elif str == 'S':
        return 1
    elif str == 'W':
        return 2
    else:
        return 3

x, y = 0, 0

for dir in arr:
    idx = find_direction(dir[0])
    dist = int(dir[1])
    for _ in range(dist):
        x += dx[idx]
        y += dy[idx]

print(x, y)