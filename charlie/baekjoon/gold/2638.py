import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()
N, M = map(int, data[0].split())
board = [list(map(int, line.split())) for line in data[1:N+1]]

DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def inrange(x, y):
    return 0 <= x < M and 0 <= y < N

def mark_outer():
    visited = [[False]*M for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    while q:
        x, y = q.popleft()
        for dx, dy in DIR:
            nx, ny = x + dx, y + dy
            if inrange(nx, ny) and not visited[ny][nx]:
                if board[ny][nx] == 0:
                    visited[ny][nx] = True
                    q.append((nx, ny))
                elif board[ny][nx] == 1:
                    count[ny][nx] += 1  # 녹을 수 있는 치즈 체크용

hour = 0
while True:
    count = [[0]*M for _ in range(N)]  # 치즈 인접 OUTER 공기 수
    mark_outer()

    melted = False
    for y in range(N):
        for x in range(M):
            if board[y][x] == 1 and count[y][x] >= 2:
                board[y][x] = 0
                melted = True

    if not melted:
        break
    hour += 1

print(hour)

