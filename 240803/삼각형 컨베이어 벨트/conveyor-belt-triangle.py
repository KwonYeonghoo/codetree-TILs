n, t = tuple(map(int, input().split()))
left = input().split()
right = input().split()
below = input().split()

for _ in range(t):
    l2r = left[n-1]
    r2b = right[n-1]
    b2l = below[n-1]
    
    for i in range(n-1, 0, -1):
        left[i] = left[i-1]
        right[i] = right[i-1]
        below[i] = below[i-1]
    
    left[0] = b2l
    right[0] = l2r
    below[0] = r2b

print(' '.join(left))
print(' '.join(right))
print(' '.join(below))