'''
    description: 给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。 返回 你可以获得的最大乘积 。
    method: 拆出一部分j，剩下的i-j要么不再拆分（直接乘上它），要么继续拆分（乘上dp[i-j]）
'''
def main():
    n = int(input())
    # 用dp[i]表示整数i拆分后的最大乘积
    dp = [0]*(n+1)
    # 为什么从2开始初始化，因为0和1不可再拆，2只能拆为1和1，最大乘积就是1
    dp[2] = 1
    # 枚举目标整数，从3到n
    for i in range(3,n+1):
        # 把整数i拆成j+(i-j)
        for j in range(1,i):
            # 状态转移方程：dp[i]表示保持历史最优，j*(i-j)表示不继续拆(i-j)，j*dp[i-j]表示继续拆i-j
            dp[i] = max(dp[i],j*(i-j),j*dp[i-j])
    print(dp[n])

if __name__ == "__main__":
    main()