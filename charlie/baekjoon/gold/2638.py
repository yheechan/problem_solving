import sys
from collections import deque

UNKNOWN = -1
OUTER = 0
INNER = 1
CHEEZE = 2
MELTING_CHEEZE = 3

DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]

class Grid:
    def __init__(self, ):
        self.identity = UNKNOWN

class Paper:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.grids = [[Grid() for _ in range(M)] for _ in range(N)]
        self.template = []

    def __str__(self, type=1):
        if type == 1:
            content = "*** paper ***\n"
            for row in self.template:
                content += str(row)+"\n"
            content += "*************"
        elif type == 2:
            content = "*** grids ***\n"
            for row in self.grids:
                for g in row:
                    content += f"{g.identity} "
                content += "\n"
            content += "*************\n"
        return content

    def inrange(self, x, y):
        if (x>-1 and self.M>x) and (y>-1 and self.N>y):
            return True
        return False

    def mark_outer(self, ):
        visited = [[0]*self.M for _ in range(self.N)]
        outer_q = deque([(0, 0)])
        cheeze_q = deque()
        inner_q = deque()


        while outer_q:
            cx, cy = outer_q.popleft()
            self.grids[cy][cx].identity = OUTER
            visited[cy][cx] = 1

            for d in range(4):
                nx, ny = cx+DIR[d][0], cy+DIR[d][1]

                if self.inrange(nx, ny):
                    if visited[ny][nx] == 0:
                        if self.template[ny][nx] == 0:
                            outer_q.append((nx, ny))
                        elif self.template[ny][nx] == 1:
                            visited[ny][nx] = 2
                            cheeze_q.append((nx, ny))

        while cheeze_q:
            cx, cy = cheeze_q.popleft()
            if visited[cy][cx] == 1:
                continue
            self.grids[cy][cx] = CHEEZE
            visited[cy][cx] = 1

            outter_layer_cnt = 0
            for d in range(4):
                nx, ny = cx+DIR[d][0], cy+DIR[d][1]

                if self.inrange(nx, ny):
                    # OUTER
                    if visited[ny][nx] == 1 \
                        and self.template[ny][nx] == 0:
                            outer_layer_cnt += 1
                    # INNER
                    elif visited[ny][nx] == 0 \
                        and self.template[ny][nx] == 0:
                            inner_q.append((nx, ny))
                    # something
                    elif vis
                        elif self.template[ny][nx] == 1:
                            cheeze_q.append((nx, ny))
            if outter_layer_cnt > 1:
                self.grids[cy][cx] = MELTING_CHEEZE

        while inner_q:
            cx

def main():
    # N: vertical 세로
    # M: horizontal 가로
    input = sys.stdin.read
    data = input().split("\n")
    N, M = map(int, data[0].strip().split())

    P = Paper(N, M)

    for i in range(1, N+1):
        row = list(map(int, data[i].split()))
        P.template.append(row)

    print(P.__str__(1))
    P.mark_outer()
    print(P.__str__(2))

if __name__ == "__main__":
    main()

