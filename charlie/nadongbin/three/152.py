from collections import deque

n, m = map(int, input().split())

array = []

for i in range(n):
  array.append(list(map(int, input())))

start = (0, 0, 1)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[False] * m for _ in range(n)]

def in_range(x, y):
  global n, m
  if (0 <= x < n) and (0 <= y < m):
    return True
  return False

def is_end(x, y):
  global n, m
  if x==n-1 and y==m-1:
    return True
  return False

def bfs(array, start, visited):
  queue = deque([start])

  while queue:
    x, y, c = queue.popleft()

    if is_end(x, y):
      return c

    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]
      nc = c + 1

      if in_range(nx, ny) \
        and not visited[nx][ny]:

        visited[nx][ny] = True
        queue.append((nx, ny, nc))

result = bfs(array, start, visited)
print(result)


