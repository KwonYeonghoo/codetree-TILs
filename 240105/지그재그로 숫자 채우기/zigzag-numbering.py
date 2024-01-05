n, m = tuple(map(int, input().split()))
arr = [[0 for _ in range(m)] for _ in range(n)]

count = 0
for i in range(m):
    if i % 2 == 0:
        for j in range(n):
            arr[j][i] = count
            count += 1
    else:
        for j in range(n):
            arr[n - 1 - j][i] = count
            count += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()