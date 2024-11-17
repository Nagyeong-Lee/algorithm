n, m = map(int, input().split())
result = []


def recursive(num):
    if m == len(result):
        print(" ".join(map(str, result)))
        return
    for i in range(1, n + 1):
        if i not in result:
            result.append(i)
            recursive(num + 1)
            result.pop()


recursive(0)
