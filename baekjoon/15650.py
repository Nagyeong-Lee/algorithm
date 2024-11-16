n, m = map(int, input().split())
res = []

def recur(num):
    if m == len(res):
        print(" ".join(map(str, res)))
        return
    for i in range(num, n + 1):
        if i not in res:
            res.append(i)
            recur(i + 1)
            res.pop()

recur(1)
