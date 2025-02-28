def initiate_cabinet(n, w, num):
    floors = n // w
    remains = n % w
    if remains > 0: floors += 1
    cabinet = [[] for _ in range(floors)]
    direction = 1 # 1 for right, -1 for left
    item = 1
    curr_floor = 0
    y_max = w * floors
    while item <= y_max:
        tem = item if item <= n else -1
        if direction > 0:
            cabinet[curr_floor].append(tem)
        else:
            cabinet[curr_floor].insert(0, tem)
        item += 1
        if len(cabinet[curr_floor]) == w:
            curr_floor += 1
            direction *= -1
    return cabinet

def find_coord(cabinet, num):
    x, y = -1, -1
    for f in range(len(cabinet)):
        if num in cabinet[f]:
            x = f
            y = cabinet[f].index(num)
            break
    return x, y

def solution(n, w, num):
    cabinet = initiate_cabinet(n, w, num)
    x, y = find_coord(cabinet, num)
    answer = 0
    for f in range(len(cabinet)-1, -1, -1):
        if cabinet[f][y] == -1: continue
        answer += 1
        if cabinet[f][y] == num:
            break
    return answer
