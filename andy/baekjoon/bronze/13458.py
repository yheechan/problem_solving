import math
N = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

answer = N

a = [x - b for x in a]

for i in a:
    if i > 0:
        answer += math.ceil(i/c)
print(answer)
