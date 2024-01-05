n, m = tuple(map(int, input().split()))

arr = [[0 for _ in range(m)] for _ in range(n)]

len_ = n * m

count = 0
for i in range(n):
    for j in range(m):
        count += 1
        arr[i][j] = count
        print(arr[i][j], end=' ')
    print()