n, t = tuple(map(int, input().split()))
r, c, d = input().split()
r, c = int(r)-1, int(c)-1

# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir_dict = {'L':2, 'R':0, 'U':3, 'D':1}
dir = dir_dict[d]

def OOB(x, y):
    if x<0 or x>=n or y<0 or y>=n:
        return True
    else:
        return False

for i in range(t):
    if OOB(r+dx[dir],c+dy[dir]):
        dir = (dir + 2 + 4) % 4
    else:
        r += dx[dir]
        c += dy[dir]
print(r+1, c+1)