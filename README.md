# problem_solving

## 1. Summary of Solved Problems
<!-- START_TABLE_SUMMARY -->
| User    | Source      | Level   |   Solved |
|:--------|:------------|:--------|---------:|
| Andy    | baekjoon    | bronze  |        3 |
| Charlie | baekjoon    | bronze  |        4 |
| Andy    | baekjoon    | silver  |        6 |
| Charlie | baekjoon    | silver  |       12 |
| Andy    | programmers | lv1     |        0 |
| Charlie | programmers | lv1     |        1 |
<!-- END_TABLE_SUMMARY -->

## 2. Lists of Solved Problems
<!-- START_TABLE_LIST -->
|   Idx | Source      | Level   | Problem          | Andy   | Charlie   |
|------:|:------------|:--------|:-----------------|:-------|:----------|
|     1 | baekjoon    | bronze  | 1110             | ✅     | ✅        |
|     2 | baekjoon    | bronze  | 13458            | ❌     | ✅        |
|     3 | baekjoon    | bronze  | 2331             | ✅     | ✅        |
|     4 | baekjoon    | bronze  | 2798             | ✅     | ✅        |
|     5 | baekjoon    | silver  | 1003             | ❌     | ✅        |
|     6 | baekjoon    | silver  | 1018             | ✅     | ✅        |
|     7 | baekjoon    | silver  | 10816            | ❌     | ✅        |
|     8 | baekjoon    | silver  | 10828            | ✅     | ✅        |
|     9 | baekjoon    | silver  | 10845            | ✅     | ✅        |
|    10 | baekjoon    | silver  | 11650            | ✅     | ✅        |
|    11 | baekjoon    | silver  | 11866            | ❌     | ✅        |
|    12 | baekjoon    | silver  | 1676             | ✅     | ✅        |
|    13 | baekjoon    | silver  | 1874             | ❌     | ✅        |
|    14 | baekjoon    | silver  | 1920             | ❌     | ✅        |
|    15 | baekjoon    | silver  | 2164             | ✅     | ✅        |
|    16 | baekjoon    | silver  | 9012             | ❌     | ✅        |
|    17 | programmers | lv1     | 택배_상자_꺼내기 | ❌     | ✅        |
<!-- END_TABLE_LIST -->

## 3. Instructions to Sign-Up as User and Add Solved Problems
1. Clone this repository to your local machine.
    ```
    git clone https://github.com/yheechan/problem_solving.git
    ```
2. Create a branch of your own and checkout to your own branch.
    ```
    git checkout -b <user-name>
    ```
3. Create a directory with ``<user-name>`` and begin adding codes for solved problems.
    ```
    mkdir <user-name>
    ```
4. Solve problems and add source code file to your directory (as explained in [section4](#4-directory-structure-to-add-solved-problems)).
    ```
    ./<user-name>/<source>/<level>/<problem-id>.py
    ```
5. **Push and send PR**
    ```
    git status
    git add .
    git commit -m "<user-name> solved <source> <level> <problem-id>"
    git push origin <user-name>
    ```

## 4. Directory Structure to Add Solved Problems
```
./problem_solving/
    ├── README.md
    ├── <user-name>/
    │   └── <source>/
    │       ├── <level>/
    │       │   ├── <problem-id>.py
    │       └── silver/
    │           ├── 11650.py
    │           └── input
    └── update-README.py
```
* ``<user-name>``: Your own username.
* ``<source>``: Company name that produced the problem (e.g., programmers, baekjoon, leetcode).
* ``<level>``: Name of the level of the problem designated by the company (e.g., bronze, silver, easy, hard, etc.)
* ``<problem-id>.py``: The unique id of the problem designated by the company (e.g., 11650.py).


## 5. Command Usage
* Update ``README.md`` file to follow up to the newly solved problems by users.
  * command: ``python3 update-README.py``

---

<!-- START_LAST_UPDATED -->
Last Update: 2025 Mar 10
<!-- END_LAST_UPDATED -->
