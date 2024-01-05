arr = [list(map(int, input().split())) for _ in range(2)]


for i in range(2):
    hor_avg = 0
    hor_avg += round(sum(arr[i]) / 4, 2)
    print(hor_avg, end=' ')
print()

for i in range(4):
    ver_avg = 0
    for j in range(2):
        ver_avg += arr[j][i]
    ver_avg = round(ver_avg / 2, 2)
    print(ver_avg, end=' ')
print()

total = 0
for a in arr:
    for n in a:
        total += n
tot_avg = total / (len(arr) * len(arr[0]))
tot_avg = round(tot_avg, 2)
print(tot_avg)