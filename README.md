# problem_solving

## 1. Summary of Solved Problems
<!-- START_TABLE_SUMMARY -->
| User    | Source   | Level   |   Solved |
|:--------|:---------|:--------|---------:|
| Andy    | baekjoon | bronze  |        2 |
| Charlie | baekjoon | bronze  |        2 |
| Andy    | baekjoon | silver  |        0 |
| Charlie | baekjoon | silver  |        2 |
<!-- END_TABLE_SUMMARY -->

## 2. Lists of Solved Problems
<!-- START_TABLE_LIST -->
|   Idx | Source   | Level   | Problem   | Andy   | Charlie   |
|------:|:---------|:--------|:----------|:-------|:----------|
|     1 | baekjoon | bronze  | 1110.py   | ✅     | ❌        |
|     2 | baekjoon | bronze  | 2331.py   | ✅     | ✅        |
|     3 | baekjoon | silver  | 11650.py  | ❌     | ✅        |
|     4 | baekjoon | silver  | 1676.py   | ❌     | ✅        |
|     5 | baekjoon | bronze  | 2798.py   | ❌     | ✅        |
<!-- END_TABLE_LIST -->

## 3. Instruction to Sign-Up as User
1. Clone this repository to your local machine.
    ```
    git clone https://github.com/yheechan/problem_solving.git
    ```
2. Create a branch of your own and checkout to your own branch.
    ```
    git checkout -b <user-name>
    ```
3. Create a directory with ``<user-name>`` and begin adding codes for solved problems
    ```
    mkdir <user-name>
    ```
4. **Push and send PR** after adding scripts for solved problems to directory (as explained in [section4](#4-structure-of-solved-problems-within-user-name-directories)).
    ```
    git status
    git add .
    git commit -m "<user-name> solved <source> <level> <problem-id>"
    git push origin <user-name>
    ```

## 4. Structure of Solved Problems within ``<user-name>`` directories
```
├── README.md
├── <user-name>
│   └── <source>
│       ├── <level>
│       │   ├── <problem-id>.py
│       └── silver
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

<!-- START_LAST_UPDATED -->
Last Update: 2025 Feb 28
<!-- END_LAST_UPDATED -->
