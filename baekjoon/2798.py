n, m = map(int, input().split())
numArr = list(map(int, input().split()))
numArrSize = len(numArr)
res = 0
diff = m

for i in range(numArrSize):
    for j in range(i + 1, numArrSize):
        for k in range(j + 1, numArrSize):
            sum = numArr[i] + numArr[j] + numArr[k]
            if (sum <= m) & (m - sum < diff):
                res = sum
                diff = m - sum
print(res)
