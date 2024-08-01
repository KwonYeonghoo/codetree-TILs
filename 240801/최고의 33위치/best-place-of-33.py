N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_coin = 0
# 기준점 좌표: i,j
for i in range(N):
    for j in range(N):
        if i+2 >= N or j+2 >= N:
            continue
        count = 0
        for x in range(3):
            for y in range(3):
                if arr[i+x][j+y] == 1:
                    count += 1
        max_coin = max(count, max_coin)

print(max_coin)