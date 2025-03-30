from collections import deque

DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]] # N, E, S, W

def within_range(x, y, x_lim, y_lim):
  if (x>-1 and x_lim>x) and (y>-1 and y_lim>y):
    return True
  return False

def bfs(M, N, farm, traverse, empty):
  result_days = -1
  ryped = len(traverse)

  while traverse:
    x, y, curr_day = traverse.popleft()
    if curr_day > result_days:
      result_days = curr_day

    for c in range(4):
      check_x, check_y = x+DIR[c][0], y+DIR[c][1]

      # RYPE THE TOMATO
      if within_range(check_x, check_y, M, N) and farm[check_y][check_x] == 0:
        next_day = curr_day + 1
        farm[check_y][check_x] = 1
        ryped += 1
        traverse.append((check_x, check_y, next_day))
  
  if ryped != (N*M)-empty:
    return -1

  return result_days

def main():
  # M: horizontal (가로)
  # N: vertical (세로)
  M, N = map(int, input().split())
  print(M, N)

  traverse = deque()
  empty = 0
  farm = []

  for j in range(N):
    row = list(map(int, input().split()))
    farm.append(row)
    for i in range(M):
      if row[i] == 1:
        traverse.append((i, j, 0))
      if row[i] == -1:
        empty += 1


  res = bfs(M, N, farm, traverse, empty)
  print(res)

    

if __name__ == "__main__":
  main()

