



def dp(items, N, K):
    n = N
    dp = [[0]*(K+1) for _ in range(N+1)]

    # for each item
    for i in range(N+1):
        # for each weight
        for j in range(K+1):

            if i==0 and j==0:
                dp[i][j] = 0
            else:
                pick = 0

                if items[i-1][


    return res


def main():
    # N: number of items
    # K: weight limit
    N, K = map(int, input().split())
    items = []
    for _ in range(N):
        W, V = map(int, input().split())
        items.append((W, V))

    res = dp(items, N, K)
    print(res)

if __name__ == "__main__":

    main()


