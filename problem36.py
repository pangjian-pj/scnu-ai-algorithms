'''
    经典背包问题
'''
def main():
    n, c = map(int,input().split())
    w_list = list(map(int, input().split()))
    v_list = list(map(int, input().split()))
    # dp[i]表示背包容量为j的时候，能装入物品的最大价值
    dp = [0]*(c+1)
    # 遍历每件物品
    for i in range(n):
        w,v= w_list[i],v_list[i]
        # 逆序遍历容量
        for j in range(c,w-1,-1):
            dp[j]=max(dp[j],dp[j-w]+v)
    print(max(dp))

if __name__ == '__main__':
    main()

