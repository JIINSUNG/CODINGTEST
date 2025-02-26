import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

# 5 3 1
# 0 -1 0 0 0
# -1 -1 0 1 1
# 0 0 0 1 1
dx = [0, 0, 1, 0, -1, 0] # 위, 아래, 우, 하, 좌, 상
dy = [0, 0, 0, 1, 0 , -1]
dz = [-1, 1, 0, 0, 0, 0]

m, n, h = map(int, input().split())

graph = []



for _ in range(h):
    temp = []
    for _ in range(n):
        temp.append(list(map(int, input().split())))
    graph.append(temp)

tomato = 0
queue = deque()
for z in range(h):
    for i in range(n):
        for j in range(m):
            if graph[z][i][j] == 0:
                tomato += 1
            elif graph[z][i][j] == 1:
                queue.append((z, i, j))

answer = 0
while queue and tomato != 0:
    # 이번 차례에
    for _ in range(len(queue)):
        z, x, y = queue.popleft()

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = 1
                queue.append((nz, nx, ny))
                tomato -= 1
    answer += 1

if tomato <= 0:
    print(answer)
else:
    print(-1)
