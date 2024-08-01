N = int(input())
commands = [input().split() for _ in range(N)]
# 동 남 서 북(2차원 배열이 아닌 그냥 2차원 배열 기준)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
dir_dict = {'E':0, 'S':1, 'W':2, 'N':3}
x, y = 0, 0

flag = False
count = 0
for command in commands:
    if flag == True:
        break
    dir = dir_dict[command[0]]
    dist = int(command[1])
    for d in range(dist):
        x += dx[dir]
        y += dy[dir]
        count += 1
        if x==0 and y==0:
            flag = True
            break
if flag == False:
    print(-1)
else: print(count)