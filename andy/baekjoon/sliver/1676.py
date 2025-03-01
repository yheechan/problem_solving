def factorial (n):
    fac = 1
    for i in range(n):
        fac *= n
        n -= 1
    return fac

x = int(input())
fac = factorial(x)

count = 0
for i in str(fac)[::-1]:
    if i == str(0):
        count += 1
    else:
        print(count)
        break

