# 00
# 10 11
# 20 21 22
# 30 31 32 33

arr = [list(map(int, input().split())) for _ in range(4)]

result = arr[0][0] + arr[1][0] + arr [1][1]+ \
arr[2][0] + arr[2][1] + arr[2][2] + \
arr[3][0] + arr[3][1] + arr[3][2] + arr[3][3]

print(result)