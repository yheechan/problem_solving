import sys
import heapq
import math

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj_list = {i: {} for i in range(V)}

    def add_edge(self, u, v, w):
        u -= 1  # 1-based index → 0-based index 변환
        v -= 1  
        # 이미 존재하는 간선이 있으면 더 작은 값으로 갱신
        if v in self.adj_list[u]:
            self.adj_list[u][v] = min(self.adj_list[u][v], w)
        else:
            self.adj_list[u][v] = w

def dijkstra(G, K):
    K -= 1
    short = [math.inf] * G.V
    short[K] = 0
    pq = [(0, K)]  # (거리, 노드)

    while pq:
        dist, v = heapq.heappop(pq)
        if dist > short[v]:  # 이미 더 작은 값으로 갱신된 경우 무시
            continue

        for n, w in G.adj_list[v].items():
            sum_w = short[v] + w
            if sum_w < short[n]:  # 최단 거리 갱신
                short[n] = sum_w
                heapq.heappush(pq, (sum_w, n))

    return short

def main():
    input = sys.stdin.readline
    V, E = map(int, input().split())
    K = int(input())

    G = Graph(V)
    for _ in range(E):
        u, v, w = map(int, input().split())
        G.add_edge(u, v, w)

    res = dijkstra(G, K)
    print("\n".join(str(s) if s != math.inf else "INF" for s in res))

if __name__ == "__main__":
    main()

