n, m, k = tuple(map(int, input().split()))
commands = list(map(int, input().split()))

# k개의 말들 중 하나를 n번 고를 수 있다.

horses = []
max_score = 0

def get_score():
    horse_dict = {}
    score = 0
    for horse in horses:
        horse_dict[horse] = 0

    for i in range(n):
        if horse_dict[horses[i]] >= m-1:
            continue
        horse_dict[horses[i]] += commands[i]
        if horse_dict[horses[i]] >= m-1:
            score += 1
    return score

def choose_horse(curr_num):
    global max_score
    if curr_num == n+1:
        score = get_score()
        max_score = max(score, max_score)
        return
    for i in range(1, k+1):
        horses.append(i)
        choose_horse(curr_num+1)
        horses.pop()

choose_horse(1)
print(max_score)