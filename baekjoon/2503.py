import itertools

permList = itertools.permutations([i for i in range(1, 10)], 3)

n = int(input())
inputList = [list(input().split()) for _ in range(n)]
res = 0

for i in permList:
    flag = True
    for j in inputList:
        strCnt, ballCnt = 0, 0
        num = j[0]
        inputStrCnt, inputBallCnt = int(j[1]), int(j[2])
        for idx in range(0, 3):
            if str(i[idx]) == num[idx]:
                strCnt += 1
            elif str(i[idx]) in num:
                ballCnt += 1
        if (inputStrCnt != strCnt) | (inputBallCnt != ballCnt):
            flag = False
            break

    if flag:
        res += 1

print(res)
