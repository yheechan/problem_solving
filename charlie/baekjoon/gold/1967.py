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

    def dfs_rec(self, visited, s, distance):
        visited[s] = 1
        longest = distance
        for n, w in self.adj_nodes[s].items():
            if visited[n] == 0:
                longest = max(longest, self.dfs_rec(visited, n, distance+w))
        return longest

    def dfs(self, s):
        visited = copy.deepcopy(self.visited)
        return self.dfs_rec(visited, s, 0)
    
    def diameter_of_graph(self, ):
        answer = -1

        # DFS for each std_node and find the longest path
        for std_node in range(self.n):
            res = self.dfs(std_node)
            answer = max(res, answer)

        return answer


def main():
    # n: number of nodes (1<=n<=10,000)
    n = int(input())

    G = Graph(n)
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        G.add_edge(u, v, w)

    res = G.diameter_of_graph()
    print(res)



if __name__ == "__main__":
    main()

