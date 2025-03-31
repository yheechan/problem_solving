from collections import deque

DIR = [[0, 1, 0], [1, 0, 0], [0, -1, 0], [-1, 0, 0], [0, 0, 1], [0, 0, -1]] # N, E, S, W, U, D

def within_range(x, y, z, x_lim, y_lim, z_lim):
  if (x>-1 and x_lim>x) and (y>-1 and y_lim>y) and (z>-1 and z_lim>z):
    return True
  return False

def bfs(M, N, H, farm_stack, traverse, empty):
  result_days = -1
  ryped = len(traverse)

  while traverse:
    x, y, z, curr_day = traverse.popleft()
    if curr_day > result_days:
      result_days = curr_day

    next_day = curr_day + 1
    for c in range(6):
      check_x, check_y, check_z = x+DIR[c][0], y+DIR[c][1], z+DIR[c][2]

      # RYPE THE TOMATO
      if within_range(check_x, check_y, check_z, M, N, H) and farm_stack[check_z][check_y][check_x] == 0:
        farm_stack[check_z][check_y][check_x] = 1
        ryped += 1
        traverse.append((check_x, check_y, check_z, next_day))
  
  if ryped != (N*M*H)-empty:
    return -1

  return result_days

def main():
  # M: horizontal (가로)
  # N: vertical (세로)
  # H: stacks
  M, N, H = map(int, input().split())

  traverse = deque()
  empty = 0
  farm_stack = []

  for k in range(H):
    farm = []
    for j in range(N):
      row = list(map(int, input().split()))
      farm.append(row)
      for i in range(M):
        if row[i] == 1:
          traverse.append((i, j, k, 0))
        if row[i] == -1:
          empty += 1
    farm_stack.append(farm)

  res = bfs(M, N, H, farm_stack, traverse, empty)
  print(res)

if __name__ == "__main__":
  main()

