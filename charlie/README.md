# Notes by charlie

## 1. CPP
### 1.0 Optimize standard input/output
* code:
  ```
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  ```

### 1.1 Data Types - Problems
* list of usefule data types in cpp:
  | data-type | problem | problem_title |
  |:--------|:------------|---------:|
  | [unordered_set](#121-unordered_set) | [1920.cpp](./baekjoon/silver/1920.cpp) | [수 찾기](https://www.acmicpc.net/problem/1920) |
  | [unordered_map](#122-unordered_map) | [10816.cpp](./baekjoon/silver/10816.cpp) | [숫자 카드 2](https://www.acmicpc.net/problem/10816) |
  | [vector](#123-vector) | [1018.cpp](./baekjoon/silver/1018.cpp) | [체스판 다시 칠하기](https://www.acmicpc.net/problem/1018) |
  | [stack](#124-stack) | [10828.cpp](./baekjoon/silver/10828.cpp) | [스택](https://www.acmicpc.net/problem/10828) |
  | [queue](#125-queue) | [10845.cpp](./baekjoon/silver/10845.cpp) | [큐](https://www.acmicpc.net/problem/10845) |

### 1.2 Data Types - And there functions
#### 1.2.1 unordered_set
* initialization
  ```
  unordered_set<int> SET;
  ```
* insert a value to the given set
  ```
  int x = 0;
  SET.insert(x);
  ```
* check whether a value exists within the given set
  ```
  // res == 1, exists
  // res == 0, not exists
  int res = SET.count(x);
  ```

#### 1.2.2 unordered_map
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
* check whether a key exists within the given map
  ```
  // res == 1, exists
  // res == 0, not exists
  int x = 2;
  int res = MAP.count(x);
  ```

#### 1.2.3 vector


#### 1.2.4 stack


#### 1.2.5 queue

