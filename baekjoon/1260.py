# n : 정점의 개수
# m : 간선의 개수
# v : 탐색을 시작할 정점의 번호

n, m, v = map(int, input().split())

visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)
queue = []
graph = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(v):
    print(v, end=' ')
    visited_dfs[v] = True
    for i in range(1, n + 1):
        if visited_dfs[i] == False and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    queue.append(v)
    visited_bfs[v] = True
    while queue:
        first_item = queue.pop(0)
        print(first_item, end=' ')
        for i in range(1, n + 1):
            if visited_bfs[i] == False and graph[first_item][i] == 1:
                queue.append(i)
                visited_bfs[i] = True


dfs(v)
print()
bfs(v)
