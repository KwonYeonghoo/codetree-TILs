n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]

count = 0
for i in range(n):
    for j in range(n):
        count += 1
        arr[j][i] = count

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()