n, m, k = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
k = k-1

def is_fine():
    flag = True
    for i in range(n):
        if i == n-1:
            for j in range(k, k+m):
                arr[i][j] = 1
            return arr
        for j in range(k, k+m):
            arr[i][j] = 1
            if arr[i+1][j] != 0:
                flag = False
        if flag == False:
            return arr
        else:
            for j in range(k, k+m):
                arr[i][j] = 0


new_arr = is_fine()
for row in new_arr:
    print(' '.join(map(str, row)))