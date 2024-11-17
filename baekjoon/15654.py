n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
result = []


def recursive(num):
    if m == len(result):
        print(" ".join(map(str, result)))
        return
    for i in range(n):
        if nums[i] not in result:
            result.append(nums[i])
            recursive(num + 1)
            result.pop()


recursive(1)
