from collections import deque

DIR = [2, -1, 1]

def bfs(me, target):
    visited = [0]*100001
    depths = 0
    traverse = deque([(me, 0)])

    while traverse:
        cur_me, cur_depths = traverse.popleft()

        # when this node is not visited before (for shortest route)
        if visited[cur_me] == 0:
            visited[cur_me] = 1

        if cur_me == target:
            return cur_depths

        next_depths = cur_depths

        for c in range(3):
            if c > 0:
                next_me = cur_me+DIR[c]
                # check nodes of next depths
                next_depths = cur_depths+1
            else:
                next_me = cur_me*DIR[c]
            
            # traverse next_me if it is in range 0~100,000
            if next_me>-1 and 100001>next_me:
                traverse.append((next_me, next_depths))

    return -1

def main():
    me, target = map(int, input().split())
    res = bfs(me, target)
    print(res)

if __name__ == "__main__":
    main()

