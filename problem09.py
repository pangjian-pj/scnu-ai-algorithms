def coin_change(n:int)->list:
    coins = [2, 5, 7]
    INF = n + 1
    # 初始化时，假设所有金额都无法凑出
    dp = [INF] * (n+1)
    dp[0] = 0
    # 外层循环，遍历金额
    for i in range(1, n+1):
        # 内层循环，遍历硬币
        for c in coins:
            # 只有当当前金额大于等于硬币面值时，才能使用
            if i >= c:
                # 状态转移方程，凑出i的最优解=凑出i-c的最优解+1
                dp[i] = min(dp[i], dp[i-c]+1)
    return dp

n = int(input())
dp = coin_change(n)
if dp[n] == n+1:
    print("-1")
else:
    print(dp[n])



