from sys import stdin
N = int(stdin.readline().strip())

stack = []
for i in range(N):
    x = stdin.readline().split()
    if x[0] == "push":
        stack.append(x[1])
    elif x[0] == "pop":
        print(stack.pop() if stack else "-1")
    elif x[0] == "size":
        print(len(stack))
    elif x[0] == "empty":
        print("0" if stack else "1")
    elif x[0] == "top":
        print(stack[-1] if stack else "-1")


