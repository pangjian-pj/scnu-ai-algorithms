def coin_change(n:int)->list:
    coins = [2, 5, 7]
    INF = n + 1
    dp = [INF] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        for c in coins:
            if i >= c:
                dp[i] = min(dp[i], dp[i-c]+1)
    return dp

n = int(input())
dp = coin_change(n)
if dp[n] == n+1:
    print("-1")
else:
    print(dp[n])



