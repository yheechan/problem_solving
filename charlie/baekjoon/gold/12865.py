def dp(items, N, K):
    n = N
    dp = [[0]*(K+1) for _ in range(N+1)]

    # for each item
    for i in range(N+1):
        # for each weight
        for j in range(K+1):

            if i==0 or j==0:
                dp[i][j] = 0
            else:
                pick = 0

                if items[i-1][0] <= j:
                    pick = items[i-1][1] + dp[i-1][j-items[i-1][0]]

                notpick = dp[i-1][j]
                dp[i][j] = max(pick, notpick)

    return dp[N][K]

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

