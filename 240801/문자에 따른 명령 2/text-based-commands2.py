dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

commands = input()

cur_dir = 0
dir_dict = {'L':-1, 'R':1}
x,y = 0,0

for dir in commands:
    if dir == 'F':
        x += dx[cur_dir]
        y += dy[cur_dir]
    else:
        cur_dir = (cur_dir + dir_dict[dir] + 4) % 4 # 반시계로 돌 경우를 대비하여 +4를 한 값을 4로 나눈 나머지를 사용

print(x,y)