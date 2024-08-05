K, N = tuple(map(int, input().split()))

answer = []

def print_answer():
    print(' '.join(map(str, answer)))

def choose(curr_num):
    if curr_num == N+1:
        print_answer()
        return
    
    for i in range(1, K+1):
        answer.append(i)
        choose(curr_num+1)
        answer.pop()

choose(1)