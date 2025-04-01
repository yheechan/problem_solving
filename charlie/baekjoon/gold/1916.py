import math
import  heapq

class Graph:
    def __init__(self, N):
        self.N = N
        self.s = -1
        self.d = -1
        self.adj_nodes = {n: {} for n in range(self.N)}

    def add_edge(self, u, v, w):
        u -= 1  # 1-based index → 0-based index 변환
        v -= 1  
        # 이미 존재하는 간선이 있으면 더 작은 값으로 갱신
        if v in self.adj_nodes[u]:
            self.adj_nodes[u][v] = min(self.adj_nodes[u][v], w)
        else:
            self.adj_nodes[u][v] = w

    def __str__(self, ):
        content = "\n*** adj_nodes ***\n"

        for n, edges_dict in self.adj_nodes.items():
            content += f"{n}: "
            for n, w in edges_dict.items():
                content += f"({n}: {w}), "
            content += "\n"

        content += "\n*****************\n"

        content += f">> source, dest = {self.s}, {self.d}\n"
        return content


    def dijkstra(self,):
        short = [math.inf]*self.N
        short[self.s] = 0
        pq = [(0, self.s)] # for mean-heap

        while pq:
            dist, v = heapq.heappop(pq)
            if dist>short[v]:  # 이미 더 작은 값으로 갱신된 경우 무시
                continue

            for n, w in self.adj_nodes[v].items():
                sum_w = short[v] + w

                if short[n]>sum_w:  # 최단 거리 갱신
                    short[n] = sum_w
                    heapq.heappush(pq, (sum_w, n))

        return short[self.d]


def main():
    N = int(input())
    M = int(input())
    G = Graph(N)

    for _ in range(M):
        u, v, w = map(int, input().split())
        G.add_edge(u, v, w)

    s, d = map(int, input().split())
    G.s = s-1
    G.d = d-1

    res = G.dijkstra()
    print(res)



if __name__ == "__main__":
    main()

