arr = [int(input()) for _ in range(9)]
targetSum = sum(arr) - 100
arrSize = len(arr)
num1, num2, findYN = 0, 0, 0

for i in range(arrSize):
    for j in range(i+1, arrSize):
        if (arr[i] + arr[j] == targetSum):
            num1, num2 = arr[i], arr[j]
            findYN = 1
            break
    if findYN:
        break

arr.remove(num1)
arr.remove(num2)
arr.sort()
for i in arr:
    print(i)