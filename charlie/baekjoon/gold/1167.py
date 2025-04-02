import copy

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj_nodes = {x: {} for x in range(n)}
        self.visited = [0]*n

    def add_edge(self, u, v, w):
        u -= 1
        v -= 1
        if v in self.adj_nodes[u]:
            self.adj_nodes[u][v] = min(self.adj_nodes[u][v], w)
        else:
            self.adj_nodes[u][v] = w

        # Undirected Graph
        if u in self.adj_nodes[v]:
            self.adj_nodes[v][u] = min(self.adj_nodes[v][u], w)
        else:
            self.adj_nodes[v][u] = w

    def __str__(self, ):
        content = "\n*** adj_nodes ***\n"

        for n, edges_dict in self.adj_nodes.items():
            content += f"{n}: "
            for n, w in edges_dict.items():
                content += f"({n}: {w}), "
            content += "\n"

        content += "*****************\n"

        return content


    def dfs(self, s):
        visited = copy.deepcopy(self.visited)

        stack = []
        visited[s] = 1
        longest = (s, 0)
        for n, w in self.adj_nodes[s].items():
            stack.append((n, w, w))

        while stack:
            cn, cw, cd = stack.pop()
            visited[cn] = 1
            if cd>longest[1]:
                longest = (cn, cd)

            for nn, nw in self.adj_nodes[cn].items():
                if visited[nn] == 0:
                    stack.append((nn, nw, nw+cd))

        return longest


def main():
    # n: number of nodes (1<=n<=10,000)
    n = int(input().strip())

    G = Graph(n)
    for _ in range(n-1):
        u, v, w = map(int, input().strip().split())
        G.add_edge(u, v, w)

    res = G.dfs(0)
    res = G.dfs(res[0])
    print(res[1])


if __name__ == "__main__":
    main()

