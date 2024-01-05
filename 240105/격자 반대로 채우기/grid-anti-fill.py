n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]

count = 1
for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            arr[n-1-j][n-1-i] = count
            count += 1
    else:
        for j in range(n):
            arr[j][n-1-i] = count
            count += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()