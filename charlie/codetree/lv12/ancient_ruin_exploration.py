from collections import deque

BOARD_SIZE = 5
SELECT_SIZE = 3

def myPrint(K, M, B, Q):
  print(K, M)
  print(B)
  print(Q)

class Board:
    def __init__(self):
        self.board = [[-1 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def in_range(self, y, x):
      return 0 <= y < BOARD_SIZE and 0 <= x < BOARD_SIZE

    def rotate(self, y, x, cnt):
      result = Board()
      result.board = [row[:] for row in self.board]

      for _ in range(cnt):
        tmp = result.board[y-1][x+1]
        result.board[y-1][x+1] = result.board[y-1][x-1]
        result.board[y-1][x-1] = result.board[y+1][x-1]
        result.board[y+1][x-1] = result.board[y+1][x+1]
        result.board[y+1][x+1] = tmp
        tmp = result.board[y-1][x]
        result.board[y-1][x] = result.board[y][x-1]
        result.board[y][x-1] = result.board[y+1][x]
        result.board[y+1][x] = result.board[y][x+1]
        result.board[y][x+1] = tmp

      return result

    def calculate_score(self):
      score = 0
      visit = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
      dy, dx = [0, 1, 0, -1], [1, 0, -1, 0] # R, U, L, D

      # traverse BFS for the given matrix map
      for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
          if not visit[i][j]:
            # START and impelement BFS structure here: FLOOD FILL
            q, trace = deque([(i, j)]), deque([(i, j)])
            visit[i][j] = True
            while q:
              cur = q.popleft()
              for k in range(4):
                ny, nx = cur[0] + dy[k], cur[1] + dx[k]

                # Indicate all matching blocks
                if self.in_range(ny, nx) and self.board[ny][nx] == self.board[cur[0]][cur[1]] and not visit[ny][nx]:
                  q.append((ny, nx))
                  trace.append((ny, nx))
                  visit[ny][nx] = True

            # At standard of specific block (e.g., block-type) check the score
            if len(trace) >= 3:
              score += len(trace)
              while trace:
                t = trace.popleft()
                self.board[t[0]][t[1]] = 0
      return score

    def fill(self, que):
      for j in range(BOARD_SIZE):
        for i in reversed(range(BOARD_SIZE)):
          if self.board[i][j] == 0:
            self.board[i][j] = que.popleft()
      

    def __str__(self):
      return_str = ""
      for row in self.board:
        return_str += str(row)+"\n"
      return return_str
      

def main():
    K, M = map(int, input().split())
    B = Board()

    # init board values
    for i in range(BOARD_SIZE):
        B.board[i] = list(map(int, input().split()))
    
    Q = deque()
    for t in list(map(int, input().split())):
        Q.append(t)



    # FOR K TURNS
    for _ in range(K):
      maxScore = 0
      maxScoreBoard = None

      # attempt less turn first on all possible x, y
      for cnt in range(1, 4):
        for sx in range(1, BOARD_SIZE - SELECT_SIZE + 2):
          for sy in range(1, BOARD_SIZE - SELECT_SIZE + 2):
            rotated = B.rotate(sy, sx, cnt)
            score = rotated.calculate_score()
            if maxScore < score:
              maxScore = score
              maxScoreBoard = rotated

      if maxScoreBoard is None:
        break
      B = maxScoreBoard

      while True:
        B.fill(Q)
        newScore = B.calculate_score()
        if newScore == 0:
          break
        maxScore += newScore

      print(maxScore, end= " ")

    

if __name__ == "__main__":
    main()
