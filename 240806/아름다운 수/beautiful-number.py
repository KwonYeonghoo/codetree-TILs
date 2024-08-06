# 1은 항상 아름다운 숫자
# 1로만 이루어진 숫자는 항상 아름다운 숫자
# 

n = int(input())

def is_beautiful(num):
    two = 0
    three = 0 
    four = 0
    for i in range(len(num)):
        if num[i] == 1: continue
        elif num[i] == 2:
            if three != 0 or four != 0:
                return False
            two += 1
            if two == 2:
                two = 0
        elif num[i] == 3:
            if two != 0 or four != 0:
                return False
            three += 1
            if three == 3:
                three = 0
        else:
            if two != 0 or three != 0:
                return False
            four += 1
            if four == 4:
                four = 0
    if two == 0 and three == 0 and four == 0:
        return True
    else:
        return False


num = []
count = 0
def permutation(curr_num):
    global count
    if curr_num == n+1:
        if is_beautiful(num):
            count += 1
        return

    for i in range(1, 5):
        num.append(i)
        permutation(curr_num+1)
        num.pop()

permutation(1)
print(count)