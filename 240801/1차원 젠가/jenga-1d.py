N = int(input())
arr = [int(input()) for _ in range(N)]
commands = [tuple(map(int, input().split())) for _ in range(2)]

def find_leftovers(command, arr):
    start = command[0]-1
    end = command[1]-1
    temp = []
    for i in range(0,start):
        temp.append(arr[i])
    for j in range(end+1, len(arr)):
        temp.append(arr[j])
    return temp

for command in commands:
    result = find_leftovers(command, arr)
    arr = result

print(len(arr))
print('\n'.join(map(str, arr)))