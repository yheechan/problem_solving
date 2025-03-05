# Notes by Andy

## 1. python
### I/O
input : 2 7
* input()
```
N = input()         -> 2 7
N = input().split() -> ['2', '7']
```
* readline() is faster than input(). It return string + '\n'. For removing \n, use the strip()
``` 
N = sys.stdin.readline()          -> 2 7 \n
N = sys.stdin.readline().strip()  -> 2 7
N = sys.stdin.readline().split()  -> ['2', '7']   (no \n here)

```
* map() return iterable object
```
N = map(int, input().split())       -> map object
N = list(map(int, input().split())) -> [2, 7]
```


### Data structure
* stack
```
stack = []
stack.append()
stack.pop()
```

* queue
```
queue = []
queue.append()
queue.pop()
queue.pop(0) O(N)
```

* deque
```
from collections import deque

dq = deque(list(range(N)))
dq.append()
dq.appendleft()	 O(1)			
dq.pop()
dq.popleft()
```