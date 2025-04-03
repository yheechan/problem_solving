import sys
from collections import deque

NORM = 0
START = 1
END = 2

class Square:
    def __init__(self, ):
        self.type = NORM
        self.dest = -1
        self.visited = 0

class Board:
    def __init__(self, ):
        self.board = [Square() for _ in range(101)]

    def add_edge(self, x, y):
        self.board[x].type = START
        self.board[x].dest = y
        self.board[y].type = END
        self.board[y].dest = x

    def __str__(self,):
        content = "*** board ***\n"
        for i, square in enumerate(self.board):
            content += f"{i}: {square.type}, "
            if i%10 == 0:
                content += "\n"
        content += "*************\n"
        return content

    def inrange(self, pos):
        if pos > 0 and 101 > pos:
            return True
        return False

    def bfs(self, ):
        traverse = deque([(1, 0)])

        while traverse:
            pos, turn = traverse.popleft()
            self.board[pos].visited = 1

            if pos == 100:
                return turn
            
            n_turn = turn+1
            for dice in range(1, 7):
                n_pos = pos + dice

                if self.inrange(n_pos):
                    if self.board[n_pos].type == START:
                        n_pos = self.board[n_pos].dest
                    if self.board[n_pos].visited == 0:
                        traverse.append((n_pos, n_turn))


def main():
    # N: number of ladders
    # M: number of snakes

    input = sys.stdin.read
    data = input().split("\n")
    N, M = map(int, data[0].strip().split())

    B = Board()

    for i in range(1, 1+N):
        x, y = map(int, data[i].strip().split())
        B.add_edge(x, y)

    for i in range(1+N, 1+N+M):
        u, v = map(int, data[i].strip().split())
        B.add_edge(u, v)

    res = B.bfs()
    print(res)


if __name__ == "__main__":
    main()

