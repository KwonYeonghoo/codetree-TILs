n = int(input())
visited = [0] * n

ans = []

def print_ans():
    print(' '.join(map(str, ans)))

def permutation(curr_num):
    if curr_num == n+1:
        print_ans()
        return
    for i in range(n, 0, -1):
        if visited[i-1] == 1:
            continue
        ans.append(i)
        visited[i-1] = 1
        permutation(curr_num+1)
        ans.pop()
        visited[i-1] = 0

permutation(1)