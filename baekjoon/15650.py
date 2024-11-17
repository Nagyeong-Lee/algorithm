n, m = map(int, input().split())
result = []


def recursive(num):
    if m == len(result):
        print(" ".join(map(str, result)))
        return
    for i in range(num, n + 1):
        result.append(i)
        recursive(i + 1)
        result.pop()


recursive(1)
