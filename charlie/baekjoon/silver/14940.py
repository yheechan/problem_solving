from collections import deque

DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def inrange(x, y, y_lim, x_lim):
  if (x>-1 and x_lim>x) and (y>-1 and y_lim>y):
    return True
  return False

def distance2target(mapp, n, m, target):
  visited = [[0]*m for _ in range(n)]
  answer = [[-2]*m for _ in range(n)]
  tx, ty = target
  answer[ty][tx] = 0

  traverse = deque([(tx, ty, 0)])

  # measure the distance to target for each x, y in the mapp
  while traverse:
    cx, cy, cd = traverse.popleft()
    answer[cy][cx] = cd

    nd = cd+1

    for c in range(4):
      nx, ny = cx+DIR[c][0], cy+DIR[c][1]

      if inrange(nx, ny, n, m) \
      and visited[ny][nx] != 1 \
        and mapp[ny][nx] != 0:
          visited[ny][nx] = 1
          traverse.append((nx, ny, nd))

  return answer


def main():
  # n: vertical (세로)
  # m: horizontal (가로)
  n, m = map(int, input().split())

  target = (-1, -1)
  mapp = []
  for j in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)

    for i, e in enumerate(row):
      if e == 2:
        target = (i, j)
        break

  res = distance2target(mapp, n, m, target)

  for j, row in enumerate(res):
    for i, col in enumerate(row):
      if col == -2:
        if mapp[j][i] == 0:
          col = 0
        else:
          col = -1
      elif (i, j) == (target):
        col = 0
      print(col,end='')
      if i < m-1:
        print(end=' ')
    print()
      


if __name__ == "__main__":
  main()

