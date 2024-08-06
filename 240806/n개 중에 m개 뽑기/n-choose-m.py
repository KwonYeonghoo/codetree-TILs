N, M = tuple(map(int, input().split()))

ans = []

def print_ans():
    print(' '.join(map(str, sorted(ans))))

def permutation(curr_num):
    if curr_num == M+1:
        print_ans()
        return

    for i in range(1, N+1):
        if curr_num >= 2 and ans[-1] >= i:
            continue
        ans.append(i)
        permutation(curr_num+1)
        ans.pop()

permutation(1)