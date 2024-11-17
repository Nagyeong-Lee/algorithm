n, m = map(int, input().split())
checked = [False] * (n + 1)
res = []

def recur(num):
    if num == m:
        print(" ".join(map(str, res)))
        return
    for i in range(1, n + 1):
        checked[i] = True
        res.append(i)
        recur(num + 1)
        checked[i] = False
        res.pop()

recur(0)
