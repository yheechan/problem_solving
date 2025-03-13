from collections import deque

BOARD_SIZE = 5
SELECT_SIZE = 3

class Board:
    def __init__(self):
        self.board = [[-1 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def main():
    K, M = map(int, input().split())
    B = Board()

    # init board values
    for i in range(BOARD_SIZE):
        B.board[i] = list(map(int, input().split()))
    
    next_vals = deque()
    for t in list(map(int, input().split())):
        next_vals.append(t)
    
    print(K, M)
    for row in B.board:
        print(row)
    print(next_vals)
    

if __name__ == "__main__":
    main()
