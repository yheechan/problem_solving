import copy
from collections import deque

DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs(M, N, farm, visited):
  result = 0
  # for each y_coor, to x_coor
  for j in range(N):
    for i in range(M):
      # check near cabbages
      traverse = deque([(i, j)])
      near_cab_cnt = 0
      while traverse:
        x, y = traverse.popleft()
        if farm[y][x] == 1 and visited[y][x] == 0:
          near_cab_cnt += 1
          visited[y][x] = 1
          for c in range(4):
            next_x, next_y = x+DIR[c][0], y+DIR[c][1]
            
            # This limits the traverse to be within the farm
            if (next_x>=0 and M>next_x) and (next_y>=0 and N>next_y):
              traverse.append((next_x, next_y))
      if near_cab_cnt > 0: result+= 1
  return result

def main():
  T = int(input())

  # For each test case
  for _ in range(T):
    # M: Horizontal size (가로)
    # N: Vertical size (세로)
    # K: number of cabbages planted
    M, N, K = map(int, input().split())
    farm = [[0]*M for _ in range(N)]
    visited = copy.deepcopy(farm)

    # Initialize farm with cabbages
    for _ in range(K):
      x, y = map(int, input().split())
      farm[y][x] = 1

    required_worms = bfs(M, N, farm, visited)
    print(required_worms)

if __name__ == "__main__":
  main()

