n = int(input())
ingredients = [list(map(int, input().split())) for _ in range(n)]
result = 9999999

def recur(idx, use, sin, sun):
    global result

    if idx == n:
        if use > 0:
            result = min(result, abs(sin - sun))
        return

    # 현재 재료 선택
    recur(idx + 1, use + 1, sin * ingredients[idx][0], sun + ingredients[idx][1])

    # 현재 재료를 선택하지 않을 경우 다음 재료로 이동
    recur(idx + 1, use, sin, sun)


recur(0, 0, 1, 0)
print(result)
