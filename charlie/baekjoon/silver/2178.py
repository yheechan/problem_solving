from collections import deque

DIR = [[0,1], [1,0], [0,-1], [-1,0]]

def inrange(x, y, x_lim, y_lim):
    if (x>-1 and x_lim>x) and (y>-1 and y_lim>y):
        return True
    return False


def bfs(mapp, N, M):
    target = (M-1, N-1)
    tx, ty = target

    traverse = deque([(0, 0, 1)])
    visited = [[0]*M for _ in range(N)]

    while traverse:
        cx, cy, cs = traverse.popleft()

        if cx == tx and cy == ty:
            return cs

        ns = cs + 1
        
        for c in range(4):
            nx, ny = cx+DIR[c][1], cy+DIR[c][0]

            if inrange(nx, ny, M, N) and visited[ny][nx] == 0 and mapp[ny][nx] != 0:
                visited[ny][nx] = 1
                traverse.append((nx, ny, ns))


def main():
    # N: 세로 vertical
    # M: 가로 horizontal
    N, M = map(int, input().split())

    mapp = []
    for _ in range(N):
        row = [int(x) for x in input().strip()]
        mapp.append(row)


    res = bfs(mapp, N, M)
    print(res)


if __name__ == "__main__":
    main()

