from itertools import combinations_with_replacement

n = int(input())
inputArr = [int(input()) for _ in range(n)]
arr = [int(i * (i + 1) / 2) for i in range(1, 45)]

for i in inputArr:
    flag = 0
    for j in combinations_with_replacement(arr,3):
        if i == sum(j):
            flag = 1
            break

    if flag:
        print(1)
    else: print(0)
