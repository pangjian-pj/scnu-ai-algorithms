'''
    description: 戳气球,动态规划
    method: dp[left][right] = 在开区间 (left, right) 内戳完所有气球能获得的最大硬币数
'''
def main():
    nums = list(map(int,input().split()))
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0]*n for _ in range(n)]

    # 枚举区间长度
    for length in range(2,n):
        for left in range(0, n-length):
            right = left + length
            # 枚举最后戳的气球
            for k in range(left+1,right):
                dp[left][right]=max(dp[left][right],dp[left][k]+nums[left]*nums[k]*nums[right]+dp[k][right])
    print(dp[0][n-1])

if __name__ == '__main__':
    main()

    
