N = int(input())


def calc(n):
    bag = 0
    while n >= 0:
        if n % 5 == 0:  # If divisible by 5, we found the optimal solution
            bag += (n // 5)
            return bag
        n -= 3  # Otherwise, take one 3kg bag and try again
        bag += 1
    return -1   # If n becomes negative, it's impossible

print(calc(N))
