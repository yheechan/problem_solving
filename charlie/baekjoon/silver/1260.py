from collections import deque
import copy

WHITE = 0
BLACK = 1
GRAY = 2

class Node:
  def __init__(self,):
    self.state = WHITE
    self.edges = list()

class Graph:
  def __init__(self, N, M, V):
    self.N = N
    self.M = M
    self.V = V
    self.nodes = {x: Node() for x in range(1, N+1)}


def DFS(graph, v):
  if len(graph.nodes[v].edges) == 0:
    if graph.nodes[v].state == WHITE:
      graph.nodes[v].state = BLACK
      print(v, end=' ')
    return

  if graph.nodes[v].state == WHITE:
    graph.nodes[v].state = BLACK
    print(v, end=' ')
    
  while len(graph.nodes[v].edges) != 0:
    next_node = graph.nodes[v].edges[0]
    graph.nodes[v].edges.remove(next_node)
    if graph.nodes[next_node] != BLACK:
      DFS(graph, next_node)
    
  
def BFS(graph, v):
  if graph.nodes[v].state == WHITE:
    graph.nodes[v].state = BLACK
    print(v, end=' ')
    return

  for next_node_idx in graph.nodes[v].edges:
    if graph.nodes[next_node_idx].state == WHITE:
      graph.nodes[next_node_idx].state = BLACK
      print(next_node_idx, end=' ')

  while len(graph.nodes[v].edges) != 0:
    next_node = graph.nodes[v].edges[0]
    graph.nodes[v].edges.remove(next_node)
    if graph.nodes[next_node] != BLACK:
      BFS(graph, next_node)

    


def main():
  N, M, V = map(int, input().split())
  G = Graph(N, M, V)

  # get input and make graph
  graph = {}
  for i in range(M):
    x, y = map(int, input().split())
    if x not in graph:
      graph[x] = []
    if y not in graph:
      graph[y] = []
    if y not in graph[x]:
      graph[x].append(y)
    if x not in graph[y]:
      graph[y].append(x)

  # sort and save it as deque data type
  for node, edges in graph.items():
    G.nodes[node].edges = sorted(edges)


  dfs_graph = copy.deepcopy(G)
  bfs_graph = copy.deepcopy(G)
  
  DFS(dfs_graph, V)
  print()
  BFS(bfs_graph, V)
  

if __name__ == "__main__":
  main()
