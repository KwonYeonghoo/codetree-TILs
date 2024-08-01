# n, t = tuple(map(int, input().split()))
# arr = [input().split(), list(reversed(input().split()))]

# for _ in range(t):
#     # 1. 윗변 밀기
#     temp1 = arr[0][n-1]
#     for i in range(n-1, 0 ,-1):
#         arr[0][i] = arr[0][i-1]
    
#     # 2. 아랫변 밀기
#     temp2 = arr[1][0]
#     for j in range(1, n):
#         arr[1][j-1] = arr[1][j]
    
#     # 3. temp1, temp2 대입
#     arr[0][0] = temp2
#     arr[1][n-1] = temp1

# print(' '.join(arr[0]))
# print(' '.join(list(reversed(arr[1]))))


# 다른 풀이
n, t = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(2)]

for _ in range(t):
    tempGoDown = arr[0].pop()
    tempGoUp = arr[1].pop()
    arr[0].insert(0, tempGoUp)
    arr[1].insert(0, tempGoDown)

for a in arr:
    print(' '.join(map(str, a)))