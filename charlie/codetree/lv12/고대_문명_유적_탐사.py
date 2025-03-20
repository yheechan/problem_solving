from collections import deque

BOARD_SIZE = 5
SELECT_SIZE = 3

# 90, 180, 270

def myPrint(K, M, B, Q):
  print(K, M)
  print(B)
  print(Q)

class Board:
    def __init__(self):
        self.board = [[-1 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def rotate(self, x, y, cnt):
      result = Board()
      result.board = [row for row in self.board]

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
    


    myPrint(K, M, B, Q)

    result = B.rotate(1, 1, 1)

    myPrint(K, M, result, Q)
    

if __name__ == "__main__":
    main()
