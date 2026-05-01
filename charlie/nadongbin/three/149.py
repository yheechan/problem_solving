from collections import deque

n, m = map(int, input().split())

array = []
for _ in range(n):
  array.append(list(map(int, input())))


visited = [[False] * m for _ in range(n)]

def in_range(x, y):
  global n, m
  if (0 <= x < n) and (0 <= y < m):
    return True
  return False

def dfs(x, y):
  global visited
  if not in_range(x, y):
    return False

  if array[x][y] == 1:
    return False

  if visited[x][y] == False:
    visited[x][y] = True

    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]

      dfs(nx, ny)

    return True
  return False
  

result = 0
for i in range(n):
  for j in range(m):

    if dfs(i, j):
      result += 1

print(result)      

