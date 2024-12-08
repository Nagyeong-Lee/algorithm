n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
res = 0

for bitmask in range(1 << (n * m)):
    totalSum = 0

    # 가로줄 합
    for i in range(n):
        rowSum = 0
        for j in range(m):
            idx = i * m + j
            if bitmask & (1 << idx) == 0:  # 칸이 가로로 선택된 경우 숫자 붙이기
                rowSum = rowSum * 10 + graph[i][j]
            else:
                totalSum += rowSum
                rowSum = 0
        totalSum += rowSum

    # 세로줄 합
    for j in range(m):
        colSum = 0
        for i in range(n):
            idx = i * m + j
            if bitmask & (1 << idx):  # 칸이 세로로 선택된 경우 숫자 붙이기
                colSum = colSum * 10 + graph[i][j]
            else:
                totalSum += colSum
                colSum = 0
        totalSum += colSum

    res = max(res, totalSum)
print(res)
