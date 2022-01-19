from collections import deque

# 최단거리 구하는 문제

# (nx,ny)랑 (x,y)랑 안헷갈리게 조심하자


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(nx < 0 or nx >= n or ny < 0 or ny >= m):
                continue
            elif(graph[nx][ny] == 0):
                continue
            elif(graph[nx][ny] == 1):
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))
