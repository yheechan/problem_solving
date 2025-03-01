def count(board, s_i, s_j):
    count2 = [0,0]
    for k in range(2):
        count = 0
        for i in range(s_i, s_i+8):
            for j in range(s_j, s_j+8):
                if i == s_i and j == s_j:
                    prev = board[i][j]
                    
                    if k == 0 and prev == 'W': # first start with B
                        prev = 'B'
                        count += 1
                    elif k == 1 and prev == 'B':
                        prev = 'W'
                        count += 1
                    continue
                
                if j > s_j:
                    if board[i][j] == prev:
                        count += 1
                        if prev == 'B':
                            prev = 'W'
                        else:
                            prev = 'B'
                    else:
                        prev = board[i][j] 
                else:
                    if board[i][j] != prev:
                        count += 1
        count2[k] = count
    return min(count2)




h, w = map(int, input().split())

board = [list(input()) for i in range(h)]
m = 3000
for i in range(h):
    for j in range(w):
        if i+7 < h and j+7 < w:
            cnt = count(board, i, j)
            if cnt < m:
                m = cnt
print(m)
