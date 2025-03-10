# Notes by charlie

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

---
Last Update: 2025 Mar 10
