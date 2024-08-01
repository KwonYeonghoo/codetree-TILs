command = input()
# 좌표평면에서의 dx dy
# 북 동 남 서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 초기값은 북쪽을 바라보게
dir = 0
x,y = 0,0
flag = False
count = 0
for c in command:
    if c == 'L':
        dir = (dir - 1 + 4) % 4
        count += 1
    elif c == 'R':
        dir = (dir + 1 + 4) % 4
        count += 1
    else:
        x += dx[dir]
        y += dy[dir]
        count += 1
        if x == 0 and y == 0:
            flag = True
            break
if flag == False:
    print(-1)
else: print(count)