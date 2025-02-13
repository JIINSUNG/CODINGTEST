import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

n = int(input())
graph = []
max_water = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))
    max_water = max(max_water, max(graph[-1]))

# visited = [[False] * n for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(i, j, visit):
    queue = deque([(i, j)])
    visit[i][j] = True
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                visit[nx][ny] = True
                queue.append((nx, ny))

answer = 1
for i in range(1, max_water):
    visited = [[False] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if graph[x][y] <= i:
                visited[x][y] = True

    cnt = 0

    for z in range(n):
        for p in range(n):
            if not visited[z][p]:
                cnt += 1
                visited[z][p] = True
                bfs(z, p, visited)
    answer = max(answer, cnt)



print(answer)