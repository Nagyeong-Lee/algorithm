n = int(input())
inputArr = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    skill = list(map(int, input().split()))
    for j in range(1, n + 1):
        inputArr[i][j] = skill[j - 1]

combs, result = [], []

# 스타트 조합
def getCombinations(num):
    if len(result) == n // 2:
        combs.append(result[:])
        return
    for i in range(num, n + 1):
        result.append(i)
        getCombinations(i + 1)
        result.pop()

getCombinations(1)

# 능력치 계산
def getPower(comb):
    power = 0
    for i in range(len(comb)):
        for j in range(i + 1, len(comb)):
            power += inputArr[comb[i]][comb[j]] + inputArr[comb[j]][comb[i]]
    return power


min = 9999999999
for i in combs:
    start = i
    link = [i for i in range(1, n + 1) if i not in start]
    startPower = getPower(start)
    linkPower = getPower(link)
    if abs(startPower - linkPower) < min:
        min = abs(startPower - linkPower)

print(min)
