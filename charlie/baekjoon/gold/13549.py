from collections import deque
import math

DIR = [2, -1, 1]

def inrange(x):
    if x>-1 and 100001>x:
        return True
    return False

def bfs(me, target):
    visited = [0]*100001            # If all outgoing edges of this node is calculated, it is visited
    distance = [math.inf]*100001    # shortest distance from starting node to this node
    distance[me] = 0                # starting node is 0

    traverse = deque([(me, 0)])

    while traverse:
        cur_me, cur_time = traverse.popleft()

        if cur_me == target:
            return cur_time

        next_time = cur_time
        shortest = (-1, math.inf)
        for c in range(3):
            if c > 0:
                next_me = cur_me+DIR[c]
                next_time = cur_time+1
            else:
                next_me = cur_me*DIR[c]

            # if the node is not visited, and the calculated distance is shorter
            if inrange(next_me) and visited[next_me] == 0 and next_time < distance[next_me]:
                distance[next_me] = next_time
                if shortest[1] > next_time:
                    traverse.append((next_me, next_time))

        # when this node is not visited before (for shortest route)
        if visited[cur_me] == 0:
            visited[cur_me] = 1

    return -1

def main():
    me, target = map(int, input().split())
    res = bfs(me, target)
    print(res)

if __name__ == "__main__":
    main()

