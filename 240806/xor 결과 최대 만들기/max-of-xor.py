n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

combination = []

def xor_calc():
    i = 1
    num = combination[0]
    while i < m:
        num ^= combination[i]
        i += 1
    return num
        

max_num = 0
def choose_number(curr_num, index):
    global max_num
    if curr_num == m+1:
        num = xor_calc()
        max_num = max(num, max_num)
        return
    for i in range(n):
        if curr_num >= 2 and index >= i:
            continue
        combination.append(arr[i])
        choose_number(curr_num+1, i)
        combination.pop()

choose_number(1,0)
print(max_num)