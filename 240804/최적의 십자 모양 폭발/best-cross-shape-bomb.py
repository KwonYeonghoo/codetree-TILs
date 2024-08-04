import copy

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def OOB(nr, nc):
    if nr<0 or nr>=n or nc<0 or nc>=n:
        return True
    else:
        return False

def explode_bomb(arr, r,c):
    bomb = arr[r][c]
    for i in range(bomb):
        if r-i < 0: pass
        else: arr[r-i][c] = 0

        if r+i >= n: pass
        else: arr[r+i][c] = 0

        if c-i < 0: pass
        else: arr[r][c-i] = 0

        if c+i >= n: pass
        else: arr[r][c+i] = 0
    return arr

max_count = 0
# 폭탄의 좌표
for r in range(n):
    for c in range(n):
        copy_arr = copy.deepcopy(arr)
        copy_arr = explode_bomb(copy_arr, r,c)
        count = 0
        for a in range(n):
            temp = []
            zero_count = 0
            for b in range(n):
                if copy_arr[b][a] == 0:
                    zero_count += 1
                    continue
                temp.append(copy_arr[b][a])
            for _ in range(zero_count):
                temp.insert(0,0)
        
            for c in range(n):
                copy_arr[c][a] = temp[c]
        
        # dx dy로 풀기
        for i in range(n):
            for j in range(n):
                for dir in range(4):
                    ni = i + dx[dir]
                    nj = j + dy[dir]
                    if OOB(ni, nj) or copy_arr[ni][nj] == 0:
                        continue
                    if copy_arr[i][j] == copy_arr[ni][nj]:
                        count += 1

        max_count = max(count//2, max_count)

print(max_count)