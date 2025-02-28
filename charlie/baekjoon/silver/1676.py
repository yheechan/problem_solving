N = int(input())
def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)
N = str(fact(N))
count = 0
for i in range(len(N)-1, -1, -1):
    if N[i] == '0': count += 1
    else: break
print(count)