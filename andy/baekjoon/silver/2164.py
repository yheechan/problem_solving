from collections import deque

N = int(input())
dq = deque(list(range(1,N+1)))

i = 0
while len(dq) > 1:
    if i%2 == 0:
        dq.popleft()
    else:
        dq.append(dq.popleft())
    i += 1

print(dq[0])

        
