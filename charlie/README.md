# Notes by charlme

## 0. Algorithm Representatives
| algorithm | problem | problem_title |
|:--------|:------------|---------:|
| [Dynamic Programming](https://www.geeksforgeeks.org/dynamic-programming/) | [12865.py](./baekjoon/gold/12865.py) | [평범한 배낭](https://www.acmicpc.net/problem/12865) |
| [BFS](https://www.geeksforgeeks.org/dynamic-programming/) | [7576.py](./baekjoon/gold/7576.py) | [토마토](https://www.acmicpc.net/problem/7576) |
| [DFS+BFS](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/) | [1260.py](./baekjoon/silver/1260.py) | [DFS와 BFS](https://www.acmicpc.net/problem/1260) |
| [BFS+DIJKSTRA+Shortest](https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php) | [13549.py](./baekjoon/gold/13549.py) | [숨바꼭질 3](https://www.acmicpc.net/problem/13549) |
| [DIJKSTRA+python-heapq*](https://littlefoxdiary.tistory.com/3) | [1753.py](./baekjoon/gold/1753.py) | [최단경로](https://www.acmicpc.net/problem/1753)

## 1. CPP
### 1.0 Minor Optimizations

#### 1.0.1 Standard input/output
* code:
  ```
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  ```

#### 1.0.2 Next Line Character
* code:
  ```
  // use
  cout << "\n";
  // instead of
  cout << endl;
  ```


### 1.1 Data Types - Problems
* list of usefule data types in cpp:
  | data-type | problem | problem_title |
  |:--------|:------------|---------:|
  | [unordered_set](#121-unordered_set-ref) | [1920.cpp](./baekjoon/silver/1920.cpp) | [수 찾기](https://www.acmicpc.net/problem/1920) |
  | [unordered_map](#122-unordered_map-ref) | [10816.cpp](./baekjoon/silver/10816.cpp) | [숫자 카드 2](https://www.acmicpc.net/problem/10816) |
  | [vector](#123-vector-ref) | [1018.cpp](./baekjoon/silver/1018.cpp) | [체스판 다시 칠하기](https://www.acmicpc.net/problem/1018) |
  | [stack](#124-stack-ref) | [10828.cpp](./baekjoon/silver/10828.cpp) | [스택](https://www.acmicpc.net/problem/10828) |
  | [queue](#125-queue-ref) | [10845.cpp](./baekjoon/silver/10845.cpp) | [큐](https://www.acmicpc.net/problem/10845) |
  | [string](#126-string-ref) | [9012.cpp](./baekjoon/silver/9012.cpp) | [괄호](https://www.acmicpc.net/problem/9012) |
  | [pair](#127-pair-ref) | None | None |
  | [heapq](#128-heapq-ref) | [1753.py](./baekjoon/gold/1753.py) | [최단경로](https://www.acmicpc.net/problem/1753)

### 1.2 Data Types - And there functions
#### 1.2.1 unordered_set ([ref.](https://www.geeksforgeeks.org/unordered_set-in-cpp-stl/))
* initialization
  ```
  unordered_set<int> SET;
  ```
* ``insert()``: insert a value to the given set
  ```
  int x = 0;
  SET.insert(x);
  ```
* ``count()``: check whether a value exists within the given set
  ```
  // res == 1, exists
  // res == 0, not exists
  int res = SET.count(x);
  ```

#### 1.2.2 unordered_map ([ref.](https://www.geeksforgeeks.org/unordered_map-in-cpp-stl/))
* initialization
  ```
  // given key, value of any type
  unordered_map<int, string> MAP;
  ```
* intializing key2map data to the given map
  ```
  MAP[99] = "ninety-nine";
  MAP[2] = "two";
  ```
* ``count()``: check whether a key exists within the given map
  ```
  // res == 1, exists
  // res == 0, not exists
  int x = 2;
  int res = MAP.count(x);
  ```

#### 1.2.3 vector ([ref.](https://www.geeksforgeeks.org/vector-in-cpp-stl/))
* initialization
  ```
  // 1Dimensional vector
  vector<string> VECTOR(5);
  VECTOR[0] = "Hello World";

  // 2Dimensional vector
  // initalized with zeros
  vector<vector<int>> 2DVector(5, vector<int>(5, 0));
  2DVector[0][0] = 1;
  ```
* accessing vector
  ```
  String VAR = VECTOR[0];
  int ONE = 2DVector[0][0];
  ```

#### 1.2.4 stack ([ref.](https://www.geeksforgeeks.org/stack-in-cpp-stl/))
* initialization
  ```
  stack<int> STACK;
  ```
* ``push()``: pushes an element to the top of the stack.
  ```
  STACK.push(1);
  ```
* ``pop()``: pops (or removes) the top most element from the stack.
  ```
  STACK.pop();
  ```
* ``size()``: returns the number of elements in the stack.
  ```
  int size = STACK.size();
  ```
* ``top()``: returns the value of the top most element from the stack.
  ```
  int top_value = STACK.top();
  ```
* ``empty()``: returns ``true`` if the stack is empty, ``false`` otherwise.


#### 1.2.5 queue ([ref.](https://www.geeksforgeeks.org/queue-cpp-stl/))
* initialization
  ```
  queue<int> QUEUE;
  ```
* ``push()``: adds an element to the back of the queue.
  ```
  QUEUE.push(1);
  ```
* ``pop()``: deletes (or removes) the front most element from the queue.
  ```
  QUEUE.pop();
  ```
* ``size()``: returns the number of elements in the queue
  ```
  int size = QUEUE.size();
  ```
* ``front()``: returns the value of the front most element from the queue.
  ```
  int top_value = QUEUE.front();
  ```
* ``back()``: returns the value of the back most element from the queue.
  ```
  int top_value = QUEUE.back();
  ```
* ``empty()``: return ``true`` if the stack is empty, ``false`` otherwise.


#### 1.2.6 string ([ref.](https://www.geeksforgeeks.org/strings-in-cpp/))
* initialization
  ```
  string STREAM = "Hello World";
  ```
* ``size()``: returns the length of the string.
  ```
  int str_length = STREAM.size();
  ```
* accessing a character from the string.
  ```
  char c = STREAM[1];
  ```
* ``find()``: searches for a certain substring within a string, returning the position of the first character of the substring if found. Otherwise, returns ``string::npos``.
  ```
  if (STREAM.find("World") != string::npos) cout << "Substring Found\n";
  else cout << "Substring NOT FOUND\n";
  ```

#### 1.2.7 pair ([ref.](https://www.geeksforgeeks.org/pair-in-cpp-stl/))
* initialization
  ```
  pair<int, int> p1 = {3, 5};
  ```
* accessing pair data
  ```
  int e1 = p1.first;
  int e2 = p1.second;
  ```

### 1.2.8 heapq ([ref.](https://littlefoxdiary.tistory.com/3))
``heapq`` works as a mean-heap in which orders the elements in list as a binary tree form. At all time, parent node is greater than its children nodes.
* initializatoin (usage):
  ```
  ls = [(0, "A")]
  num, ch = heapq.heappop(ls)
  ```
* ``heapq.heappop(ls)``: Pops the element that has the mean value for first element in tuple
  ```
  ls = [(0, "A")]
  num, ch = heapq.heappop(ls)
  ```
* ``heapq.heappush(ls, (2, "C"))``: Pushes a new element and sor

# 2. Python
### 2.0 Minor Optimizations

#### 2.0.1 Standard input/output
* code:
  ```
  x, y, z = map(int, input.split())
  ```

### 2.1 Data Types - Problems
* list of usefule data types in cpp:
  | data-type | problem | problem_title |
  |:--------|:------------|---------:|
  | [deque](#221-deque-ref) | [1260.cpp](./baekjoon/silver/1260.py) | [DFS와 BFS](https://www.acmicpc.net/problem/1260) |
  | [list](#222-list-ref) | [1260.cpp](./baekjoon/silver/1260.py) | [DFS와 BFS](https://www.acmicpc.net/problem/1260) |

### 2.2 Data Types - And there functions
#### 2.2.1 deque ([ref.](https://www.geeksforgeeks.org/deque-in-python/))
* initialization
  ```
  DEQUE = deque([1, 2])
  ```
* ``append(x)``: appends an element to the right-end of the deque.
  ```
  DEQUE.append(1);
  ```
* ``DEQUE.appendleft(x)``: appends an element to the left-end of the deque.
  ```
  DEQUE.appendleft(1);
  ```
* ``pop()``: removed and return the element from the right-end of the deque.
  ```
  x = DEQUE.pop()
  ```
* ``popleft()``: removed and return the element from the left-end of the deque.
  ```
  x = DEQUE.popleft()
  ```
* ``count(x)``: counts the number of occurrences of value in the deque.
  ```
  x = DEQUE.count(2)
  ```

#### 2.2.2 list ([ref.](https://www.geeksforgeeks.org/python-lists/))
* initialization
  ```
  LIST = list()
  ```
* ``remove(x)``: removed the first occurence of an element.
  ```
  LIST.remove(3)
  ```


---
Last Update: 2025 Mar 28

