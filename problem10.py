def main():
    m,n=input().split()
    m=int(m)
    n=int(n)
    # dp[i][j]表示从(1,1)走到(i,j)的不同路径数量
    dp=[[0]*(n+1) for _ in range(m+1)]
    # 对于第一列的元素来说，只能一直往下走，所以只有一种走法
    for i in range(1,m+1):
        dp[i][1]=1
    # 对于第一行的元素来说，只能一直往右走，所以也只有一种走法
    for j in range(1,n+1):
        dp[1][j]=1
    # 出发点不用走即可到达，因此初始化为0
    dp[1][1]=0
    for i in range(2,m+1):
        for j in range(2,n+1):
            # 到达(i,j)只能来自两个方向，从(i-1,j)向下或者从(i,j-1)向右
            # 这是一个典型的路径累加型dp，没有选择没有最优性，只有计数
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    print(dp[m][n])

if __name__ == "__main__":
    main()