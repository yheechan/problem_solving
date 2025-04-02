# problem_solving

## 1. Summary of Solved Problems
<!-- START_TABLE_SUMMARY -->
| User    | Source      | Level   |   Solved |
|:--------|:------------|:--------|---------:|
| Andy    | baekjoon    | bronze  |        3 |
| Charlie | baekjoon    | bronze  |        4 |
| Andy    | baekjoon    | gold    |        0 |
| Charlie | baekjoon    | gold    |        7 |
| Andy    | baekjoon    | silver  |        6 |
| Charlie | baekjoon    | silver  |       18 |
| Andy    | programmers | lv1     |        0 |
| Charlie | programmers | lv1     |        1 |
| Andy    | codetree    | lv12    |        0 |
| Charlie | codetree    | lv12    |        1 |
<!-- END_TABLE_SUMMARY -->

## 2. Lists of Solved Problems
<!-- START_TABLE_LIST -->
|   Idx | Source      | Level                                      | Problem                  | Andy   | Charlie   |
|------:|:------------|:-------------------------------------------|:-------------------------|:-------|:----------|
|     1 | baekjoon    | <span style="color:#CD7F32;">bronze</span> | 1110                     | ✅      | ✅         |
|     2 | baekjoon    | <span style="color:#CD7F32;">bronze</span> | 13458                    | ❌      | ✅         |
|     3 | baekjoon    | <span style="color:#CD7F32;">bronze</span> | 2331                     | ✅      | ✅         |
|     4 | baekjoon    | <span style="color:#CD7F32;">bronze</span> | 2798                     | ✅      | ✅         |
|     5 | baekjoon    | <span style="color:#FFD700;">gold</span>   | 12865                    | ❌      | ✅         |
|     6 | baekjoon    | <span style="color:#FFD700;">gold</span>   | 13549                    | ❌      | ✅         |
|     7 | baekjoon    | <span style="color:#FFD700;">gold</span>   | 1753                     | ❌      | ✅         |
|     8 | baekjoon    | <span style="color:#FFD700;">gold</span>   | 1916                     | ❌      | ✅         |
|     9 | baekjoon    | <span style="color:#FFD700;">gold</span>   | 1931                     | ❌      | ✅         |
|    10 | baekjoon    | <span style="color:#FFD700;">gold</span>   | 7569                     | ❌      | ✅         |
|    11 | baekjoon    | <span style="color:#FFD700;">gold</span>   | 7576                     | ❌      | ✅         |
|    12 | baekjoon    | <span style="color:#C0C0C0;">silver</span> | 1003                     | ❌      | ✅         |
|    13 | baekjoon    | <span style="color:#C0C0C0;">silver</span> | 1012                     | ❌      | ✅         |
|    14 | baekjoon    | <span style="color:#C0C0C0;">silver</span> | 1018                     | ✅      | ✅         |
|    15 | baekjoon    | <span style="color:#C0C0C0;">silver</span> | 10816                    | ❌      | ✅         |
|    16 | baekjoon    | <span style="color:#C0C0C0;">silver</span> | 10828                    | ✅      | ✅         |
|    17 | baekjoon    | <span style="color:#C0C0C0;">silver</span> | 10845                    | ✅      | ✅         |
|    18 | baekjoon    | <span style="color:#C0C0C0;">silver</span> | 11650                    | ✅      | ✅         |
|    19 | baekjoon    | <span style="color:#C0C0C0;">silver</span> | 11866                    | ❌      | ✅         |
|    20 | baekjoon    | <span style="color:#C0C0C0;">silver</span> | 1260                     | ❌      | ✅         |
|    21 | baekjoon    | <span style="color:#C0C0C0;">silver</span> | 14501                    | ❌      | ✅         |
|    22 | baekjoon    | <span style="color:#C0C0C0;">silver</span> | 14940                    | ❌      | ✅         |
|    23 | baekjoon    | <span style="color:#C0C0C0;">silver</span> | 1676                     | ✅      | ✅         |
|    24 | baekjoon    | <span style="color:#C0C0C0;">silver</span> | 1697                     | ❌      | ✅         |
|    25 | baekjoon    | <span style="color:#C0C0C0;">silver</span> | 1874                     | ❌      | ✅         |
|    26 | baekjoon    | <span style="color:#C0C0C0;">silver</span> | 1920                     | ❌      | ✅         |
|    27 | baekjoon    | <span style="color:#C0C0C0;">silver</span> | 2164                     | ✅      | ✅         |
|    28 | baekjoon    | <span style="color:#C0C0C0;">silver</span> | 2178                     | ❌      | ✅         |
|    29 | baekjoon    | <span style="color:#C0C0C0;">silver</span> | 9012                     | ❌      | ✅         |
|    30 | codetree    | lv12                                       | ancient_ruin_exploration | ❌      | ✅         |
|    31 | programmers | lv1                                        | 택배_상자_꺼내기                | ❌      | ✅         |
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
  * Change the file's extension to ``*.hidden`` to prevent this script to count the **unsolved problem**.

---

<!-- START_LAST_UPDATED -->
Last Update: 2025 Apr 02
<!-- END_LAST_UPDATED -->
