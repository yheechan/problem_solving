from collections import deque

def add_node(graph, n):
  if n not in graph:
    graph[n] = []

def add_edge(graph, x, y):
  # undirected graph
  graph[x].append(y)
  graph[y].append(x)

def sort_edges(graph):
  for n, edges in graph.items():
    graph[n].sort()


def dfs_rec(graph, visited, v):
  visited[v] = True
  print(v, end=' ')

  for i in graph[v]:
    if not visited[i]:
      dfs_rec(graph, visited, i)
  

def dfs(graph, v, N):
  visited = [False for _ in range(N+1)]
  dfs_rec(graph, visited, v)



def bfs(graph, v, N):
  visited = [False for _ in range(N+1)]

  visited[v] = True
  Q = deque([v])

  res = []

  while Q:
    curr = Q.popleft()
    res.append(curr)

    for i in graph[curr]:
      if not visited[i]:
        visited[i] = True
        Q.append(i)
  
  out = " ".join(map(str, res))
  print(out)



def main():
  N, M, V = map(int, input().split())

  graph = {i: [] for i in range(1, N+1)}

  # get input and make graph
  for i in range(M):
    x, y = map(int, input().split())
    add_node(graph, x)
    add_node(graph, y)
    add_edge(graph, x, y)

  sort_edges(graph)


  dfs(graph, V, N)
  print()
  bfs(graph, V, N)
  
  

if __name__ == "__main__":
  main()



