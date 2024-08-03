A = list(input())
N = len(A)

def run_length_encoding(A):
    count = 1
    compare = A[0]
    result = ""
    for i in range(1, N):
        if compare == A[i]:
            count += 1
        else:
            result += (compare+str(count))
            compare = A[i]
            count = 1
        if i == N-1:
            result += (A[i]+str(count))
    return len(result)
        
min_length = 10
for _ in range(N):
    temp = A[N-1]
    for i in range(N-1, 0, -1):
        A[i] = A[i-1]
    A[0] = temp
    length = run_length_encoding(A)
    min_length = min(length, min_length)
print(min_length)