from sys import stdin 
N = int(input())

queue = []
for i in range(N):
    x = stdin.readline().split()
    
    if x[0] == "push":
        queue.append(x[1])
    elif x[0] == "pop":
        print(queue.pop(0) if queue else "-1")
    elif x[0] == "size":
        print(len(queue))
    elif x[0] == "empty":
        print("0" if queue else "1")
    elif x[0] == "front":
        print(queue[0] if queue else "-1")
    elif x[0] == "back":
        print(queue[-1] if queue else "-1")

